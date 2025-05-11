from flask import Flask, render_template, request
from prioritizer import prioritize_ticket
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit_ticket", methods=["POST"])
def submit_ticket():
    if request.method == "POST":
        ticket = request.form.get("ticket", "").strip()

        if not ticket:
            # Handle empty input
            return render_template("index.html", error="Ticket cannot be empty.")

        try:
            # Get both category and priority from the prioritizer
            priority, category = prioritize_ticket(ticket)
            return render_template("index.html", ticket=ticket, priority=priority, category=category)
        except Exception as e:
            print("Error processing ticket:", e)
            return render_template("index.html", error="Something went wrong while processing the ticket. Please try again.")

    return render_template("index.html")

@app.route('/history', methods=['GET'])
def history():
    # Get the sorting/filtering criteria from the URL parameters (if any)
    sort_by = request.args.get('sort_by', 'timestamp')  # Default is sorting by timestamp
    filter_priority = request.args.get('filter_priority', '')
    filter_category = request.args.get('filter_category', '')

    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()

    query = "SELECT * FROM priorities WHERE 1=1"
    
    # Apply filters if provided
    if filter_priority:
        query += f" AND priority = '{filter_priority}'"
    if filter_category:
        query += f" AND category = '{filter_category}'"
    
    query += f" ORDER BY {sort_by}"  # Sorting by the chosen column

    c.execute(query)
    tickets = c.fetchall()
    conn.close()

    return render_template('history.html', tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
