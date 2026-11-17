# Project 1: Employee Performance & HR Analytics

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![PowerBI](https://img.shields.io/badge/Power_BI-Desktop-yellow.svg)](https://powerbi.microsoft.com/)
[![Status](https://img.shields.io/badge/Status-Complete_%26_Validated-brightgreen.svg)]()

> **End-to-End Enterprise Data Analytics Project tailored for Academic Portals & Fresher Job Placement Portfolio.**

---

## 📋 Executive Overview

A modern enterprise with 1,200 active employees requires rigorous data-driven insights into employee performance, compensation distribution, department productivity, flexible work adoption (Remote/Hybrid/Office), education levels, and talent retention. 

This project delivers an end-to-end data analytics and business intelligence solution addressing:
1. **Relational Database Design & SQL Querying** (10 Complex Production SQL Queries including Window Functions & Subqueries).
2. **Python Exploratory Data Analysis (EDA)** (Handling missing values, deduplication, descriptive statistics, and correlation analysis).
3. **Data Visualization** (12 publication-grade charts covering distributions, categorical counts, regression plots, and heatmaps).
4. **Automated Executive PDF Report Generation** (Python ReportLab script compiling KPI cards, statistical tables, embedded visual plots, and strategic recommendations).
5. **Interactive Power BI Dashboard Architecture** (7 multi-page analytical views, 6 live DAX KPI Cards, and star schema modeling).

---

## 📂 Repository & Project Structure

```
Employee_Performance_HR_Analytics_Project/
│
├── 01_Dataset/
│   ├── employee_data_raw.csv                 # Raw dataset with deliberate anomalies & nulls
│   └── employee_data_cleaned.csv             # Cleaned, validated dataset (1,200 unique records)
│
├── 02_SQL_Analysis/
│   ├── hr_analytics_schema_and_queries.sql   # Complete SQL DDL, indexes, and all 10 analytical queries
│   └── sql_query_results_and_explanations.md # Query breakdown with result tables and business commentary
│
├── 03_Python_EDA/
│   ├── hr_eda_analysis.py                    # Standalone executable Python EDA script (all 13 steps)
│   └── hr_employee_analytics_eda.ipynb       # Fully annotated Jupyter Notebook for interactive exploration
│
├── 04_Visualizations/
│   ├── 01_salary_distribution_histogram.png  # Salary spread with KDE curve
│   ├── 02_age_distribution_histogram.png     # Age demographics breakdown
│   ├── 03_salary_boxplot.png                 # Departmental compensation quartiles & outliers
│   ├── 04_experience_boxplot.png             # Years of experience across business units
│   ├── 05_department_countplot.png           # Workforce headcount by department
│   ├── 06_gender_countplot.png               # Workforce gender diversity breakdown
│   ├── 07_education_countplot.png            # Educational qualification distribution
│   ├── 08_avg_salary_by_department_bar.png   # Comparative departmental compensation benchmarks
│   ├── 09_work_mode_pie_chart.png            # Remote vs Hybrid vs Office adoption shares
│   ├── 10_experience_vs_salary_scatter.png   # Experience-to-salary growth regression line
│   ├── 11_correlation_heatmap.png            # Multi-variable correlation matrix
│   └── 12_pairplot.png                       # Cross-metric distributions and scatter pairings
│
├── 05_Automated_Report/
│   ├── generate_pdf_report.py                # Automated Python script using ReportLab
│   ├── Employee_Performance_HR_Analytics_Executive_Report.pdf  # Comprehensive 6-page PDF Report
│   └── Business_Insights_and_Strategic_Recommendations.md      # Executive strategy & action roadmap
│
├── 06_Power_BI_Dashboard/
│   └── Power_BI_Dashboard_Design_and_DAX_Guide.md # Setup guide, DAX formulas for 6 KPI Cards & 7 Dashboards
│
├── README.md                                 # Complete project documentation & execution guide
└── Submission_Cover_Letter_and_Viva_Prep.md  # Academic portal submission cover letter & Viva Q&A
```

---

## 🛠️ Tech Stack & Requirements

- **Database:** MySQL 8.0+ / MariaDB / PostgreSQL / SQLite
- **Programming Language:** Python 3.8+
- **Key Python Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `reportlab`
- **Business Intelligence:** Microsoft Power BI Desktop

---

## 🚀 Execution Guide

### 1. Database Setup & SQL Execution
1. Open **MySQL Workbench**, **DBeaver**, or **phpMyAdmin**.
2. Run `02_SQL_Analysis/hr_analytics_schema_and_queries.sql`.
3. Import `01_Dataset/employee_data_cleaned.csv` into the `Employees` table.
4. Execute the 10 provided SQL queries to retrieve instant analytical reports.

### 2. Python EDA Pipeline Execution
Open your terminal/command prompt and run:
```bash
python 03_Python_EDA/hr_eda_analysis.py
```
Or open the interactive Jupyter Notebook:
```bash
jupyter notebook 03_Python_EDA/hr_employee_analytics_eda.ipynb
```

### 3. Automated Executive PDF Report Generation
To regenerate the executive PDF report dynamically:
```bash
python 05_Automated_Report/generate_pdf_report.py
```
This generates `05_Automated_Report/Employee_Performance_HR_Analytics_Executive_Report.pdf` with updated KPI tables and embedded charts.

### 4. Power BI Dashboard Setup
1. Launch **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV** -> Select `01_Dataset/employee_data_cleaned.csv`.
3. Follow the layout and copy the certified DAX formulas documented in `06_Power_BI_Dashboard/Power_BI_Dashboard_Design_and_DAX_Guide.md`.

---

## 📊 Core Analytical Findings & Business Highlights

| Metric | Empirical Finding | Strategic Interpretation |
| :--- | :--- | :--- |
| **Workforce Scale** | 1,200 Clean Records | Balanced cross-functional representation across 5 core departments. |
| **Sales Attrition** | 24.1% Attrition Rate | Highest in enterprise; driven by target volatility and lower base salary. |
| **Hybrid Efficiency** | 42.3% Workforce Share | Delivers highest job satisfaction (2.62/4.0) with zero performance drop. |
| **Pay Equity** | < 0.4% Gender Pay Gap | Outstanding corporate parity between male (₹11.04L) and female (₹11.00L) salaries. |
| **High Performer Alert**| 38.2% Underpaid Rating 4s | 92 top performers earn below department median, representing flight risks. |

---

## 🎓 Viva Voce & Fresher Technical Interview Prep

**Q1: Why did you use `DENSE_RANK()` instead of `RANK()` or `ROW_NUMBER()` in SQL Task 8?**  
*Answer:* `DENSE_RANK()` ensures that if two employees in the same department earn identical salaries, they receive the same rank, and the next rank is consecutive without skipping numbers. This provides a fair, contiguous ranking suitable for salary benchmarking.

**Q2: How did you handle missing values during the Python EDA phase?**  
*Answer:* Missing values in continuous variables like `Salary` were imputed using departmental median values rather than overall mean to prevent skewness from high-earning executives. Categorical missing values in `WorkMode` were imputed using modal frequency grouped by job family.

**Q3: How does Power BI calculate the Attrition Rate dynamically across slicers?**  
*Answer:* Using DAX `DIVIDE(CALCULATE(COUNTROWS(Employees), Employees[Attrition] = "Yes"), COUNTROWS(Employees), 0)`. The `CALCULATE` function modifies the filter context to count only employees who left, while respecting active department and work mode slicer filters.

---

## 📄 Submission Compliance
This project satisfies all requirements for academic portal upload:
- Single-file ZIP compression ready.
- Comprehensive code, data, visualizations, reports, and dashboards included.
