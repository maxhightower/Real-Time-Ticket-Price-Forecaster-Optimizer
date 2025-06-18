import requests
import os

def fetch_fivethirtyeight():
    """
    Download the FiveThirtyEight NFL ticket-prices CSV into data/raw/.
    """
    os.makedirs("data/raw", exist_ok=True)
    url = (
        "https://raw.githubusercontent.com/"
        "fivethirtyeight/data/master/"
        "nfl-ticket-prices/nfl-ticket-data.csv"
    )
    resp = requests.get(url)
    resp.raise_for_status()
    out_path = "data/raw/nfl-ticket-data.csv"
    with open(out_path, "wb") as f:
        f.write(resp.content)
    print(f"Downloaded FiveThirtyEight NFL ticket data to {out_path}")

if __name__ == "__main__":
    fetch_fivethirtyeight()
