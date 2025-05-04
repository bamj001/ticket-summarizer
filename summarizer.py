from openai import OpenAI
import os
import sqlite3
import datetime
import sys
from dotenv import load_dotenv
# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# SQLite setup
conn = sqlite3.connect('tickets.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_text TEXT,
    summary TEXT,
    created_at TIMESTAMP
)
''')

def summarize(text):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional support assistant."},
        {"role": "user", "content": f"Summarize this ticket in 2 sentences:\n\n{text}"}
    ],
    temperature=0.3)
    return response.choices[0].message.content.strip()

def save_to_db(original, summary):
    c.execute(
        'INSERT INTO tickets (original_text, summary, created_at) VALUES (?, ?, ?)',
        (original, summary, datetime.datetime.now())
    )
    conn.commit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py 'Your ticket text here'")
    else:
        text = sys.argv[1]
        summary = summarize(text)
        save_to_db(text, summary)
        print(f"\n✅ Summary:\n{summary}\n\n💾 Saved to tickets.db")