from connection import staging_conn, base_conn
from datetime import date
 
stg_cursor = staging_conn.cursor()
base_cursor = base_conn.cursor()
 
table_mapping = {
    "stg_member": ("member", "member_id"),
    "stg_provider": ("provider", "provider_id"),
    "stg_plan": ("plan", "plan_id"),
    "stg_coverage": ("coverage", "coverage_id"),
    "stg_claim": ("claim", "ClaimID"),
    "stg_claimline": ("claimline", "Claim_Line_ID")
}
 
today = date.today()
future_date = "9999-12-30"
 
for stg_table, (base_table, business_key) in table_mapping.items():
    insert_count = 0
    update_count = 0
    drop_count = 0        
 
    stg_cursor.execute(f"SELECT * FROM {stg_table}")
    rows = stg_cursor.fetchall()
 
    # get column names
    stg_cursor.execute(f"SHOW COLUMNS FROM {stg_table}")
    cols = [c[0] for c in stg_cursor.fetchall()]
 
    key_index = cols.index(business_key)
    checksum_index = cols.index("checksum")
 
    for row in rows:
 
        business_value = row[key_index]
        stage_checksum = row[checksum_index]
 
        check_sql = f"""
        SELECT checksum
        FROM {base_table}
        WHERE {business_key}=%s
        AND curr_ind='Y'
        """
 
        base_cursor.execute(check_sql, (business_value,))
        existing = base_cursor.fetchone()
 
        # New record
        if existing is None:
 
            new_row = list(row)
            new_row.extend(['Y', today, future_date])
 
            placeholders = ",".join(["%s"] * len(new_row))
 
            insert_sql = f"""
            INSERT INTO {base_table}
            VALUES ({placeholders})
            """
 
            base_cursor.execute(insert_sql, tuple(new_row))

            insert_count += 1
 
        # Same record already exists
        elif existing[0] == stage_checksum:
            drop_count += 1
            continue
 
       
        else:
 
            update_sql = f"""
            UPDATE {base_table}
            SET curr_ind='N',
                end_date=%s
            WHERE {business_key}=%s
            AND curr_ind='Y'
            """
 
            base_cursor.execute(
                update_sql,
                (today, business_value)
            )
 
            new_row = list(row)
            new_row.extend(['Y', today, future_date])
 
            placeholders = ",".join(["%s"] * len(new_row))
 
            insert_sql = f"""
            INSERT INTO {base_table}
            VALUES ({placeholders})
            """
 
            base_cursor.execute(insert_sql, tuple(new_row))
            update_count += 1
    audit_sql = """INSERT INTO etl_audit_log 
(table_name, load_date, inserted_records, updated_records, dropped_records) 
VALUES (%s, NOW(), %s, %s, %s)"""

    base_cursor.execute(
    audit_sql,
    (base_table, insert_count, update_count, drop_count)
)
    print(f"{base_table} processed")
    base_conn.commit()
 
print("Base Layer SCD2 Load Completed")
# =====================================
# TRUNCATE STAGING TABLES
# =====================================
 
stage_tables = [
    "stg_member",
    "stg_provider",
    "stg_plan",
    "stg_coverage",
    "stg_claim",
    "stg_claimline"
]
 
for table in stage_tables:
    stg_cursor.execute(f"TRUNCATE TABLE {table}")
    print(f"{table} truncated")
 
staging_conn.commit()
 
print("Stage Layer Truncated Successfully")
 
stg_cursor.close()
base_cursor.close()

staging_conn.close()
base_conn.close() 