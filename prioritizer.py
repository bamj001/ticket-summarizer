from openai import OpenAI
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prioritize_ticket(ticket):
    # Context and improved prompt for GPT-3.5
    prompt = f"""
    You are a support ticket prioritization assistant.
    Classify the following support ticket into the appropriate category and assign it a priority (High, Medium, Low). 
    Consider factors like the nature of the issue, urgency, and business impact.

    Ticket Description:
    "{ticket}"

    Output should be a JSON object with 'category' and 'priority' fields like so:
    {{ "category": "<category_name>", "priority": "<priority_level>" }}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content.strip()

    # Parse JSON output from GPT model
    try:
        output = json.loads(result)
        category = output.get("category", "Unknown")
        priority = output.get("priority", "Low")
    except json.JSONDecodeError:
        category, priority = "Unknown", "Low"

    print(f"Category: {category}, Priority: {priority}")

    # Save to database
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS priorities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticket TEXT,
                    category TEXT,
                    priority TEXT,
                    timestamp TEXT)''')
    c.execute('INSERT INTO priorities (ticket, category, priority, timestamp) VALUES (?, ?, ?, ?)',
              (ticket, category, priority, datetime.now().isoformat()))
    conn.commit()
    conn.close()

    return category, priority
