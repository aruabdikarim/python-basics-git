-- Procedure to add phone by contact name
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INTEGER;
BEGIN
    -- Find the contact ID using the 'name' column
    SELECT id INTO v_id FROM contacts WHERE name = p_name;
    
    IF v_id IS NOT NULL THEN
        INSERT INTO phones(contact_id, phone, type) VALUES (v_id, p_phone, p_type);
    ELSE
        RAISE NOTICE 'Contact % not found', p_name;
    END IF;
END;
$$;

-- Procedure to move contact to group (creates group if missing)
CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    g_id INTEGER;
BEGIN
    SELECT id INTO g_id FROM groups WHERE name = p_group_name;
    IF g_id IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group_name) RETURNING id INTO g_id;
    END IF;
    UPDATE contacts SET group_id = g_id WHERE name = p_contact_name;
END;
$$;

-- Function for pattern search across name, email, and phones
CREATE OR REPLACE FUNCTION search_contacts_func(p_query TEXT)
RETURNS TABLE(contact_name VARCHAR, contact_email VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%'||p_query||'%'
       OR c.email ILIKE '%'||p_query||'%'
       OR p.phone ILIKE '%'||p_query||'%';
END;
$$ LANGUAGE plpgsql;