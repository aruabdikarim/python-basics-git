import psycopg2
import json
import csv
from connect import get_connection

def import_csv(filename="contacts.csv"):
    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 1. First, ensure the group ID exists in the groups table
                # If your CSV uses names like 'Family', we look up the ID.
                # If it uses IDs, we ensure that ID exists.
                group_id = row['group_id']
                
                cur.execute("SELECT id FROM groups WHERE id = %s", (group_id,))
                if not cur.fetchone():
                    # If ID doesn't exist, create a placeholder group
                    cur.execute("INSERT INTO groups (id, name) VALUES (%s, %s)", 
                                (group_id, f"Group_{group_id}"))

                # 2. Now insert the contact
                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id) 
                    VALUES (%s, %s, %s, %s)
                """, (row['name'], row['email'], row['birthday'], group_id))
        
        conn.commit()
        print("CSV Import complete.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

def filter_by_group(group_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, g.name 
        FROM contacts c 
        JOIN groups g ON c.group_id = g.id 
        WHERE g.name = %s
    """, (group_name,))
    for row in cur.fetchall():
        print(f"Name: {row[0]}, Email: {row[1]}, Group: {row[2]}")
    conn.close()

def sort_contacts(by="name"):
    conn = get_connection()
    cur = conn.cursor()
    # Mapping user friendly names to DB columns
    allowed = {"name": "name", "birthday": "birthday", "date": "id"}
    sort_col = allowed.get(by, "name")
    
    cur.execute(f"SELECT name, email, birthday FROM contacts ORDER BY {sort_col}")
    for row in cur.fetchall():
        print(row)
    conn.close()

def paginate_contacts(limit=2):
    conn = get_connection()
    cur = conn.cursor()
    offset = 0
    while True:
        cur.execute("SELECT name, email FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        if not rows and offset > 0:
            print("--- End of list ---")
        elif not rows:
            print("No contacts found.")
            break
        
        for r in rows:
            print(f">> {r[0]} ({r[1]})")
            
        cmd = input("\n[N]ext, [P]rev, [Q]uit: ").lower()
        if cmd == 'n':
            offset += limit
        elif cmd == 'p':
            offset = max(0, offset - limit)
        elif cmd == 'q':
            break
    conn.close()

def export_to_json(filename="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name as group_name,
               COALESCE(json_agg(json_build_object('number', p.phone, 'type', p.type)) 
               FILTER (WHERE p.phone IS NOT NULL), '[]') as phones
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        GROUP BY c.id, g.name
    """)
    rows = cur.fetchall()
    data = []
    for r in rows:
        data.append({
            "name": r[0],
            "email": r[1],
            "birthday": str(r[2]) if r[2] else None,
            "group": r[3],
            "phones": r[4]
        })
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Exported to {filename}")
    conn.close()

def import_from_json(filename="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, "r") as f:
        data = json.load(f)

    for item in data:
        # 1. Ensure group exists
        cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (item['group'],))
        cur.execute("SELECT id FROM groups WHERE name = %s", (item['group'],))
        group_id = cur.fetchone()[0]

        # 2. Check for duplicate name
        cur.execute("SELECT id FROM contacts WHERE name = %s", (item['name'],))
        existing = cur.fetchone()

        if existing:
            action = input(f"Contact '{item['name']}' exists. [S]kip or [O]verwrite? ").lower()
            if action == 's': continue
            
            # Overwrite logic
            cur.execute("UPDATE contacts SET email=%s, birthday=%s, group_id=%s WHERE id=%s",
                        (item['email'], item['birthday'], group_id, existing[0]))
            cur.execute("DELETE FROM phones WHERE contact_id = %s", (existing[0],))
            contact_id = existing[0]
        else:
            cur.execute("INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
                        (item['name'], item['email'], item['birthday'], group_id))
            contact_id = cur.fetchone()[0]

        # 3. Insert Phones
        for p in item.get('phones', []):
            cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                        (contact_id, p['number'], p['type']))
    
    conn.commit()
    conn.close()
    print("JSON Import complete.")

def call_add_phone_proc(name, phone, ptype):
    conn = get_connection()
    cur = conn.cursor()
    # Убедись, что здесь CALL add_phone и 3 параметра
    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
    conn.commit()
    conn.close()
    print("Phone added successfully!")

def main_menu():
    while True:
        print("\n--- Phonebook ---")
        print("1. Import from CSV")
        print("2. Import from JSON")
        print("3. Paginated View (Next/Prev)")
        print("4. Search Contacts (Name/Email/Phone)")
        print("5. Sort Contacts")
        print("6. Filter by Group")
        print("7. Add Phone to Contact (Procedure)")
        print("8. Export to JSON")
        print("0. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            import_csv("contacts.csv")
        elif choice == '2':
            import_from_json("contacts.json")
        elif choice == '3':
            paginate_contacts(limit=2)
        elif choice == '4':
            query = input("Enter search term: ")
            # Calling the SQL function via Python
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM search_contacts_func(%s)", (query,))
            for row in cur.fetchall():
                print(row)
            conn.close()
        elif choice == '5':
            sort_val = input("Sort by (name, birthday, date): ")
            sort_contacts(sort_val)
        elif choice == '6':
            grp = input("Enter group name: ")
            filter_by_group(grp)
        elif choice == '7':
            name = input("Contact name: ")
            num = input("Phone number: ")
            ptype = input("Type (home, work, mobile): ")
            call_add_phone_proc(name, num, ptype)
        elif choice == '8':
            export_to_json("exported_contacts.json")
        elif choice == '0':
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
