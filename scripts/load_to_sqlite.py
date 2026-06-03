import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:////Users/shreyasinha/Desktop/bluestock_mf_capstone/data/db/bluestock_mf.db"
)
base = "/Users/shreyasinha/Desktop/bluestock_mf_capstone"

files = {
    "fund_master": f"{base}/data/processed/01_fund_master_clean.csv",
    "nav_history": f"{base}/data/processed/02_nav_history_clean.csv",
    "aum": f"{base}/data/processed/03_aum_clean.csv",
    "sip": f"{base}/data/processed/04_sip_clean.csv",
    "category": f"{base}/data/processed/05_category_clean.csv",
    "folios": f"{base}/data/processed/06_folios_clean.csv",
    "performance": f"{base}/data/processed/07_performance_clean.csv",
    "transactions": f"{base}/data/processed/08_transactions_clean.csv",
    "holdings": f"{base}/data/processed/09_holdings_clean.csv",
    "benchmark": f"{base}/data/processed/10_benchmark_clean.csv"
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
    