import pandas as pd

perf = pd.read_csv(
    "../data/processed/07_performance_clean.csv"
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
        "Enter Risk Level: "
    )

    print(
        recommend_funds(risk)
    )