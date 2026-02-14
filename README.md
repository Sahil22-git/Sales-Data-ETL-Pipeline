END TO END SALES DATA ETL & ANALYTICS PIPELINE
PROJECT OVERVIEW

This project is an end to end automated ETL pipeline built using Python and MySQL.
It ingests messy sales data from multiple CSV files cleans and transforms the data loads it into a relational database and automatically generates analytical reports.

The pipeline simulates a real world business environment where data arrives in batches and requires validation, transformation and reporting.



ARCHITECTURE

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



TECH STACK

Python

Pandas

SQLAlchemy

PyMySQL

MySQL

SQL (Advanced Queries & Window Functions)


PIPELINE WORKFLOW

1️. Data Ingestion

Dynamically reads multiple CSV files

Adds source tracking column

Combines all files into a unified dataset


2️. Data Cleaning

Removes duplicate records

Handles missing values

Standardizes date formats

Converts invalid numeric entries

Filters negative sales values

Logs cleaning activity


3️. Data Transformation

Creates business-ready analytical features:

Order Year

Order Month

Shipping Days (Delivery performance metric)

Removes unrealistic delivery records.


4️. Database Loading

Connects to MySQL using SQLAlchemy

Loads processed dataset into relational table

Automatically replaces previous data


5️. Automated Reporting

Generates analytical reports including:

Monthly sales trends

Top customers

Regional sales performance

Product performance ranking

Shipping delay analysis

Category sales ranking (Window Functions)

All reports are exported automatically as CSV files.



HOW TO RUN THIS PROJECT

Clone the repository

Install required dependencies:

pip install -r requirements.txt


Update MySQL credentials inside:

scripts/load.py

reports/generate_report.py

Run the full pipeline:

python main.py

All reports will be generated inside the reports/ folder.


PROJECT STRUCTURE

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




EXAMPLE BUSINESS INSIGHTS GENERATED

Monthly revenue trends

Top spending customers

Regional performance comparison

Product-level sales ranking

Average shipping time by region

Long shipping delay detection

Category-level ranking using SQL window functions



KEY HIGHLIGHTS

Modular ETL pipeline design

Real world data validation handling

Python SQL integration

Automated analytics generation

Window functions and advanced SQL usage

One command pipeline orchestration



FUTURE IMPROVEMENTS

Add scheduling (Airflow / Cron)

Integrate interactive dashboard (Power BI / Streamlit)

Add performance monitoring

Add automated testing framework

Cloud deployment (AWS / GCP)



ABOUT THIS PROJECT

This project was built to simulate a real world data engineering workflow.
It demonstrates the ability to design scalable data pipelines, integrate Python with relational databases and generate automated business analytics reports.


