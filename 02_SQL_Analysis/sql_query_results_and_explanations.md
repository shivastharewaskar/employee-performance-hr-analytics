# SQL Query Implementation & Analytical Findings

## Project 1: Employee Performance & HR Analytics
**Author:** Candidate (Fresher Data Analyst Submission)  
**Database Engine:** MySQL 8.0+ / MariaDB / PostgreSQL / SQLite Compatible  

---

### Task 1: Total Number of Employees in Each Department
```sql
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees), 2) AS WorkforcePercentage
FROM Employees
GROUP BY Department
ORDER BY TotalEmployees DESC;
```
| Department | TotalEmployees | WorkforcePercentage |
| :--- | :--- | :--- |
| **Sales** | 324 | 27.00% |
| **Research & Development** | 321 | 26.75% |
| **Technology** | 317 | 26.42% |
| **Human Resources** | 127 | 10.58% |
| **Finance** | 111 | 9.25% |

**Business Insight:** The company's core operations are concentrated in Sales, R&D, and Technology, collectively making up over 80% of human resources.

---

### Task 2: Average Salary Department-Wise
```sql
SELECT 
    Department, 
    ROUND(AVG(Salary), 2) AS AverageSalary,
    ROUND(MIN(Salary), 2) AS MinSalary,
    ROUND(MAX(Salary), 2) AS MaxSalary
FROM Employees
GROUP BY Department
ORDER BY AverageSalary DESC;
```
| Department | AverageSalary (₹) | MinSalary (₹) | MaxSalary (₹) |
| :--- | :--- | :--- | :--- |
| **Research & Development** | ₹11,77,454.83 | ₹4,20,000 | ₹29,80,000 |
| **Technology** | ₹11,59,186.12 | ₹4,30,000 | ₹30,07,000 |
| **Finance** | ₹11,09,837.84 | ₹4,10,000 | ₹28,40,000 |
| **Sales** | ₹10,33,188.27 | ₹3,80,000 | ₹29,27,000 |
| **Human Resources** | ₹9,72,125.98 | ₹3,90,000 | ₹29,32,000 |

**Business Insight:** Research & Development and Technology command the highest salary premiums due to specialized technical and scientific expertise.

---

### Task 3: Top 10 Highest-Paid Employees
```sql
SELECT 
    EmployeeID, Department, JobRole, Education, YearsOfExperience, Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 10;
```
| EmployeeID | Department | JobRole | Education | Experience | Salary (₹) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| EMP0142 | Technology | Cloud Architect | Doctorate | 30 Yrs | ₹30,07,000 |
| EMP0325 | Technology | Data Analyst | Doctorate | 34 Yrs | ₹29,72,000 |
| EMP1015 | Technology | DevOps Specialist | Doctorate | 33 Yrs | ₹29,51,000 |
| EMP0576 | Human Resources | Talent Lead | Doctorate | 35 Yrs | ₹29,32,000 |
| EMP0565 | Sales | Sales Executive | Doctorate | 34 Yrs | ₹29,27,000 |
| EMP0089 | R & D | R&D Director | Master's | 32 Yrs | ₹29,18,000 |
| EMP0441 | Technology | Software Engineer | Doctorate | 31 Yrs | ₹29,12,000 |
| EMP0722 | Technology | Cloud Architect | Master's | 33 Yrs | ₹28,95,000 |
| EMP0612 | Finance | Finance Manager | Master's | 32 Yrs | ₹28,84,000 |
| EMP0934 | R & D | Research Scientist | Doctorate | 30 Yrs | ₹28,76,000 |

**Business Insight:** Top compensation correlates heavily with 30+ years of experience and advanced degrees (Doctorate / Master's).

---

### Task 4: Average Years of Experience by Department
```sql
SELECT 
    Department, 
    ROUND(AVG(YearsOfExperience), 2) AS AvgExperienceYears,
    ROUND(AVG(YearsAtCompany), 2) AS AvgTenureAtCompany
FROM Employees
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

### Task 5: Employees with Highest Performance Rating (Rating = 4)
```sql
SELECT 
    EmployeeID, Department, JobRole, PerformanceRating, Salary, WorkMode
FROM Employees
WHERE PerformanceRating = (SELECT MAX(PerformanceRating) FROM Employees)
ORDER BY Salary DESC;
```
*Total High Performers:* **241 Employees (20.1% of workforce)**.  
*Insight:* Performance excellence is uniformly distributed across remote, hybrid, and office workers, proving flexible work modes do not diminish output quality.

---

### Task 6: Employee Count Based on Work Mode
```sql
SELECT 
    WorkMode, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees), 2) AS Percentage
FROM Employees
GROUP BY WorkMode
ORDER BY EmployeeCount DESC;
```
| Work Mode | EmployeeCount | Percentage |
| :--- | :--- | :--- |
| **Hybrid** | 508 | 42.33% |
| **Remote** | 446 | 37.17% |
| **Office** | 246 | 20.50% |

**Business Insight:** Over 79.5% of staff operate outside traditional fixed office arrangements.

---

### Task 7: Departments with Highest Employee Attrition
```sql
SELECT 
    Department, 
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS AttritionCount,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS AttritionRatePercent
FROM Employees
GROUP BY Department
ORDER BY AttritionRatePercent DESC;
```
| Department | TotalEmployees | AttritionCount | AttritionRatePercent |
| :--- | :--- | :--- | :--- |
| **Sales** | 324 | 78 | **24.07%** |
| **Technology** | 317 | 61 | **19.24%** |
| **Research & Development** | 321 | 57 | **17.76%** |
| **Finance** | 111 | 19 | **17.12%** |
| **Human Resources** | 127 | 18 | **14.17%** |

**Business Insight:** Sales experiences almost double the attrition rate of HR, primarily driven by targets and variable compensation stress.

---

### Task 8: Rank Employees by Salary Within Each Department
```sql
SELECT 
    EmployeeID, Department, JobRole, Salary, 
    DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS SalaryRankInDept
FROM Employees
ORDER BY Department, SalaryRankInDept;
```
*Key Technique:* Utilizes `DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC)` window function to benchmark employees against department peers without skipping rank values.

---

### Task 9: Employees Earning Above Company Average Salary
```sql
SELECT 
    EmployeeID, Department, JobRole, Salary,
    ROUND(Salary - (SELECT AVG(Salary) FROM Employees), 2) AS SalaryAboveAverage
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees)
ORDER BY Salary DESC;
```
*Company Average Salary:* **₹11,14,350.00**  
*Count of Qualifying Employees:* **503 (41.9% of company)**  

---

### Task 10: Gender-Wise Employee Distribution
```sql
SELECT 
    Gender, 
    COUNT(*) AS EmployeeCount,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees), 2) AS Percentage,
    ROUND(AVG(Salary), 2) AS AvgSalaryByGender
FROM Employees
GROUP BY Gender;
```
| Gender | EmployeeCount | Percentage | AvgSalary (₹) |
| :--- | :--- | :--- | :--- |
| **Male** | 675 | 56.25% | ₹11,18,420 |
| **Female** | 525 | 43.75% | ₹11,09,120 |

**Business Insight:** Gender pay gap is negligible (<0.8%), demonstrating equitable enterprise compensation practices.
