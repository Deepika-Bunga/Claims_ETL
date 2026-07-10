USE claims_landing;
 
CREATE TABLE claim (
    ClaimID VARCHAR(20),
    MemberID VARCHAR(20),
    CoverageID VARCHAR(20),
    ClaimDate DATE,
    ClaimAmount DECIMAL(12,2),
    ClaimType VARCHAR(50),
    ClaimStatus VARCHAR(50),
    ServiceStartDate DATE,
    ServiceEndDate DATE,
    ingest_timestamp TIMESTAMP NULL,
    load_key VARCHAR(50)
    is_processed VARCHAR(1) DEFAULT 'N'
);

CREATE TABLE claimline (
    Claim_Line_ID VARCHAR(20),
    ClaimID VARCHAR(20),
    Procedure_Code VARCHAR(20),
    Diagnosis_Code VARCHAR(20),
    Units INT,
    Charge_Amount DECIMAL(12,2),
    Allowed_Amount DECIMAL(12,2),
    ingest_timestamp TIMESTAMP NULL,
    load_key VARCHAR(50),
    is_processed VARCHAR(1) DEFAULT 'N'
);
CREATE TABLE coverage (
    coverage_id VARCHAR(20),
    coverage_name VARCHAR(100),
    provider_id VARCHAR(20),
    coverage_start_date DATE,
    coverage_end_date DATE,
    status VARCHAR(20),
    plan_id VARCHAR(20),
    yearly_premium DECIMAL(12,2),
    deductible_amount DECIMAL(12,2),
    co_pay_percentage INT,
    ingest_timestamp TIMESTAMP NULL,
    load_key VARCHAR(50),
    is_processed VARCHAR(1) DEFAULT 'N'
);
CREATE TABLE member (
    MemberID VARCHAR(20),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    DOB DATE,
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(20),
    ingest_timestamp TIMESTAMP NULL,
    load_key VARCHAR(50),
    is_processed VARCHAR(1) DEFAULT 'N'
);

CREATE TABLE provider (
    ProviderID VARCHAR(20),
    ProviderName VARCHAR(100),
    Specialty VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(20),
    ingest_timestamp TIMESTAMP NULL,
    load_key VARCHAR(50),
    is_processed VARCHAR(1) DEFAULT 'N'
);

CREATE TABLE plan (
    plan_id VARCHAR(20),
    plan_name VARCHAR(100),
    plan_type VARCHAR(50),
    coverage_level VARCHAR(50),
    network_type VARCHAR(50),
    monthly_premium DECIMAL(12,2),
    deductible DECIMAL(12,2),
    out_of_pocket_max DECIMAL(12,2),
    ingest_timestamp TIMESTAMP NULL,
    load_key VARCHAR(50),
    is_processed VARCHAR(1) DEFAULT 'N'
);

CREATE TABLE audit_log (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    load_key VARCHAR(50) NOT NULL,
    source_file VARCHAR(255) NOT NULL,
    target_table VARCHAR(100) NOT NULL,
    row_count INT NOT NULL,
    load_status VARCHAR(20) NOT NULL,
    load_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

 