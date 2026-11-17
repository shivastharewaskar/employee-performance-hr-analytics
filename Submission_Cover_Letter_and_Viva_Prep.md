# Project Submission Document & Fresher Viva Guide

**Candidate Name:** [Your Name]  
**Enrollment / Student ID:** [Your Student ID]  
**Course / Track:** Data Analytics / Full-Stack Data Science & Business Intelligence  
**Project Chosen:** Project 1 - Employee Performance & HR Analytics  
**Submission Format:** Complete Single Compressed Archive (`.zip`)  

---

## 📌 Submission Statement & Summary (Copy-Paste for Portal Description Box)

### Project Title:
**End-to-End Employee Performance & HR Analytics (SQL, Python, Power BI)**

### Project Summary:
I have selected and executed **Project 1: Employee Performance & HR Analytics** from the project curriculum. This project represents a complete, industry-standard workforce intelligence solution analyzing 1,200 enterprise employees across 5 functional departments (Sales, Technology, R&D, HR, and Finance).

The deliverable includes:
1. **Relational Database & SQL Modeling:** A complete MySQL database schema (`HR_Analytics_DB`) with constraints, indexes, and full solutions for all **10 SQL Tasks** (including window functions like `DENSE_RANK()`, subqueries, and group-level aggregations).
2. **Python Exploratory Data Analysis (EDA):** A clean data pipeline executing data loading, deduplication (removing 20 duplicates), median-based null imputation (15 salaries, 10 work modes), descriptive statistics, and multi-variable correlations in both a standalone script (`hr_eda_analysis.py`) and a Jupyter Notebook (`hr_employee_analytics_eda.ipynb`).
3. **Data Visualizations:** All **12 publication-quality visualizations** saved in high resolution (Salary/Age Histograms, Department/Gender/Education Countplots, Boxplots, Scatter Plots with regression fit, and Correlation Heatmaps).
4. **Automated Executive PDF Reporting:** A Python script utilizing ReportLab that compiles an executive 6-page PDF report (`Employee_Performance_HR_Analytics_Executive_Report.pdf`) featuring KPI cards, summary tables, embedded charts, and strategic HR recommendations.
5. **Business Insights Document:** A comprehensive strategic document detailing retention drivers, pay parity findings (<0.4% gender disparity), hybrid work productivity, and a 4-pillar retention roadmap.
6. **Interactive Power BI Architecture:** Full design guide with certified DAX expressions for all **6 KPI Cards** (Total Employees, Avg Salary, Max Salary, Avg Experience, Attrition Rate, Avg Rating) across **7 interactive dashboards**.

All project code, cleaned datasets, high-resolution visual plots, and reports are structured in accordance with submission guidelines and packaged into a single archive for immediate evaluation.

---

## 🎯 Viva Voce & Technical Defense Prep (Top 10 Questions & Answers)

### Q1. Why is Employee Performance & HR Analytics the best project for a fresher?
> **Answer:** HR Analytics is universally applicable to every industry and company. Unlike niche domains, hiring managers and interviewers instantly understand and value attrition tracking, salary benchmarking, and hybrid work dynamics. It provides freshers the ideal platform to showcase advanced SQL (window functions, subqueries), Python data manipulation, statistical acumen, visual storytelling, automated PDF generation, and Power BI dashboard creation.

### Q2. What was your data cleaning strategy for handling missing values and duplicate records?
> **Answer:** In the raw dataset of 1,220 records, I identified 20 duplicate employee IDs and removed them using `drop_duplicates(subset=['EmployeeID'])`. For continuous missing values (15 missing salaries), I used median imputation grouped by department rather than overall mean to prevent skewness from high executive compensation. For categorical values (10 missing work modes), I used modal frequency based on job roles.

### Q3. Explain your approach to SQL Task 8: Ranking employees based on salary within each department.
> **Answer:** I utilized the window function `DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS SalaryRankInDept`. The `PARTITION BY` clause resets the ranking counter for each individual department, while `DENSE_RANK()` avoids gap ranking when ties occur, providing an accurate intra-departmental compensation hierarchy.

### Q4. What did the correlation analysis reveal between experience and salary?
> **Answer:** The Pearson correlation coefficient was **r = 0.917**, indicating a very strong positive linear association. This confirms that organizational compensation increases systematically with industry experience, though regression analysis also highlighted significant educational qualification premiums (Doctorates earning ~35% more than Bachelor's holders at equivalent tenure).

### Q5. What was the most significant business finding regarding employee attrition?
> **Answer:** The Sales department exhibited the highest attrition rate at **24.07%** (78 exits out of 324 staff), almost double that of HR (14.17%). Cross-variable analysis revealed this was driven by aggressive quota stress, lower base salaries, and low work-life balance scores (2.18 / 4.0).

### Q6. Did the data support the effectiveness of remote and hybrid work models?
> **Answer:** Yes. Hybrid (42.3%) and Remote (37.2%) employees represented 79.5% of the total workforce. Their performance ratings averaged 2.85 and 2.81 respectively, virtually identical to in-office employees (2.89), while hybrid workers reported the highest job satisfaction (mean 2.62 / 4.0) and lower voluntary resignation rates.

### Q7. How did you formulate the Attrition Rate measure in Power BI DAX?
> **Answer:** 
> ```dax
> Attrition Rate = 
> DIVIDE(
>     CALCULATE(COUNTROWS(Employees), Employees[Attrition] = "Yes"),
>     COUNTROWS(Employees),
>     0
> )
> ```
> `CALCULATE` modifies the evaluation context to count only employees who left (`Attrition = "Yes"`), while `DIVIDE` safely handles division by zero.

### Q8. What flight risk did you uncover regarding top performers?
> **Answer:** Out of 241 employees who achieved the highest Performance Rating of 4 (Outstanding), **38.2% (92 employees)** were compensated below their departmental median salary. This underpayment creates an acute vulnerability to competitor recruitment.

### Q9. How did you implement automated PDF reporting in Python?
> **Answer:** I developed a custom script using `reportlab.platypus` (`SimpleDocTemplate`, `Paragraph`, `Table`, `Image`, `PageBreak`). It connects directly to the cleaned dataset, computes live KPI metrics, formats executive tables, embeds the generated high-resolution PNG charts, applies headers/footers with dynamic page numbering via a two-pass `canvas.Canvas` subclass, and outputs a publication-grade PDF report.

### Q10. What recommendations would you present to the Chief HR Officer?
> **Answer:**
> 1. Restructure Sales compensation to a 70/30 base-to-variable model with quarterly milestone bonuses.
> 2. Institute off-cycle merit adjustments for the 92 underpaid Rating 4 performers.
> 3. Formally standardize the 3-day hybrid schedule as permanent corporate policy.
> 4. Establish 18-month fast-track progression paths for junior staff (1-3 years experience) to plug early-career churn.
