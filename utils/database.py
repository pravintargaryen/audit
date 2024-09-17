import sqlite3

def create_db():
    conn = sqlite3.connect("audit_logs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            action TEXT,
            resource TEXT,
            decision TEXT,
            encrypted_log TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(user, action, resource, decision, encrypted_log):
    conn = sqlite3.connect("audit_logs.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (user, action, resource, decision, encrypted_log)
        VALUES (?, ?, ?, ?, ?)
    ''', (user, action, resource, decision, encrypted_log))
    conn.commit()
    conn.close()

def fetch_logs():
    conn = sqlite3.connect("audit_logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    return cursor.fetchall()
