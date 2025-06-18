import requests
import os
from pathlib import Path

DATA_URLS = [
    # Primary (new) path
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-ticket-prices/nfl-ticket-prices.csv",
    # Legacy mirrors
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-01-23/nfl_ticket_prices.csv",
]

def download_file(url: str, dest: Path):
    resp = requests.get(url, timeout=30)
    if resp.status_code == 200:
        dest.write_bytes(resp.content)
        return True
    return False

def fetch_fivethirtyeight():
    """Download NFL ticket‐price CSV into data/raw/. Tries multiple mirrors."""
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    out_path = Path("data/raw/nfl-ticket-data.csv")
    for url in DATA_URLS:
        if download_file(url, out_path):
            print(f"✔ Downloaded data from {url}")
            return
        else:
            print(f"⚠ Failed to download from {url} (status != 200)")
    raise RuntimeError("All download sources failed for FiveThirtyEight dataset.")

if __name__ == "__main__":
    fetch_fivethirtyeight()
