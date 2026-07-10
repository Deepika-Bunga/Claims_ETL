Claims ETL Pipeline
 
## Project Overview
This project implements an End-to-End ETL (Extract, Transform, Load) pipeline for processing healthcare claims data using Python and MySQL.
 
The pipeline extracts raw CSV files, performs data cleaning and standardization, loads the data into different ETL layers (Landing, Staging, and Base), applies Slowly Changing Dimension (SCD Type 2) logic, and finally creates a Claims View for reporting and analysis.
 
---
 
## Technology Stack
 
- Python
- MySQL
- Pandas
- SQL
- ETL Concepts
 
---
 
## Project Structure
 
```
Claims_ETL_Project/
│
├── datasets/
│   ├── member.csv
│   ├── provider.csv
│   ├── plan.csv
│   ├── coverage.csv
│   ├── claim.csv
│   └── claimline.csv
│
├── connection.py
├── load_landing.py
├── dataframe.py
├── cleaning.py
├── process_cleaning.py
├── staging_load.py
├── base_load.py
├── claims_database_creation.sql
├── create_claims_view.sql
└── README.md
```
 
---
 
## ETL Workflow
 
1. Load raw CSV files into the Landing Layer.
2. Add Load Key and Ingestion Timestamp.
3. Read Landing data into DataFrames.
4. Perform data cleaning and standardization.
5. Load cleaned data into the Staging Layer.
6. Load data into the Base Layer using SCD Type 2.
7. Generate ETL Audit Logs.
8. Create the Claims View.
 
---
 
## ETL Layers
 
### Landing Layer
- Stores raw source data.
- Maintains original records.
- Adds:
  - Load Key
  - Ingestion Timestamp
 
### Staging Layer
- Cleans and standardizes the data.
- Removes unwanted characters.
- Formats IDs.
- Standardizes phone numbers and email addresses.
 
### Base Layer
- Stores historical data.
- Implements Slowly Changing Dimension (SCD Type 2).
- Generates:
  - Surrogate Key
  - Checksum
  - Current Indicator
  - Start Date
  - End Date
 
---
 
## Features
 
- End-to-End ETL Pipeline
- Data Cleaning
- Data Standardization
- Load Key Generation
- Ingestion Timestamp
- Surrogate Key Generation
- Checksum Validation
- SCD Type 2 Implementation
- ETL Audit Logging
- Claims View Creation
 
---
 
## Database Layers
 
- claims_landing
- claims_stagez
- claims_base
 
---
 
## Execution Order
 
Run the following files in sequence:
 
1. claims_database_creation.sql
2. load_landing.py
3. process_cleaning.py
4. staging_load.py
5. base_load.py
6. create_claims_view.sql
 
---
 
## Output
 
After successful execution:
 
- Landing tables populated
- Staging tables cleaned
- Base tables updated
- ETL Audit Log generated
- Claims View created successfully
 
---
 
## Author
 
**Deepika Bunga**
  