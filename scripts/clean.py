import pandas as pd
import logging

def run_cleaning():


    print("Cleaning pipeline started...")

    INPUT_PATH = "data/cleaned/combined.csv"
    OUTPUT_PATH = "data/cleaned/cleaned.csv"


    logging.basicConfig(
        filename="logs/cleaning.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


    df = pd.read_csv(INPUT_PATH)
    print("File loaded")

        
    df.columns = df.columns.str.strip()

        
    before = len(df)
    df.drop_duplicates(inplace=True)
    after = len(df)

    print(f"Removed {before - after} duplicates")
    logging.info(f"Removed {before - after} duplicate rows")

    
    df.fillna("Unknown", inplace=True)
    print("Missing values handled")

    
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
    print("Dates standardized")

    
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    
    df = df[df["Sales"] >= 0]
    print("Invalid sales removed")

        
    df.to_csv(OUTPUT_PATH, index=False)

    print("Cleaning completed successfully!")



