import pandas as pd
import os 

def run_ingestion():

    print(" Starting ingestion...")

    RAW_PATH = "Data/Raw/"
    OUTPUT_PATH = "Data/cleaned/combined.csv"


    all_files = os.listdir(RAW_PATH)
    dataframes = []

    for file in all_files:
        if file.endswith(".csv"):
            file_path = os.path.join(RAW_PATH,file)
            print(f"Reading file: {file}")

            df = pd.read_csv(file_path)

            df["source_file"] = file

            dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)

    combined_df.to_csv(OUTPUT_PATH,index=False)

    print("Ingestion complete. Combined file created.")

    