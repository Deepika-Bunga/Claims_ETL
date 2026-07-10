Show databases;
Use claims_landing;

Show tables;
Use claims_landing;
Select * from audit_log;
Select * from claim;
Select * from claimline;
select * from coverage;
select * from member;
select * from plan;
select * from provider;

use claims_stagez;
show tables;

select * from stg_claim;
select * from stg_claimline;
select * from stg_coverage;
select * from stg_member;
select * from stg_plan;
select * from stg_provider;

use claims_base;
show tables;

select * from claim;
select * from claimline;
select * from coverage;
select * from member; 
select * from plan;
select * from provider;
select * from etl_audit_log;

use claims_base;
select * from claims_view;
select * from etl_audit_log;
Select * from claims_view where ClaimID='0000P539'; 
show databases;