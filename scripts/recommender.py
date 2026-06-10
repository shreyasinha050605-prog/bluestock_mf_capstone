from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

perf = pd.read_csv(
    DATA_DIR / "07_performance_clean.csv"
)

def recommend_funds(risk_level):

    result = (
        perf[
            perf["risk_grade"]
            .str.lower()
            ==
            risk_level.lower()
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]

if __name__ == "__main__":

    risk = input(
        "Enter Risk Level (Low/Moderate/High): "
    )

    print("\nRecommended Funds:\n")

    print(
        recommend_funds(risk)
    )