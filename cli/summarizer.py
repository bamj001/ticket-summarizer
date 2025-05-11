from openai import OpenAI
import os
import sqlite3
import datetime
import sys
from dotenv import load_dotenv
# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# SQLite DB setup
DB_FILE = "tickets.db"

# SQLite setup
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_text TEXT,
        summary TEXT,
        created_at TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def save_to_db(original, summary):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        'INSERT INTO tickets (original_text, summary, created_at) VALUES (?, ?, ?)',
        (original, summary, datetime.datetime.now())
    )
    conn.commit()
    conn.close()

# Function to summarize a single ticket
def summarize(text):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional support assistant."},
        {"role": "user", "content": f"Summarize this ticket in 2 sentences:\n\n{text}"}
    ],
    temperature=0.3)
    summary = response.choices[0].message.content.strip()
    save_to_db(text,summary)
    return summary

# Function to summarize a batch of tickets from a file
def summarize_batch(file_path):
    with open(file_path, "r") as file:
        tickets = file.readlines()
    summaries = []
    for ticket in tickets:
        summary = summarize(ticket.strip())
        summaries.append(summary)
    return summaries

if __name__ == "__main__":
    import sys

    init_db()

    if len(sys.argv) == 3 and sys.argv[1] == "batch":
        file_path = sys.argv[2]
        print(f"Summarizing tickets from {file_path}...\n")
        summaries = summarize_batch(file_path)
        for i, s in enumerate(summaries, start=1):
            print(f"Ticket {i}: {s}\n")

    elif len(sys.argv) == 2:
        ticket = sys.argv[1]
        summary = summarize(ticket)
        print("Summary:\n", summary)

    else:
        print("Usage:")
        print("  python summarizer.py \"<ticket text>\"")
        print("  python summarizer.py batch <path_to_text_file>")