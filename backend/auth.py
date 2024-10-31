import sqlite3

def register_user(username, proof):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, proof) VALUES (?, ?)", (username, proof))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    username = input("Enter your username: ")
    proof = input("Enter your proof: ")
    register_user(username, proof)
    print(f"User {username} registered successfully.")
