CREATE TABLE claim (
    ClaimID VARCHAR(8),
    MemberID VARCHAR(8),
    CoverageID VARCHAR(8),
    ClaimDate DATE,
    ClaimAmount DECIMAL(12,2),
    ClaimType VARCHAR(50),
    ClaimStatus VARCHAR(50),
    ServiceStartDate DATE,
    ServiceEndDate DATE,
    load_key VARCHAR(50),
    ingestion_timestamp DATETIME,
    claim_key CHAR(36),
    checksum CHAR(32),
    curr_ind CHAR(1),
    start_date DATE,
    end_date DATE
);
 
CREATE TABLE member (
    member_id VARCHAR(8),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(100),
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    join_date DATE,
    status VARCHAR(20),
    coverage_id VARCHAR(8),
    load_key VARCHAR(50),
    ingestion_timestamp DATETIME,
    member_key CHAR(36),
    checksum CHAR(32),
    curr_ind CHAR(1),
    start_date DATE,
    end_date DATE
);
 
CREATE TABLE provider (
    provider_id VARCHAR(8),
    provider_name VARCHAR(100),
    Gender VARCHAR(10),
    Birth_date DATE,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(20),
    country VARCHAR(100),
    telephone_number VARCHAR(20),
    specialty_id VARCHAR(50),
    emergency_services VARCHAR(10),
    overall_rating DECIMAL(3,2),
    rating_footnote VARCHAR(255),
    load_key VARCHAR(50),
    ingestion_timestamp DATETIME,
    provider_key CHAR(36),
    checksum CHAR(32),
    curr_ind CHAR(1),
    start_date DATE,
    end_date DATE
);
 
CREATE TABLE plan (
    plan_id VARCHAR(8),
    planname VARCHAR(100),
    MaxCoverageAmount DECIMAL(12,2),
    InpatientCoverage VARCHAR(10),
    OutPatientCoverage VARCHAR(10),
    EmergencyServices VARCHAR(10),
    PrescriptionDrug VARCHAR(10),
    MentalHealthCoverage VARCHAR(10),
    VisionCoverage VARCHAR(10),
    DentalCoverage VARCHAR(10),
    load_key VARCHAR(50),
    ingestion_timestamp DATETIME,
    plan_key CHAR(36),
    checksum CHAR(32),
    curr_ind CHAR(1),
    start_date DATE,
    end_date DATE
);
 
 
CREATE TABLE coverage (
    coverage_id VARCHAR(8),
    coverage_name VARCHAR(100),
    provider_id VARCHAR(8),
    coverage_start_date DATE,
    coverage_end_date DATE,
    status VARCHAR(20),
    plan_id VARCHAR(8),
    yearly_premium DECIMAL(10,2),
    deductible_amount DECIMAL(10,2),
    co_pay_percentage DECIMAL(5,2),
    load_key VARCHAR(50),
    ingestion_timestamp DATETIME,
    coverage_key CHAR(36),
    checksum CHAR(32),
    curr_ind CHAR(1),
    start_date DATE,
    end_date DATE
);
 
CREATE TABLE claimline (
    Claim_Line_ID VARCHAR(8),
    ClaimID VARCHAR(8),
    Procedure_Code VARCHAR(50),
    Diagnosis_Code VARCHAR(50),
    Units INT,
    Charge_Amount DECIMAL(12,2),
    Allowed_Amount DECIMAL(12,2),
    load_key VARCHAR(50),
    ingestion_timestamp DATETIME,
    claimline_key CHAR(36),
    checksum CHAR(32),
    curr_ind CHAR(1),
    start_date DATE,
    end_date DATE
);
 