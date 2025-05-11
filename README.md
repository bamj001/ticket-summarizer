
# Ticket Prioritizer App

## Overview

This project is a web-based ticket prioritization system that uses AI to classify support tickets. It leverages OpenAI's GPT-3.5 to assign priority levels (High, Medium, or Low) and categories (e.g., Technical, Billing, Account) to support tickets. The app also includes a history page where users can view previously classified tickets.

## Features

### 1. **Submit Ticket**
- Users can submit a support ticket through the form.
- The ticket description is analyzed by OpenAI's model to determine its priority and category.
- After submission, the result is displayed in a modal on the same page.

### 2. **Ticket History**
- A history page is available to view all submitted tickets, with their respective priorities, categories, and timestamps.

### 3. **Email Notifications**
- High-priority tickets trigger an email notification to the admin.

### 4. **Loading Spinner**
- A loading spinner is shown while the ticket is being processed and disappears once the result is ready.

### 5. **Validation**
- Ensures that the ticket description is not empty before submission.
- Gracefully handles errors from OpenAI or database interactions.

## Technologies Used
- Python
- Flask (for the web server)
- SQLite (for ticket storage)
- OpenAI API (for AI-driven classification)
- Jinja2 (for templating)
- HTML, CSS, and JavaScript (for the front-end)

## Setup

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/ticket-prioritizer.git
   cd ticket-prioritizer
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

4. **Run the app**
   ```
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://127.0.0.1:5000/`

## File Structure

- `app.py` - The main Flask application file.
- `templates/` - Contains HTML files for the frontend.
- `static/` - Contains CSS and JavaScript files.
- `prioritizer.py` - Contains the AI logic to classify ticket priority and category.
- `notifier.py` - Handles email notifications for high-priority tickets.
- `database.py` - Handles SQLite database interactions for storing tickets.
- `cli/` - Contains scripts for running the application in a CLI environment.

## Future Enhancements
- Add more complex filtering options for the history page.
- Implement user authentication for restricted access to the history page.
- Improve the UX/UI of the app.

## License
MIT License.


## 💬 Questions?

Open an issue or contact me on GitHub: https://github.com/bamj001
