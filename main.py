from scripts.ingest import run_ingestion
from scripts.clean import run_cleaning
from scripts.transform import run_transformation
from scripts.load import run_loading
from reports.generate_reports import run_reporting

print("Starting FULL ETL Pipeline...\n")

run_ingestion()
run_cleaning()
run_transformation()
run_loading()
run_reporting()

print("\nFULL PIPELINE COMPLETED SUCCESSFULLY!")
