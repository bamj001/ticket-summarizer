import sys
from summarizer import summarize
from sentiment import analyze_sentiment
from categorizer import categorize_ticket
from prioritizer import prioritize_ticket
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py [summarize|sentiment|categorize|priority] \"Your ticket text here\"")
        return

    command = sys.argv[1].lower()
    ticket = " ".join(sys.argv[2:])

    if command == "summarize":
        summarize(ticket)
    elif command == "sentiment":
        analyze_sentiment(ticket)
    elif command == "categorize":
        categorize_ticket(ticket)
    elif command == "priority":
        prioritize_ticket(ticket)
    else:
        print(f"Unknown command: {command}")
        print("Usage: python main.py [summarize|sentiment|categorize|priority] \"Your ticket text here\"")

if __name__ == "__main__":
    main()
