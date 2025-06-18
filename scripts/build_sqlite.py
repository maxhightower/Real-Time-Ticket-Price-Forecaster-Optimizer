import pandas as pd
import sqlite3
import os

def build_sqlite_db():
    os.makedirs("data/processed", exist_ok=True)
    conn = sqlite3.connect("data/processed/tickets.db")
    
    ticket_df = pd.read_csv("data/raw/nfl-ticket-data.csv")
    ticket_df.to_sql("ticket_prices", conn, if_exists="replace", index=False)

    event_df = pd.read_json("data/raw/seatgeek_events.json")
    event_df.to_sql("seatgeek_events", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    build_sqlite_db()
