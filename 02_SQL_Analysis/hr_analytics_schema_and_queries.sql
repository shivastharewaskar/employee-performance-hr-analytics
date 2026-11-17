-- =====================================================================
-- PROJECT 1: EMPLOYEE PERFORMANCE & HR ANALYTICS
-- Database Management System: MySQL / MariaDB (Compatible with SQLite / PostgreSQL)
-- Description: End-to-End SQL Schema, Data Ingestion, and 10 Core Analytical Tasks
-- =====================================================================

-- Step 1: Database Initialization
CREATE DATABASE IF NOT EXISTS HR_Analytics_DB;
USE HR_Analytics_DB;

-- Step 2: Table Creation (DDL with Constraints)
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    EmployeeID VARCHAR(10) PRIMARY KEY,
    Age INT NOT NULL CHECK (Age >= 18 AND Age <= 70),
    Gender VARCHAR(10) NOT NULL CHECK (Gender IN ('Male', 'Female', 'Other')),
    Department VARCHAR(50) NOT NULL,
    JobRole VARCHAR(50) NOT NULL,
    Education VARCHAR(50) NOT NULL,
    YearsOfExperience INT NOT NULL CHECK (YearsOfExperience >= 0),
    YearsAtCompany INT NOT NULL CHECK (YearsAtCompany >= 0),
    Salary DECIMAL(12, 2) NOT NULL CHECK (Salary > 0),
    WorkMode VARCHAR(20) NOT NULL CHECK (WorkMode IN ('Remote', 'Hybrid', 'Office')),
    PerformanceRating INT NOT NULL CHECK (PerformanceRating BETWEEN 1 AND 4),
    JobSatisfaction INT NOT NULL CHECK (JobSatisfaction BETWEEN 1 AND 4),
    WorkLifeBalance INT NOT NULL CHECK (WorkLifeBalance BETWEEN 1 AND 4),
    Attrition VARCHAR(5) NOT NULL CHECK (Attrition IN ('Yes', 'No'))
);

-- Note: Data can be populated directly via MySQL Workbench Import Wizard
-- or LOAD DATA LOCAL INFILE 'employee_data_cleaned.csv' INTO TABLE Employees...

-- Step 3: Performance Optimization (Indexes)
CREATE INDEX idx_emp_dept ON Employees(Department);
CREATE INDEX idx_emp_salary ON Employees(Salary);
CREATE INDEX idx_emp_workmode ON Employees(WorkMode);
CREATE INDEX idx_emp_attrition ON Employees(Attrition);

-- =====================================================================
-- SQL TASKS (10 CORE PROBLEM STATEMENTS)
-- =====================================================================

-- ---------------------------------------------------------------------
-- Task 1: Retrieve the total number of employees in each department.
-- Business Context: Essential for workforce capacity planning and resource allocation.
-- ---------------------------------------------------------------------
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees), 2) AS WorkforcePercentage
FROM Employees
GROUP BY Department
ORDER BY TotalEmployees DESC;

-- ---------------------------------------------------------------------
-- Task 2: Find the average salary department-wise.
-- Business Context: Establishes baseline compensation cost per business division.
-- ---------------------------------------------------------------------
SELECT 
    Department, 
    ROUND(AVG(Salary), 2) AS AverageSalary,
    ROUND(MIN(Salary), 2) AS MinSalary,
    ROUND(MAX(Salary), 2) AS MaxSalary
FROM Employees
GROUP BY Department
ORDER BY AverageSalary DESC;

-- ---------------------------------------------------------------------
-- Task 3: Identify the top 10 highest-paid employees.
-- Business Context: Identifies top executive and specialized talent investments.
-- ---------------------------------------------------------------------
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    Education, 
    YearsOfExperience, 
    Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 10;

-- ---------------------------------------------------------------------
-- Task 4: Calculate the average years of experience by department.
-- Business Context: Measures talent seniority and institutional knowledge density.
-- ---------------------------------------------------------------------
SELECT 
    Department, 
    ROUND(AVG(YearsOfExperience), 2) AS AvgExperienceYears,
    ROUND(AVG(YearsAtCompany), 2) AS AvgTenureAtCompany
FROM Employees
GROUP BY Department
ORDER BY AvgExperienceYears DESC;

-- ---------------------------------------------------------------------
-- Task 5: Find employees with the highest performance rating.
-- Business Context: Talent review pool for annual promotion and merit awards.
-- ---------------------------------------------------------------------
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    PerformanceRating, 
    Salary, 
    WorkMode
FROM Employees
WHERE PerformanceRating = (SELECT MAX(PerformanceRating) FROM Employees)
ORDER BY Salary DESC;

-- ---------------------------------------------------------------------
-- Task 6: Count employees based on work mode (Remote, Hybrid, Office).
-- Business Context: Determines infrastructure needs and remote policy adoption.
-- ---------------------------------------------------------------------
SELECT 
    WorkMode, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees), 2) AS AdoptionPercentage
FROM Employees
GROUP BY WorkMode
ORDER BY EmployeeCount DESC;

-- ---------------------------------------------------------------------
-- Task 7: Identify departments with the highest employee attrition.
-- Business Context: Pinpoints organizational friction and high-turnover centers.
-- ---------------------------------------------------------------------
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS AttritionExits,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS AttritionRatePercent
FROM Employees
GROUP BY Department
ORDER BY AttritionRatePercent DESC;

-- ---------------------------------------------------------------------
-- Task 8: Rank employees based on salary within each department.
-- Business Context: Advanced window function used for internal equity comparisons.
-- ---------------------------------------------------------------------
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    Salary, 
    DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS SalaryRankInDept
FROM Employees
ORDER BY Department, SalaryRankInDept;

-- ---------------------------------------------------------------------
-- Task 9: Find employees earning above the company average salary.
-- Business Context: Subquery analysis identifying premium compensation earners.
-- ---------------------------------------------------------------------
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    Salary,
    ROUND(Salary - (SELECT AVG(Salary) FROM Employees), 2) AS SalaryAboveAverage
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees)
ORDER BY Salary DESC;

-- ---------------------------------------------------------------------
-- Task 10: Calculate gender-wise employee distribution.
-- Business Context: Monitors corporate Diversity, Equity, and Inclusion (DEI) metrics.
-- ---------------------------------------------------------------------
SELECT 
    Gender, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees), 2) AS DistributionPercentage,
    ROUND(AVG(Salary), 2) AS AvgSalaryByGender
FROM Employees
GROUP BY Gender
ORDER BY EmployeeCount DESC;

-- =====================================================================
-- BONUS ADVANCED SQL: VIEWS AND STORED PROCEDURES
-- =====================================================================

-- Analytical View for Power BI Direct Query Connection
CREATE OR REPLACE VIEW vw_HR_Department_KPIs AS
SELECT 
    Department,
    COUNT(*) AS TotalHeadcount,
    ROUND(AVG(Salary), 2) AS DeptAvgSalary,
    ROUND(AVG(YearsOfExperience), 2) AS DeptAvgExperience,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS DeptAttritionRate,
    ROUND(AVG(PerformanceRating), 2) AS DeptAvgPerformance
FROM Employees
GROUP BY Department;

-- Stored Procedure: Departmental Talent Filter
DELIMITER //
CREATE PROCEDURE sp_GetDepartmentTalent(IN targetDept VARCHAR(50))
BEGIN
    SELECT 
        EmployeeID, JobRole, Education, YearsOfExperience, Salary, WorkMode, PerformanceRating, Attrition
    FROM Employees
    WHERE Department = targetDept
    ORDER BY PerformanceRating DESC, Salary DESC;
END //
DELIMITER ;
