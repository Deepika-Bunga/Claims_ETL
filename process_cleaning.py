from connection import landing_conn
import uuid

 
from cleaning import (
    add_surrogate_and_checksum,
    clean_boolean,
    generate_checksum,
    trim_spaces,
    standardize_id,
    clean_phone,
    clean_email,
    standardize_date,
)
 
cursor = landing_conn.cursor()
 
cleaned_data = {}
 
# =====================================
# MEMBER
# ===================================== 
cursor.execute("""SELECT * FROM member WHERE is_processed = 'N'""")
 
rows = cursor.fetchall()
 
member_cleaned = []
 
for row in rows:
 
    row = list(row)

    row.pop() # Remove the last element (is_processed) from the row
 
    row[0] = standardize_id(row[0])     # member_id
 
    row[1] = trim_spaces(row[1])        # first_name
 
    row[2] = trim_spaces(row[2])        # last_name

    row[3] = standardize_date(row[3])     # date_of_birth
 
    row[5] = clean_phone(row[5])        # phone
 
    row[6] = clean_email(row[6])        # email
 
    row[12]=standardize_date(row[12])     # join_date

    row[14] = standardize_id(row[14])   # coverage_id

    row = add_surrogate_and_checksum(
    row,
    "member",
    [
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11],
        row[12],
        row[13],
        row[14]
    ]
)
 
 
    member_cleaned.append(tuple(row))
 
cleaned_data["member"] = member_cleaned
 
print("Member Records:", len(member_cleaned))
 
 
# =====================================
# CLAIM
# =====================================
 
cursor.execute("""SELECT * FROM claim WHERE is_processed = 'N'""")
 
rows = cursor.fetchall()
 
claim_cleaned = []
 
for row in rows:
 
    row = list(row)
    row.pop() # Remove the last element (is_processed) from the row
 
    row[0] = standardize_id(row[0])     # ClaimID
 
    row[1] = standardize_id(row[1])     # MemberID
 
    row[2] = standardize_id(row[2])     # CoverageID

    row[3] = standardize_date(row[3])     # ClaimDate

    row[7] = standardize_date(row[7])     # ServiceStartDate

    row[8] = standardize_date(row[8])     # ServiceEndDate

    row = add_surrogate_and_checksum(
    row,
    "claim",
    [
        row[1],  # MemberID
        row[2],  # CoverageID
        row[3],  # ClaimDate
        row[4],  # ClaimAmount
        row[5],  # ClaimType
        row[6],  # ClaimStatus
        row[7],  # ServiceStartDate
        row[8]   # ServiceEndDate
    ]
) 
 
 
    claim_cleaned.append(tuple(row))
 
cleaned_data["claim"] = claim_cleaned
 
print("Claim Records:", len(claim_cleaned))
 
 
# =====================================
# CLAIMLINE
# =====================================
 
cursor.execute("""SELECT * FROM claimline WHERE is_processed = 'N'""")
 
rows = cursor.fetchall()
 
claimline_cleaned = []
 
for row in rows:
 
    row = list(row)
    row.pop()  # Remove the last element (is_processed) from the row
    row[0] = standardize_id(row[0])     # Claim_Line_ID
 
    row[1] = standardize_id(row[1])     # ClaimID

    row = add_surrogate_and_checksum(
    row,
    "claim_line",
    [
        row[1],  # ClaimID
        row[2],  # Procedure_Code
        row[3],  # Diagnosis_Code
        row[4],  # Units
        row[5],  # Charge_Amount
        row[6]   # Allowed_Amount
    ]
)
 
 
    claimline_cleaned.append(tuple(row))
 
cleaned_data["claimline"] = claimline_cleaned
 
print("ClaimLine Records:", len(claimline_cleaned))
 
 
# =====================================
# COVERAGE
# =====================================
 
cursor.execute("""SELECT * FROM coverage WHERE is_processed = 'N'""")
 
rows = cursor.fetchall()
 
coverage_cleaned = []
 
for row in rows:
 
    row = list(row)
    row.pop()  # Remove the last element (is_processed) from the row
    row[0] = standardize_id(row[0])     # coverage_id
 
    row[2] = standardize_id(row[2])     # provider_id

    row[3] = standardize_date(row[3])     #coverage_start_date

    row[4] = standardize_date(row[4])     #coverage_end_date
  
    row[6] = standardize_id(row[6])     # plan_id


    row = add_surrogate_and_checksum(
    row,
    "coverage",
    [
        row[1],
        row[2],
        row[3],
        row[4],
        row[5]
    ]
)
 
    coverage_cleaned.append(tuple(row))
 
cleaned_data["coverage"] = coverage_cleaned
 
print("Coverage Records:", len(coverage_cleaned))
 
 
# =====================================
# PLAN
# =====================================
 
cursor.execute("""SELECT * FROM plan WHERE is_processed = 'N'""")
 
rows = cursor.fetchall()
 
plan_cleaned = []
 
for row in rows:
 
    row = list(row)
    row.pop()  # Remove the last element (is_processed) from the row
    row[0] = standardize_id(row[0])     # plan_id

    row[3] = clean_boolean(row[3])        # InpatientCoverage

    row[4] = clean_boolean(row[4])        # OutpatientCoverage

    row[5] = clean_boolean(row[5])        # EmergencyCoverage

    row[6] = clean_boolean(row[6])        # PrescriptionCoverage

    row[7] = clean_boolean(row[7])        #MentalHealthCoverage

    row[8] = clean_boolean(row[8])        # VisionCoverage

    row[9] = clean_boolean(row[9])        # DentalCoverage

    # Surrogate Key and checksum generation
    row = add_surrogate_and_checksum(row, "plan", [
        row[1],  # planname
        row[2],  # maxcoverage
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9]
    ])

    plan_cleaned.append(tuple(row))
 
cleaned_data["plan"] = plan_cleaned

print("Plan Records:", len(plan_cleaned))
 
 
# =====================================
# PROVIDER
# =====================================
cursor.execute("""SELECT * FROM provider WHERE is_processed = 'N'""")
 
rows = cursor.fetchall()
 
provider_cleaned = []
 
for row in rows:
 
    row = list(row)

    row.pop()  # Remove the last element (is_processed) from the row
 
    row[0] = standardize_id(row[0])     # provider_id

    row[3] = standardize_date(row[3])        #date_of_birth
 
    row[9] = clean_phone(row[9])     # telephone no.

    row[10]=clean_boolean(row[10])    

    row = add_surrogate_and_checksum(
    row,
    "provider",
    [
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11],
        row[12],
        row[13]
    ]
)
  
    provider_cleaned.append(tuple(row))
 
cleaned_data["provider"] = provider_cleaned
 
print("Provider Records:", len(provider_cleaned))
 
 
# =====================================
# RESULT
# =====================================
 
print("\nCleaning Completed Successfully")
 
 
print(cleaned_data.keys())

cleaned_data = {
    "member": member_cleaned,
    "claim": claim_cleaned,
    "claimline": claimline_cleaned,
    "coverage": coverage_cleaned,
    "plan": plan_cleaned,
    "provider": provider_cleaned
}
 
cursor.close()