import requests
import json
import os
from pathlib import Path

def fetch_seatgeek_events(query="nfl", per_page=50):
    url = f"https://api.seatgeek.com/2/events?q={query}&per_page={per_page}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_raw_data(data, filename="data/raw/seatgeek_events.json"):
    os.makedirs(Path(filename).parent, exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    data = fetch_seatgeek_events()
    save_raw_data(data)
