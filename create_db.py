import sqlite3
from tkinter import messagebox

def initialize_database():
    conn = sqlite3.connect('items.db')
    curr = conn.cursor()

    # Create groups table
    curr.execute('''CREATE TABLE IF NOT EXISTS groups (
                        group_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        group_name TEXT NOT NULL)''')

    # Create items table (fixed the typo)
    curr.execute('''CREATE TABLE IF NOT EXISTS items (
                        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_name TEXT NOT NULL,
                        quantity INTEGER NULL,
                        sell_price REAL NULL,
                        buy_price REAL NULL,
                        group_id INTEGER,
                        FOREIGN KEY(group_id) REFERENCES groups(group_id))''')

    # Create packaging table
    curr.execute('''CREATE TABLE IF NOT EXISTS fills (
                        packaging_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        length REAL NOT NULL,
                        meter REAL NOT NULL,
                        total_price REAL NOT NULL,
                        sell_price REAL NOT NULL,
                        buy_price REAL NOT NULL)''')

    conn.commit()
    conn.close()



# Function to insert items
def insert_items(item_name, quantity, sell_price, buy_price, group_id):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO items (item_name, quantity, sell_price, buy_price, group_id)
                      VALUES (?, ?, ?, ?, ?)''', (item_name,  quantity, sell_price, buy_price, group_id))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Item added successfully!")


#fun insert group
def insert_groups(group_name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO groups (group_name) VALUES (?)''', (group_name,))
    conn.commit()
    conn.close()
    return group_name




# Function to get items from the database
def get_items():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("SELECT item_name FROM items")
    rows = cursor.fetchall()

    for row in rows:
        print(row)  # Print to console (you can display in Tkinter widget too)

    conn.close()


def get_groups():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("SELECT group_name FROM groups")
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # Print to console (you can display in Tkinter widget too)
        conn.close()
        return rows
    
def delete_group(group_name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM groups WHERE group_name = ?", (group_name,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Group deleted successfully!")

    

# Function to delete an item (fixed the column name)
def delete_item(item_name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE item_name = ?", (item_name,))  # Use the correct column name
    conn.commit()
    conn.close()
