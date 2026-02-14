# End to End Sales Data ETL & Analytics Pipeline

## Project Overview

This project is a production-style automated ETL pipeline built using Python and MySQL.

It simulates a real world business environment where messy sales data arrives in multiple batches and needs to be:

- Ingested
- Cleaned
- Transformed
- Loaded into a relational database
- Analyzed using SQL
- Reported automatically

The entire pipeline runs with a single command.

---

## Architecture

Raw CSV Files (Messy Data)
        ↓
Ingestion Layer (Python - Pandas)
        ↓
Data Cleaning & Validation
        ↓
Business Transformation
        ↓
MySQL Database
        ↓
Automated SQL Analytics Reports

---

## Tech Stack

- Python
  - Pandas
  - SQLAlchemy
  - PyMySQL
- MySQL
- SQL (Advanced Queries & Window Functions)

---

## Pipeline Workflow

### 1. Data Ingestion
- Dynamically reads multiple CSV files
- Adds source tracking column
- Combines all files into a unified dataset

### 2. Data Cleaning
- Removes duplicate records
- Handles missing values
- Standardizes date formats
- Converts invalid numeric entries
- Filters negative sales values
- Logs cleaning activity

### 3. Data Transformation
Creates business ready analytical features:
- Order Year
- Order Month
- Shipping Days (Delivery performance metric)

Removes unrealistic delivery records.

### 4. Database Loading
- Connects to MySQL using SQLAlchemy
- Loads processed dataset into relational table
- Automatically replaces previous data

### 5. Automated Reporting
Generates analytical reports including:
- Monthly sales trends
- Top customers
- Regional sales performance
- Product performance ranking
- Shipping delay analysis
- Category sales ranking (Window Functions)

All reports are exported automatically as CSV files.

---

## How to Run This Project

1. Clone the repository
2. Install required dependencies:

pip install -r requirements.txt

3. Update MySQL credentials inside:
   - scripts/load.py
   - reports/generate_report.py

4. Run the full pipeline:

python main.py

All reports will be generated inside the reports/ folder.

---

## Project Structure

sales-data-etl-pipeline/
│
├── scripts/
│   ├── ingest.py
│   ├── clean.py
│   ├── transform.py
│   ├── load.py
│
├── reports/
│   └── generate_report.py
│
├── main.py
├── README.md

---

## Example Business Insights Generated

- Monthly revenue trends
- Top spending customers
- Regional performance comparison
- Product level sales ranking
- Average shipping time by region
- Long shipping delay detection
- Category level ranking using SQL window functions

---

## Key Highlights

- Modular ETL pipeline design
- Real world data validation handling
- Python - SQL integration
- Automated analytics generation
- Window functions and advanced SQL usage
- One command pipeline orchestration

---

## Future Improvements

- Add scheduling (Airflow / Cron)
- Integrate interactive dashboard (Power BI / Streamlit)
- Add performance monitoring
- Add automated testing framework
- Cloud deployment (AWS / GCP)

---

## About This Project

This project was built to simulate a real-world data engineering workflow.  
It demonstrates the ability to design scalable data pipelines integrate Python with relational databases, and generate automated business analytics reports.
