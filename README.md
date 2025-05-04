# 🎟️ Ticket Summarizer

A Python-based CLI tool that uses OpenAI's GPT API to summarize customer support tickets, analyze sentiment, and categorize them — with results saved to a local SQLite database.

---

## ✨ Features

- 🔍 **Summarization** — Generates concise summaries of support tickets  
- 📊 **Sentiment Analysis** — Detects whether a ticket is positive, neutral, or negative  
- 🏷️ **Categorization** — Labels tickets into appropriate categories  
- 💾 **Database Logging** — All results are saved to `tickets.db` with timestamps  
- 📂 **Batch Mode** — Summarize multiple tickets from a text file  

---

## 🚀 Setup

### 1. Clone the Repo

git clone https://github.com/YOUR_USERNAME/ticket-summarizer.git
cd ticket-summarizer

### 2. Create and Activate a Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Add Your OpenAI API Key

Create a `.env` file in the root directory:

OPENAI_API_KEY=your-openai-api-key-here

---

## 🧠 Usage

### Summarize a Single Ticket

python summarizer.py "The customer says their payment failed even though they were charged."

### Summarize a Batch of Tickets

python summarizer.py batch tickets.txt

Where `tickets.txt` contains one ticket per line.

### Analyze Sentiment

python sentiment.py "I'm really upset that my issue hasn't been resolved."

### Categorize Ticket

python categorizer.py "I'd like to upgrade my plan to the premium subscription."

---

## 🗄️ Database Schema (`tickets.db`)

Each feature writes to its own table:

- `summaries(id, ticket, summary, timestamp)`
- `sentiments(id, ticket, sentiment, timestamp)`
- `categories(id, ticket, category, timestamp)`

You can explore the data using SQLite tools like DB Browser for SQLite.

---

## 📦 Requirements

See `requirements.txt`:

openai  
python-dotenv

---

## ✅ Example

$ python summarizer.py "My order arrived damaged. I want a refund."
Summary:
The customer received a damaged order and is requesting a refund.

---

## 🛠️ License

MIT — do what you want, just don't blame me.

---

## 💬 Questions?

Open an issue or contact me on GitHub: https://github.com/bamj001
