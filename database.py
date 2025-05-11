import sqlite3
from datetime import datetime

def initialize_db():
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS priorities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket TEXT,
            priority TEXT,
            category TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_ticket_to_db(ticket, priority, category):
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute('INSERT INTO priorities (ticket, priority, category, timestamp) VALUES (?, ?, ?, ?)',
              (ticket, priority, category, datetime.now().isoformat()))
    conn.commit()
    conn.close()
