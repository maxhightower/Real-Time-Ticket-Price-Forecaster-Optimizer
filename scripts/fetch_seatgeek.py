import requests
import json
import os
from pathlib import Path
import datetime as dt

BASE_URL = "https://api.seatgeek.com/2/events"
DEFAULT_QUERY = "nfl"
DEFAULT_PAGE_SIZE = 50

# SeatGeek now requires at least a client_id even for low‑volume usage.
CLIENT_ID = os.getenv("SEATGEEK_CLIENT_ID")  # create a free dev account to get this
CLIENT_SECRET = os.getenv("SEATGEEK_CLIENT_SECRET")  # optional but improves quota


def _build_params(query: str, per_page: int):
    params = {"q": query, "per_page": per_page}
    if CLIENT_ID:
        params["client_id"] = CLIENT_ID
    if CLIENT_SECRET:
        params["client_secret"] = CLIENT_SECRET
    return params


def fetch_seatgeek_events(query: str = DEFAULT_QUERY, per_page: int = DEFAULT_PAGE_SIZE):
    params = _build_params(query, per_page)
    resp = requests.get(BASE_URL, params=params, timeout=30)
    if resp.status_code == 200:
        return resp.json()
    elif resp.status_code == 403:
        raise RuntimeError(
            "SeatGeek API returned 403 Forbidden. Set SEATGEEK_CLIENT_ID env var "
            "(free at https://platform.seatgeek.com) and re‑run."
        )
    else:
        resp.raise_for_status()


def save_raw_data(data, filename: str = "data/raw/seatgeek_events.json"):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main():
    data = fetch_seatgeek_events()
    save_raw_data(data)
    print(
        f"✔ Fetched {len(data.get('events', []))} events on {dt.date.today()} → data/raw/seatgeek_events.json"
    )


if __name__ == "__main__":
    main()
