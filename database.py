import sqlite3

DB_NAME = "hats.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS hats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hat_name TEXT NOT NULL,
        hat_color TEXT NOT NULL,
        size TEXT
    )""")

    conn.commit()
    conn.close()

def connect_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

if __name__ == "__main__":
    create_table()
    print("✅ Database created")
