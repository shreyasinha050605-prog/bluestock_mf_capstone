from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"
DB_DIR = DATA_DIR / "db"

engine = create_engine(
    f"sqlite:///{DB_DIR/'bluestock_mf.db'}"
)

files = {
    "fund_master": PROCESSED_DIR / "01_fund_master_clean.csv",
    "nav_history": PROCESSED_DIR / "02_nav_history_clean.csv",
    "aum": PROCESSED_DIR / "03_aum_clean.csv",
    "sip": PROCESSED_DIR / "04_sip_clean.csv",
    "category": PROCESSED_DIR / "05_category_clean.csv",
    "folios": PROCESSED_DIR / "06_folios_clean.csv",
    "performance": PROCESSED_DIR / "07_performance_clean.csv",
    "transactions": PROCESSED_DIR / "08_transactions_clean.csv",
    "holdings": PROCESSED_DIR / "09_holdings_clean.csv",
    "benchmark": PROCESSED_DIR / "10_benchmark_clean.csv"
}

for table, path in files.items():

    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(table, len(df))

print("\nAll tables loaded successfully.")