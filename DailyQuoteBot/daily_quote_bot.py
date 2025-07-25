import requests
import json
from datetime import datetime
import os

API_URL = "https://api.quotable.io/random"
QUOTES_FILE = os.path.join(os.path.dirname(__file__), "quotes.json")

# Optional Telegram integration via environment variables
BOT_TOKEN = os.getenv("DAILY_QUOTE_BOT_TOKEN")
CHAT_ID = os.getenv("DAILY_QUOTE_CHAT_ID")


def fetch_quote():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["content"], data["author"]


def save_quote(quote, author):
    entry = {
        "quote": quote,
        "author": author,
        "timestamp": datetime.now().isoformat()
    }
    quotes = []
    if os.path.exists(QUOTES_FILE):
        try:
            with open(QUOTES_FILE, "r", encoding="utf-8") as f:
                quotes = json.load(f)
        except json.JSONDecodeError:
            quotes = []
    quotes.append(entry)
    with open(QUOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)


def send_to_telegram(quote, author):
    if not BOT_TOKEN or not CHAT_ID:
        return
    message = f"\u275D{quote}\u275E\n— *{author}*"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload, timeout=10)
    except requests.RequestException:
        pass


def main():
    try:
        quote, author = fetch_quote()
    except requests.RequestException as exc:
        print(f"Erro ao obter citação: {exc}")
        return
    formatted = f"\"{quote}\"\n  — {author}"
    print(formatted)
    save_quote(quote, author)
    send_to_telegram(quote, author)


if __name__ == "__main__":
    main()
