"""
Star Schema Loader

Creates analytical tables and relationships
required for business intelligence reporting.
"""

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

# Load cleaned files
fund_master = pd.read_csv(
    PROCESSED_DIR / "01_fund_master_clean.csv"
)

nav_history = pd.read_csv(
    PROCESSED_DIR / "02_nav_history_clean.csv"
)

transactions = pd.read_csv(
    PROCESSED_DIR / "08_transactions_clean.csv"
)

performance = pd.read_csv(
    PROCESSED_DIR / "07_performance_clean.csv"
)

aum = pd.read_csv(
    PROCESSED_DIR / "03_aum_clean.csv"
)

# DIM_FUND
dim_fund = fund_master[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "risk_category"
    ]
]

# FACT_NAV
fact_nav = nav_history.rename(
    columns={
        "date": "nav_date"
    }
)

fact_nav["daily_return"] = (
    fact_nav
    .groupby("amfi_code")["nav"]
    .pct_change(fill_method=None) * 100
)

# FACT_TRANSACTIONS
fact_transactions = transactions[
    [
        "investor_id",
        "transaction_date",
        "amfi_code",
        "transaction_type",
        "amount_inr"
    ]
]

# FACT_PERFORMANCE
fact_performance = performance[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "sharpe_ratio",
        "expense_ratio_pct"
    ]
]

# FACT_AUM
fact_aum = aum[
    [
        "fund_house",
        "date",
        "aum_crore"
    ]
]

# Load into SQLite

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

fact_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

fact_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Star schema tables loaded successfully.")