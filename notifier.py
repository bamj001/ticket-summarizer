import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email_notification(ticket, priority, category):
    if priority.lower() != "high":
        return
    
    subject =  "High Priority Ticket Alert"
    body = f"A high priority ticket was submitted under {category}:\n\n{ticket}"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # Or another admin/support address
    msg.set_content(body)

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("✅ Email notification sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
