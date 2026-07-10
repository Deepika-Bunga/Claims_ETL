CREATE OR REPLACE VIEW claims_view AS
Select 
c.ClaimID,
c.ClaimDate,
c.ClaimAmount,
c.ClaimType,
c.ClaimStatus,
c.ServiceStartDate,
c.ServiceEndDate,

m.member_id,
m.first_name,
m.last_name,
m.date_of_birth,
m.gender,
m.phone,
m.email,
m.street,
m.city,
m.state,
m.country,

cv.coverage_id,
cv.coverage_name,
cv.coverage_start_date,
cv.coverage_end_date,
cv.status AS coverage_status,
cv.yearly_premium,
cv.deductible_amount,
cv.co_pay_percentage,

p.plan_id,
p.planname,
p.MaxCoverageAmount,
p.InpatientCoverage,
p.OutPatientCoverage,
p.EmergencyServices,
p.PrescriptionDrug,
p.MentalHealthCoverage,
p.VisionCoverage,
p.DentalCoverage,

pr.provider_id,
pr.provider_name,
pr.speciality_id,
pr.telephone_number,
pr.city AS provider_city,
pr.state AS provider_state,
pr.overall_rating

FROM claim c 
Join member m ON c.MemberID = m.member_id AND m.curr_ind ='Y'
Join coverage cv ON c.CoverageID =cv.coverage_id AND cv.curr_ind='Y'
Join plan p ON cv.plan_id = p.plan_id AND p.curr_ind='Y'
Join provider pr ON cv.provider_id = pr.provider_id AND pr.curr_ind='Y'
Where c.curr_ind = 'Y'; 