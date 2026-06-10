"""
Live NAV Fetch Utility

Fetches latest mutual fund NAV values from
external sources and updates local datasets.
"""

from pathlib import Path
import requests
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    try:

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(
            data["data"]
        )

        filename = (
            RAW_DIR
            / f"{name}_nav.csv"
        )

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"Saved {filename}"
        )

    except Exception as e:

        print(
            f"Failed for {name}: {e}"
        )