import pandas as pd
import sqlite3
from pathlib import Path
import sys

def build_sqlite_db():
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect("data/processed/tickets.db")

    ticket_csv = Path("data/raw/nfl-ticket-data.csv")
    if not ticket_csv.exists():
        sys.exit("✖ Expected data/raw/nfl-ticket-data.csv – run fetch_fivethirtyeight.py first")

    ticket_df = pd.read_csv(ticket_csv)
    ticket_df.to_sql("ticket_prices", conn, if_exists="replace", index=False)

    sg_json = Path("data/raw/seatgeek_events.json")
    if sg_json.exists():
        event_df = pd.read_json(sg_json)
        event_df.to_sql("seatgeek_events", conn, if_exists="replace", index=False)
    else:
        print("⚠ No SeatGeek events file found; skipping that table.")

    conn.commit()
    conn.close()
    print("✔ Built SQLite DB at data/processed/tickets.db")

if __name__ == "__main__":
    build_sqlite_db()
