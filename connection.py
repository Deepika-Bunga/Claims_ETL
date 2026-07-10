import mysql.connector
 
# Landing DB
landing_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagannadham@1",
    database="claims_landing"
)
 
# Staging DB
staging_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagannadham@1",
    database="claims_stagez"
)

base_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagannadham@1",
    database="claims_base"
)
 
 
# Backward compatibility for old code
conn = landing_conn
cursor = conn.cursor()
 