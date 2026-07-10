import load_landing

load_landing.main()
import cleaning
import process_cleaning
import staging_load
import base_load
from connection import landing_conn, staging_conn, base_conn
landing_conn.close()
staging_conn.close()
base_conn.close()

print("ETL Completed Successfully")