from openai import OpenAI
from dotenv import load_dotenv
import os
from notifier import send_email_notification
from database import save_ticket_to_db, initialize_db

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_priority(ticket):
    try:
        prompt = f"Classify the priority of this support ticket as High, Medium, or Low:\n\n\"{ticket}\""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Failed to classify priority: {e}")
        return None

def classify_category(ticket):
    try:
        prompt = f"Classify this support ticket into a category such as Technical, Billing, Account, or Other:\n\n\"{ticket}\""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Failed to classify category: {e}")
        return None

def prioritize_ticket(ticket):
    # Avoid running DB initialization multiple times
    # Ensure this is called only once when the app starts
    initialize_db()

    priority = classify_priority(ticket)
    category = classify_category(ticket)

    if not priority or not category:
        return None, None

    print(f"Priority: {priority} | Category: {category}")

    try:
        save_ticket_to_db(ticket, priority, category)
    except Exception as db_error:
        print(f"[ERROR] Failed to save to database: {db_error}")
        return None, None

    send_email_notification(ticket, priority, category)

    return priority, category
