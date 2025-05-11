from openai import OpenAI
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DB_FILE = "tickets.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket TEXT NOT NULL,
            category TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(ticket, category):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO categories (ticket, category, timestamp)
        VALUES (?, ?, ?)
    ''', (ticket, category, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def categorize_ticket(ticket_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a support assistant."},
            {"role": "user", "content": f"Categorize the following customer support ticket: {ticket_text}"}
        ]
    )
    category = response.choices[0].message.content.strip()
    save_to_db(ticket_text, category)
    return category

if __name__ == "__main__":
    import sys

    init_db()

    if len(sys.argv) == 2:
        ticket = sys.argv[1]
        category = categorize_ticket(ticket)
        print("Category:", category)
    else:
        print("Usage:")
        print("  python categorizer.py \"<ticket text>\"")
