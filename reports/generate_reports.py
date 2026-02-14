import pandas as pd
from sqlalchemy import create_engine
import os

def run_reporting():


    print("Starting report automation...")

    engine = create_engine(
        "mysql+pymysql://root:5147@localhost/sales_pipeline"
    )


    os.makedirs("reports", exist_ok=True)


    queries = {

        "monthly_sales": """
            SELECT
                `Order Year`,
                `Order Month`,
                SUM(Sales) AS total_sales
            FROM sales_data
            GROUP BY `Order Year`, `Order Month`
            ORDER BY `Order Year`, `Order Month`;
        """,

        "top_customers": """
            SELECT
                `Customer Name`,
                SUM(Sales) AS total_spent
            FROM sales_data
            GROUP BY `Customer Name`
            ORDER BY total_spent DESC
            LIMIT 5;
        """,

        "sales_by_region": """
            SELECT
                Region,
                SUM(Sales) AS regional_sales
            FROM sales_data
            GROUP BY Region;
        """,

        "top_products": """
            SELECT
                `Product Name`,
                SUM(Sales) AS total_sales
            FROM sales_data
            GROUP BY `Product Name`
            ORDER BY total_sales DESC
            LIMIT 10;
        """,

        "yearly_sales": """
            SELECT
                `Order Year`,
                SUM(Sales) AS yearly_sales
            FROM sales_data
            GROUP BY `Order Year`
            ORDER BY `Order Year`;
        """,

        "avg_shipping_by_region": """
            SELECT
                Region,
                AVG(`Shipping Days`) AS avg_shipping_days
            FROM sales_data
            GROUP BY Region;
        """,

        "sales_by_segment": """
            SELECT
                Segment,
                SUM(Sales) AS segment_sales
            FROM sales_data
            GROUP BY Segment;
        """,

        "top_cities": """
            SELECT
                City,
                SUM(Sales) AS city_sales
            FROM sales_data
            GROUP BY City
            ORDER BY city_sales DESC
            LIMIT 5;
        """,

        "shipping_delays": """
            SELECT
                `Order ID`,
                `Customer Name`,
                `Shipping Days`
            FROM sales_data
            WHERE `Shipping Days` > 7
            ORDER BY `Shipping Days` DESC;
        """,

        "category_ranking": """
            SELECT
                Category,
                SUM(Sales) AS total_sales,
                RANK() OVER (ORDER BY SUM(Sales) DESC) AS sales_rank
            FROM sales_data
            GROUP BY Category;
        """

    }


    for report_name, query in queries.items():

        print(f"Generating {report_name}...")

        df = pd.read_sql(query, engine)

        file_path = f"reports/{report_name}.csv"
        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    print(" All reports generated successfully!")
