# Ticket Prioritizer 🎫✨

A web-based tool that uses AI to classify support tickets as **High**, **Medium**, or **Low** priority and categorize them into different categories (e.g., "Technical", "Billing", etc.). This application allows users to submit tickets, receive priority classifications, and view past tickets with their categories.

## Features 🛠️

- **Submit Ticket**: A form where users can input a support ticket description. ✍️
- **Prioritize Ticket**: The AI classifies the ticket as High, Medium, or Low priority. 📊
- **Categorize Ticket**: The AI classifies the ticket into a category such as "Technical", "Billing", etc. 🗂️
- **Email Notification**: Once a ticket is prioritized and categorized, an email is sent to notify the user. 📧
- **History Page**: Displays a list of previously submitted tickets, along with their priorities, categories, and timestamps. 🕒
- **Modal**: After submitting a ticket, the result (ticket description, priority, category) is displayed in a modal window. 💬
- **Top Navigation Bar**: Switch between the Submit Ticket and History pages. 🔝

## Installation 🖥️

### Requirements

- Python 3.8 or higher 🐍
- SQLite 🗄️
- Flask 🌐
- OpenAI API key 🌟

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ticket-summarizer.git
   cd ticket-summarizer
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:
   - Create a `.env` file in the root directory.
   - Add your API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## File Structure 📁

```
ticket-summarizer/
├── app.py                # Main Flask app
├── prioritizer.py        # Logic for ticket prioritization and categorization using OpenAI
├── notifier.py           # Logic for sending email notifications
├── templates/
│   ├── index.html        # Submit Ticket page
│   └── history.html      # History page
├── static/
│   ├── styles.css        # Styling for the pages
│   └── script.js          # Modal logic for ticket prioritization and categorization result
└── tickets.db            # SQLite database for storing tickets
```

## Endpoints 🚀

- **`/`**: Submit a ticket and get a priority and category classification.
- **`/history`**: View previously submitted tickets and their priorities and categories.

## Technologies Used 🧰

- **Flask**: Web framework for Python.
- **SQLite**: Local database for storing tickets and priorities.
- **OpenAI**: AI model for classifying ticket priorities and categories.
- **Jinja2**: Templating engine for rendering dynamic content in HTML.
- **HTML/CSS/JavaScript**: Frontend for user interface.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Questions?

Open an issue or contact me on GitHub: https://github.com/bamj001
