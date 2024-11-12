import sqlite3

def create_connection():
    conn = sqlite3.connect('db/database.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS config_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            version TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_config(name, description, version):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO config_products (name, description, version)
        VALUES (?, ?, ?)
    ''', (name, description, version))
    conn.commit()
    conn.close()

def edit_config(config_id, name, description, version):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE config_products
        SET name = ?, description = ?, version = ?
        WHERE id = ?
    ''', (name, description, version, config_id))
    conn.commit()
    conn.close()


def delete_config(config_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM config_products WHERE id = ?', (config_id,))
    conn.commit()
    conn.close()