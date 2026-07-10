import os
import shutil
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime
 
# ==========================
# DATABASE CONNECTION
# ==========================
 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagannadham@1",
    database="claims_landing"
)
 
cursor = conn.cursor()
 
SOURCE_FOLDER = "source"
ARCHIVE_FOLDER = "archive"
 
 
# ==========================
# GENERATE LOAD KEY
# ==========================
 
def get_next_sequence(cursor):
 
    cursor.execute("""
        SELECT load_key
        FROM audit_log
        ORDER BY audit_id DESC
        LIMIT 1
    """)
 
    result = cursor.fetchone()
 
    if result:
        return int(result[0].split("DP")[-1]) + 1
 
    return 1


def generate_load_key(sequence):
 
    today = datetime.now().strftime("%Y%m%d")
 
    return f"CLK{today}DP{sequence:04d}"
 
 
# ==========================
# INGESTION TIMESTAMP
# ==========================
 
def get_ingestion_timestamp():
    return datetime.now()
 
 
# ==========================
# GET FILES
# ==========================
 
def get_csv_files():
 
    files = [
        f for f in os.listdir(SOURCE_FOLDER)
        if f.endswith(".csv")
    ]
 
    files.sort()
 
    return files
 
 
# ==========================
# AUDIT LOG INSERT
# ==========================
 
def insert_audit_log(
        cursor,
        conn,
        load_key,
        source_file,
        target_table,
        row_count,
        status):
 
    cursor.execute(
        """
        INSERT INTO audit_log
        (
            load_key,
            source_file,
            target_table,
            row_count,
            load_status,
            load_timestamp
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            load_key,
            source_file,
            target_table,
            row_count,
            status,
            datetime.now()
        )
    )
 
    conn.commit()
 
 
# ==========================
# PROCESS FILE
# ==========================
 
def process_file(file_name, load_key,cursor, conn):
 
    file_path = os.path.join(SOURCE_FOLDER, file_name)
 
    try:
 
        print(f"\nProcessing : {file_name}")
 
        file_prefix = file_name.split("_")[0].lower()
 
        table_mapping = {
            "claim": "claim",
            "claimline": "claimline",
            "coverage": "coverage",
            "member": "member",
            "plan": "plan",
            "provider": "provider"
        }
 
        if file_prefix not in table_mapping:
            print(f"Skipping unknown file : {file_name}")
            return
 
        target_table = table_mapping[file_prefix]
 
 
        ingestion_timestamp = get_ingestion_timestamp()
 
        df = pd.read_csv(file_path)
 
        print("\nFILE :", file_name)
        print("Columns :", df.columns.tolist())
        print("Shape :", df.shape)
 
        df["load_key"] = load_key
        df["ingestion_timestamp"] = ingestion_timestamp
        df["is_processed"] = "N"
 
        df = df.replace({np.nan: None})
 
        columns = ",".join(df.columns)
 
        placeholders = ",".join(
            ["%s"] * len(df.columns)
        )
 
        insert_sql = f"""
        INSERT INTO {target_table}
        ({columns})
        VALUES ({placeholders})
        """
 
        data = [
            tuple(row)
            for row in df.itertuples(index=False)
        ]
 
        cursor.executemany(insert_sql, data)
 
        conn.commit()
 
        insert_audit_log(
            cursor,
            conn,
            load_key,
            file_name,
            target_table,
            len(df),
            "SUCCESS"
        )
 
        shutil.move(
            file_path,
            os.path.join(
                ARCHIVE_FOLDER,
                file_name
            )
        )
 
        print(
            f"SUCCESS -> {file_name} | "
            f"Table : {target_table} | "
            f"Rows : {len(df)} | "
            f"Load Key : {load_key}"
        )
 
    except Exception as e:
 
        conn.rollback()
 
        print(f"FAILED -> {file_name}")
        print(f"ERROR : {e}")
 
        try:
 
            insert_audit_log(
                cursor,
                conn,
                load_key if 'load_key' in locals() else None,
                file_name,
                target_table if 'target_table' in locals() else None,
                0,
                "FAILED"
            )
 
        except:
            conn.rollback()
 
 
# ==========================
# MAIN
# ==========================
 
def main():
 
    print("Starting Landing Load Process...")
 
    while True:
 
        files = get_csv_files()
 
        if len(files) == 0:
 
            print("Loading completed successfully.")
            
            print("\nSource folder is empty.")
            break

        next_sequence = get_next_sequence(cursor)
 
        for file_name in files:
            load_key = generate_load_key(next_sequence)
 
            process_file(
                file_name,
                load_key,
                cursor,
                conn
            )
            next_sequence += 1
 
    #cursor.close()
    #conn.close() 
 
 
# ==========================
# DRIVER
# ==========================
 
if __name__ == "__main__":
    main()
 