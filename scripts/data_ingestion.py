import pandas as pd
import os

folder = "/Users/shreyasinha/Desktop/bluestock_mf_capstone/data/raw"

with open(
    "/Users/shreyasinha/Desktop/bluestock_mf_capstone/reports/data_ingestion_output.txt",
    "w"
) as output_file:

    for file in os.listdir(folder):

        if file.endswith(".csv"):

            file_path = os.path.join(folder, file)

            df = pd.read_csv(file_path)

            output_file.write("\n" + "="*50 + "\n")
            output_file.write(f"FILE: {file}\n")

            output_file.write("\nSHAPE:\n")
            output_file.write(str(df.shape) + "\n")

            output_file.write("\nDATA TYPES:\n")
            output_file.write(str(df.dtypes) + "\n")

            output_file.write("\nFIRST 5 ROWS:\n")
            output_file.write(str(df.head()) + "\n")