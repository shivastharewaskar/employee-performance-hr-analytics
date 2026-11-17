# Power BI Dashboard Architecture & DAX Formula Specification

## Project 1: Employee Performance & HR Analytics
**Tool:** Microsoft Power BI Desktop / Power BI Service  
**Target Viewers:** HR Leadership, Executive Committee, Operations Directors  
**Data Source:** `employee_data_cleaned.csv` or MySQL Database (`HR_Analytics_DB`)  

---

## 1. Data Model & Architecture

### Schema Architecture
- **Table Name:** `Employees` (Import Mode or DirectQuery via MySQL)
- **Data Types Configured:**
  - `EmployeeID`: Text (Primary Key)
  - `Age`: Whole Number
  - `Gender`: Text
  - `Department`: Text
  - `JobRole`: Text
  - `Education`: Text
  - `YearsOfExperience`: Whole Number
  - `YearsAtCompany`: Whole Number
  - `Salary`: Decimal / Currency (₹ / INR or $)
  - `WorkMode`: Text (Categories: Remote, Hybrid, Office)
  - `PerformanceRating`: Whole Number (1-4)
  - `JobSatisfaction`: Whole Number (1-4)
  - `WorkLifeBalance`: Whole Number (1-4)
  - `Attrition`: Text ('Yes', 'No')

---

## 2. Certified DAX Measures for Core KPI Cards

Create a dedicated measure table `_Measures` in Power BI:

### KPI 1: Total Employees
```dax
Total Employees = COUNTROWS(Employees)
```
*Visual Format:* Card Visual | Data Label Display: None (Full number) or Thousands | Target: `1,200`

### KPI 2: Average Annual Salary
```dax
Average Salary = AVERAGE(Employees[Salary])
```
*Visual Format:* Card Visual | Formatting: Currency (₹) / Lakhs | Target: `₹11.02 Lakhs`

### KPI 3: Highest Salary
```dax
Highest Salary = MAX(Employees[Salary])
```
*Visual Format:* Card Visual | Formatting: Currency (₹) / Lakhs | Target: `₹30.07 Lakhs`

### KPI 4: Average Experience
```dax
Average Experience = AVERAGE(Employees[YearsOfExperience])
```
*Visual Format:* Card Visual | Format String: `0.0 "Years"` | Target: `6.5 Years`

### KPI 5: Attrition Rate (%)
```dax
Attrition Count = CALCULATE(COUNTROWS(Employees), Employees[Attrition] = "Yes")

Total Headcount = COUNTROWS(Employees)

Attrition Rate = 
DIVIDE(
    [Attrition Count],
    [Total Headcount],
    0
)
```
*Visual Format:* Card Visual | Formatting: Percentage (`0.0%`) | Target: `18.9%`

### KPI 6: Average Performance Rating
```dax
Average Performance Rating = AVERAGE(Employees[PerformanceRating])
```
*Visual Format:* Card Visual | Format String: `0.00 " / 4.0"` | Target: `2.84 / 4.0`

---

## 3. Supplementary Advanced DAX Measures

### High Performers Count (Rating 4)
```dax
High Performers Count = 
CALCULATE(
    COUNTROWS(Employees),
    Employees[PerformanceRating] = 4
)
```

### High Performers Below Median Salary (Flight Risk)
```dax
High Performers At Risk = 
CALCULATE(
    COUNTROWS(Employees),
    Employees[PerformanceRating] = 4,
    Employees[Salary] < [Average Salary]
)
```

### Retention Rate (%)
```dax
Retention Rate = 1 - [Attrition Rate]
```

### Dynamic KPI Card Header
```dax
Dashboard Title = "HR Enterprise Analytics Overview | Active Staff: " & FORMAT([Total Employees], "#,##0")
```

---

## 4. Multi-Page Dashboard Blueprint (7 Required Dashboards)

