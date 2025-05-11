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
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(ticket, sentiment):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sentiments (ticket, sentiment, timestamp)
        VALUES (?, ?, ?)
    ''', (ticket, sentiment, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def analyze_sentiment(ticket_text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": f"Analyze the sentiment of this customer support ticket: {ticket_text}"}
        ]
    )
    sentiment = response.choices[0].message.content.strip()
    save_to_db(ticket_text, sentiment)
    return sentiment

if __name__ == "__main__":
    import sys

    init_db()

    if len(sys.argv) == 2:
        ticket = sys.argv[1]
        sentiment = analyze_sentiment(ticket)
        print("Sentiment:", sentiment)
    else:
        print("Usage:")
        print("  python sentiment.py \"<ticket text>\"")
