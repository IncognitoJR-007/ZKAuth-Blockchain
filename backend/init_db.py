import sqlite3

def initialize_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Create a table for users with columns for username and proof
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        proof TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