### Page 1: Employee Overview Dashboard
- **Top Row:** 6 KPI Cards (Total Staff, Avg Salary, Max Salary, Avg Exp, Attrition Rate, Avg Rating)
- **Top Right:** Slicers (Department dropdown, WorkMode buttons, Gender toggles)
- **Left Chart:** Donut Chart of `Department` Headcount Distribution
- **Center Chart:** Stacked Bar Chart of `JobRole` by `Department`
- **Right Chart:** Gauge Visual showing current Attrition Rate vs 15% corporate threshold

### Page 2: Salary Analysis Dashboard
- **Top Left:** Histogram / Column Chart of Salary bins (`₹4L-8L`, `₹8L-12L`, `₹12L-16L`, `₹16L-20L`, `>₹20L`)
- **Top Right:** Clustered Bar Chart: `Average Salary by Department`
- **Bottom Left:** Scatter Plot: `YearsOfExperience` (X-axis) vs `Salary` (Y-axis) with Trend Line
- **Bottom Right:** Matrix Visual displaying `Department` vs `Education` with Mean Salary Heatmap

### Page 3: Department Performance Dashboard
- **Top Left:** Clustered Column Chart: `Average Performance Rating by Department`
- **Top Right:** Stacked Bar Chart: `Performance Rating Breakdown (1 to 4) by Department`
- **Bottom Left:** Bar Chart: `Attrition Rate % by Department` (Highlighted with conditional Red alert for Sales at 24%)
- **Bottom Right:** Decomposition Tree: Exploring Attrition Root Causes by Department -> Role -> Salary Band

### Page 4: Employee Performance Dashboard
- **Top Row:** KPI Cards: Top Performers (Rating 4 Count), Low Performers (Rating 1 Count)
- **Main Visual:** Scatter Matrix: `Performance Rating` vs `JobSatisfaction` by `JobRole`
- **Bottom Left:** Table Visual: Filtered list of Top 20 Candidates for Annual Promotion
- **Bottom Right:** Funnel Chart: Distribution of Ratings across Organization

### Page 5: Work Mode Analysis Dashboard
- **Top Center:** 100% Stacked Bar Chart: `WorkMode` (Remote, Hybrid, Office) split across Departments
- **Bottom Left:** Clustered Bar Chart: `Average Satisfaction Score by Work Mode`
- **Bottom Center:** Clustered Bar Chart: `Average Performance Rating by Work Mode`
- **Bottom Right:** Donut Chart: `Attrition Rate by Work Mode`

### Page 6: Education Analysis Dashboard
- **Top Left:** Tree Map: Headcount by `Education Level` (Bachelor's, Master's, High School, Doctorate)
- **Top Right:** Clustered Bar Chart: `Average Salary by Education Level`
- **Bottom Left:** Boxplot Visual / Distribution: Experience vs Education
- **Bottom Right:** Table: Promotion rate & performance breakdown by educational background

### Page 7: Gender Analysis Dashboard
- **Top Left:** Donut Chart: `Gender Diversity Ratio` (56.3% Male / 43.8% Female)
- **Top Right:** Clustered Column Chart: `Gender Distribution across Departments`
- **Bottom Left:** Bar Chart: `Average Salary by Gender within Job Role` (Pay Equity Verification)
- **Bottom Right:** Metric Card: Pay Disparity Delta Index (<0.4%)

---

## 5. UI Theme, Color Palette & Export Guidance

### Corporate Palette Hex Codes:
- **Primary Blue (Navy):** `#1E3A8A`
- **Accent Cyan / Teal:** `#0F766E` / `#0284C7`
- **Alert / Attrition Red:** `#EF4444`
- **Success / Retention Green:** `#10B981`
- **Neutral Light Grey:** `#F8FAFC`
- **Text Dark:** `#0F172A`

### Step-by-Step Power BI Loading Instructions:
1. Open Power BI Desktop -> Click **Get Data** -> Select **Text/CSV**.
2. Browse to `01_Dataset/employee_data_cleaned.csv` and click **Load**.
3. Create a new measure group and paste the DAX expressions provided in Section 2.
4. Drag and drop the specified visual charts onto the respective pages.
5. Save the file as `Employee_Performance_HR_Analytics.pbix`.
