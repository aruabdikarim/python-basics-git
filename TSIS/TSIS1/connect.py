import psycopg2              # библиотека для работы с PostgreSQL
from config import DB_CONFIG # словарь с параметрами подключения из config.py

def get_connection():
    # функция возвращает соединение с базой данных
    return psycopg2.connect(**DB_CONFIG)

if __name__ == "__main__":
    conn = get_connection()           # подключаемся к базе
    print("Соединение установлено!")  # выводим сообщение
    conn.close()         