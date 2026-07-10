from connection import staging_conn, landing_conn
from datetime import datetime
from process_cleaning import cleaned_data
 
landing_cursor = landing_conn.cursor()
cursor = staging_conn.cursor()
 
table_mapping = {
    "member": "stg_member",
    "claim": "stg_claim",
    "claimline": "stg_claimline",
    "coverage": "stg_coverage",
    "plan": "stg_plan",
    "provider": "stg_provider"
}
 
for source_table, rows in cleaned_data.items():
 
    if not rows:
        continue
 
    target_table = table_mapping[source_table]
 
    placeholders = ",".join(["%s"] * len(rows[0]))
 
    insert_sql = f"""
    INSERT INTO {target_table}
    VALUES ({placeholders})
    """
 
    cursor.executemany(insert_sql, rows)
 
    print(f"{cursor.rowcount} rows loaded into {target_table}")

    for source_table, rows in cleaned_data.items():
        landing_cursor.execute(f"""
    UPDATE {source_table}
    SET is_processed='Y'
    WHERE is_processed='N'
""")
 
landing_conn.commit()
 
 
landing_conn.commit()
 
 
staging_conn.commit()
 
#cursor.close()
#staging_conn.close()
 
print("\nStage Layer Load Completed Successfully")