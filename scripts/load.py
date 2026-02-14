import pandas as pd
from sqlalchemy import create_engine

def run_loading():


    print("Loading data into MySQL...")


    DB_USER = "root"
    DB_PASSWORD = "5147"
    DB_HOST = "localhost"
    DB_NAME = "sales_pipeline"

    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    INPUT_PATH = "data/cleaned/transformed.csv"

    df = pd.read_csv(INPUT_PATH)

    print("Transformed file loaded")

    df.to_sql("sales_data", engine, if_exists="replace", index=False)

    print("Data successfully loaded into MySQL!")
