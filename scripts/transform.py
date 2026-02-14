import pandas as pd

def run_transformation():


    print("Transformation started...")

    INPUT_PATH = "data/cleaned/cleaned.csv"
    OUTPUT_PATH = "data/cleaned/transformed.csv"

    df = pd.read_csv(INPUT_PATH)

    print("Cleaned file loaded")


    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])



    df["Order Year"] = df["Order Date"].dt.year


    df["Order Month"] = df["Order Date"].dt.month


    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    print("Business features created")


    df = df[df["Shipping Days"] >= 0]


    df.to_csv(OUTPUT_PATH, index=False)

    print("Transformation completed!")
