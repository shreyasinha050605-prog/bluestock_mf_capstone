import pandas as pd
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

output_path = REPORT_DIR / "data_ingestion_output.txt"

with open(
    output_path,
    "w"
) as output_file:

    for file in os.listdir(RAW_DIR):

        if file.endswith(".csv"):

            file_path = RAW_DIR / file

            df = pd.read_csv(file_path)

            output_file.write(
                "\n" + "=" * 50 + "\n"
            )

            output_file.write(
                f"FILE: {file}\n"
            )

            output_file.write(
                "\nSHAPE:\n"
            )

            output_file.write(
                str(df.shape) + "\n"
            )

            output_file.write(
                "\nDATA TYPES:\n"
            )

            output_file.write(
                str(df.dtypes) + "\n"
            )

            output_file.write(
                "\nFIRST 5 ROWS:\n"
            )

            output_file.write(
                str(df.head()) + "\n"
            )

print("Data ingestion report generated successfully.")