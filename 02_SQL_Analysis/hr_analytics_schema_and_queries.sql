/* 
 * =====================================================================
 * Student Name: Shivastha Rewaskar
 * Project: Employee Performance & HR Analytics
 * GitHub Repository: https://github.com/shivastharewaskar/employee-performance-hr-analytics
 * Database Engine: MySQL 8.0+
 * Description: Relational Schema DDL, Data Ingestion, and 10 SQL Tasks
 * =====================================================================
 */

-- 1. Database Creation
CREATE DATABASE IF NOT EXISTS HR_Analytics_DB;
USE HR_Analytics_DB;

-- 2. Drop table if it already exists to allow re-running script cleanly
DROP TABLE IF EXISTS employees;

-- 3. Table Schema with proper datatypes and constraints
CREATE TABLE employees (
    EmployeeID VARCHAR(10) PRIMARY KEY,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    JobRole VARCHAR(50) NOT NULL,
    Education VARCHAR(50) NOT NULL,
    YearsOfExperience INT NOT NULL,
    YearsAtCompany INT NOT NULL,
    Salary DECIMAL(12, 2) NOT NULL,
    WorkMode VARCHAR(20) NOT NULL,
    PerformanceRating INT NOT NULL,
    JobSatisfaction INT NOT NULL,
    WorkLifeBalance INT NOT NULL,
    Attrition VARCHAR(5) NOT NULL
);

-- Adding indexes on frequently filtered and joined columns for performance
CREATE INDEX idx_emp_dept ON employees(Department);
CREATE INDEX idx_emp_salary ON employees(Salary);
CREATE INDEX idx_emp_workmode ON employees(WorkMode);
CREATE INDEX idx_emp_attrition ON employees(Attrition);

-- =====================================================================
-- SQL TASKS (10 Core Queries)
-- =====================================================================

-- Task 1: Retrieve the total number of employees in each department
-- Logic: Group by department, count total rows, and calculate % share of total workforce
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS WorkforcePercentage
FROM employees
GROUP BY Department
ORDER BY TotalEmployees DESC;

-- Task 2: Find the average salary department-wise
-- Logic: Aggregate AVG(Salary), MIN(Salary), and MAX(Salary) per department
SELECT 
    Department, 
    ROUND(AVG(Salary), 2) AS AverageSalary,
    ROUND(MIN(Salary), 2) AS MinSalary,
    ROUND(MAX(Salary), 2) AS MaxSalary
FROM employees
GROUP BY Department
ORDER BY AverageSalary DESC;

-- Task 3: Identify the top 10 highest-paid employees
-- Logic: Order by salary descending and limit output to top 10 records
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    Education, 
    YearsOfExperience, 
    Salary
FROM employees
ORDER BY Salary DESC
LIMIT 10;

-- Task 4: Calculate the average years of experience by department
-- Logic: Average the YearsOfExperience and YearsAtCompany per department
SELECT 
    Department, 
    ROUND(AVG(YearsOfExperience), 2) AS AvgExperienceYears,
    ROUND(AVG(YearsAtCompany), 2) AS AvgTenureAtCompany
FROM employees
GROUP BY Department
ORDER BY AvgExperienceYears DESC;

-- Task 5: Find employees with the highest performance rating (Rating = 4)
-- Logic: Use subquery to dynamically find the maximum rating value in the table
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    PerformanceRating, 
    Salary, 
    WorkMode
FROM employees
WHERE PerformanceRating = (SELECT MAX(PerformanceRating) FROM employees)
ORDER BY Salary DESC;

-- Task 6: Count employees based on work mode (Remote, Hybrid, Office)
-- Logic: Group by work mode and compute headcount and percentage
SELECT 
    WorkMode, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS AdoptionPercentage
FROM employees
GROUP BY WorkMode
ORDER BY EmployeeCount DESC;

-- Task 7: Identify departments with the highest employee attrition
-- Logic: Use conditional aggregation (SUM CASE) to count 'Yes' attrition per department
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS AttritionExits,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS AttritionRatePercent
FROM employees
GROUP BY Department
ORDER BY AttritionRatePercent DESC;

-- Task 8: Rank employees based on salary within each department
-- Logic: Window function DENSE_RANK() partitioned by department and ordered by salary desc
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    Salary, 
    DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS SalaryRankInDept
FROM employees
ORDER BY Department, SalaryRankInDept;

-- Task 9: Find employees earning above the company average salary
-- Logic: Subquery in WHERE clause comparing each employee's salary to company AVG(Salary)
SELECT 
    EmployeeID, 
    Department, 
    JobRole, 
    Salary,
    ROUND(Salary - (SELECT AVG(Salary) FROM employees), 2) AS SalaryAboveAverage
FROM employees
WHERE Salary > (SELECT AVG(Salary) FROM employees)
ORDER BY Salary DESC;

-- Task 10: Calculate gender-wise employee distribution
-- Logic: Group by Gender to inspect headcount, percentage, and average salary comparison
SELECT 
    Gender, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS DistributionPercentage,
    ROUND(AVG(Salary), 2) AS AvgSalaryByGender
FROM employees
GROUP BY Gender
ORDER BY EmployeeCount DESC;

-- =====================================================================
-- Helpful View for Power BI / Reporting
-- =====================================================================
CREATE OR REPLACE VIEW vw_department_summary AS
SELECT 
    Department,
    COUNT(*) AS TotalHeadcount,
    ROUND(AVG(Salary), 2) AS AvgSalary,
    ROUND(AVG(YearsOfExperience), 2) AS AvgExperience,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS AttritionRate,
    ROUND(AVG(PerformanceRating), 2) AS AvgPerformance
FROM employees
GROUP BY Department;
