# SQL Query Solutions & Execution Results

**Student Name:** Shivastha Rewaskar  
**GitHub Repository:** [https://github.com/shivastharewaskar/employee-performance-hr-analytics](https://github.com/shivastharewaskar/employee-performance-hr-analytics)  
**Project:** Employee Performance & HR Analytics  
**Database:** MySQL 8.0+  

---

### Task 1: Retrieve the total number of employees in each department
```sql
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS WorkforcePercentage
FROM employees
GROUP BY Department
ORDER BY TotalEmployees DESC;
```
**Output:**
| Department | TotalEmployees | WorkforcePercentage |
| :--- | :--- | :--- |
| **Sales** | 324 | 27.00% |
| **Research & Development** | 321 | 26.75% |
| **Technology** | 317 | 26.42% |
| **Human Resources** | 127 | 10.58% |
| **Finance** | 111 | 9.25% |

*My Observation:* Sales, R&D, and Technology make up about 80% of our total workforce. HR and Finance are smaller administrative units.

---

### Task 2: Find the average salary department-wise
```sql
SELECT 
    Department, 
    ROUND(AVG(Salary), 2) AS AverageSalary,
    ROUND(MIN(Salary), 2) AS MinSalary,
    ROUND(MAX(Salary), 2) AS MaxSalary
FROM employees
GROUP BY Department
ORDER BY AverageSalary DESC;
```
**Output:**
| Department | AverageSalary (₹) | MinSalary (₹) | MaxSalary (₹) |
| :--- | :--- | :--- | :--- |
| **Research & Development** | ₹11,77,454.83 | ₹4,20,000 | ₹29,80,000 |
| **Technology** | ₹11,59,186.12 | ₹4,30,000 | ₹30,07,000 |
| **Finance** | ₹11,09,837.84 | ₹4,10,000 | ₹28,40,000 |
| **Sales** | ₹10,33,188.27 | ₹3,80,000 | ₹29,27,000 |
| **Human Resources** | ₹9,72,125.98 | ₹3,90,000 | ₹29,32,000 |

*My Observation:* Technical departments like R&D and Technology have the highest average pay due to specialized roles like Scientists and Cloud Architects.

---

### Task 3: Identify the top 10 highest-paid employees
```sql
SELECT 
    EmployeeID, Department, JobRole, Education, YearsOfExperience, Salary
FROM employees
ORDER BY Salary DESC
LIMIT 10;
```
*My Observation:* The top 10 highest paid employees all have 30+ years of experience and advanced degrees (Master's or Doctorate).

---

### Task 4: Calculate the average years of experience by department
```sql
SELECT 
    Department, 
    ROUND(AVG(YearsOfExperience), 2) AS AvgExperienceYears,
    ROUND(AVG(YearsAtCompany), 2) AS AvgTenureAtCompany
FROM employees
GROUP BY Department
ORDER BY AvgExperienceYears DESC;
```
| Department | AvgExperienceYears | AvgTenureAtCompany |
| :--- | :--- | :--- |
| **Technology** | 6.77 Years | 3.42 Years |
| **Sales** | 6.52 Years | 3.19 Years |
| **Human Resources** | 6.43 Years | 3.25 Years |
| **Finance** | 6.43 Years | 3.31 Years |
| **Research & Development** | 6.28 Years | 3.14 Years |

---

### Task 5: Find employees with the highest performance rating (Rating = 4)
```sql
SELECT 
    EmployeeID, Department, JobRole, PerformanceRating, Salary, WorkMode
FROM employees
WHERE PerformanceRating = (SELECT MAX(PerformanceRating) FROM employees)
ORDER BY Salary DESC;
```
*My Observation:* 241 employees achieved a rating of 4 (Outstanding). They are evenly distributed across Remote, Hybrid, and Office work modes.

---

### Task 6: Count employees based on work mode (Remote, Hybrid, Office)
```sql
SELECT 
    WorkMode, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS AdoptionPercentage
FROM employees
GROUP BY WorkMode
ORDER BY EmployeeCount DESC;
```
| Work Mode | EmployeeCount | Percentage |
| :--- | :--- | :--- |
| **Hybrid** | 508 | 42.33% |
| **Remote** | 446 | 37.17% |
| **Office** | 246 | 20.50% |

*My Observation:* Over 79% of employees work either Hybrid or Remote, showing flexible work is the dominant preference.

---

### Task 7: Identify departments with the highest employee attrition
```sql
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS AttritionExits,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS AttritionRatePercent
FROM employees
GROUP BY Department
ORDER BY AttritionRatePercent DESC;
```
| Department | TotalEmployees | AttritionExits | AttritionRatePercent |
| :--- | :--- | :--- | :--- |
| **Sales** | 324 | 78 | **24.07%** |
| **Technology** | 317 | 61 | **19.24%** |
| **Research & Development** | 321 | 57 | **17.76%** |
| **Finance** | 111 | 19 | **17.12%** |
| **Human Resources** | 127 | 18 | **14.17%** |

*My Observation:* Sales has the highest attrition rate at 24.07%, while HR has the lowest at 14.17%.

---

### Task 8: Rank employees based on salary within each department
```sql
SELECT 
    EmployeeID, Department, JobRole, Salary, 
    DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS SalaryRankInDept
FROM employees
ORDER BY Department, SalaryRankInDept;
```
*My Observation:* I used `DENSE_RANK()` so that ties get the same rank and no subsequent numbers are skipped.

---

### Task 9: Find employees earning above the company average salary
```sql
SELECT 
    EmployeeID, Department, JobRole, Salary,
    ROUND(Salary - (SELECT AVG(Salary) FROM employees), 2) AS SalaryAboveAverage
FROM employees
WHERE Salary > (SELECT AVG(Salary) FROM employees)
ORDER BY Salary DESC;
```
*My Observation:* The average salary across the company is ₹11,02,098. Exactly 503 employees (41.9%) earn above this benchmark.

---

### Task 10: Calculate gender-wise employee distribution
```sql
SELECT 
    Gender, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS Percentage,
    ROUND(AVG(Salary), 2) AS AvgSalaryByGender
FROM employees
GROUP BY Gender;
```
| Gender | EmployeeCount | Percentage | AvgSalary (₹) |
| :--- | :--- | :--- | :--- |
| **Male** | 675 | 56.25% | ₹11,03,988 |
| **Female** | 525 | 43.75% | ₹10,99,668 |

*My Observation:* The gender pay gap is negligible (<0.4%), showing fair compensation parity between male and female employees.
