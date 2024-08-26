import sqlite3
def initialize_database():
    conn = sqlite3.connect('items.db')
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS inventory (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      fills TEXT, category TEXT
                    )''')

    conn.commit()
    conn.close()

def insert_items(item_name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (?)", (item_name,))
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM items")
    items = cursor.fetchall()
    conn.close()

    return items

def delete_item(item_name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE name = ?", (item_name,))
    conn.commit()
    conn.close()
    