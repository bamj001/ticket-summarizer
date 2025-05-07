from flask import Flask, render_template, request
from prioritizer import prioritize_ticket
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticket = request.form["ticket"]
        # Get both category and priority from the prioritizer
        category, priority = prioritize_ticket(ticket)
        return render_template("index.html", ticket=ticket, priority=priority, category=category)
    return render_template("index.html")

@app.route("/history")
def history():
    # Fetch the history of tickets from the database
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute("SELECT * FROM priorities")
    tickets = c.fetchall()
    conn.close()
    return render_template("history.html", tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
