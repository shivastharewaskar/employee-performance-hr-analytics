# Strategic Business Insights & Human Capital Recommendations

**Student Name:** Shivastha Rewaskar  
**GitHub Repository:** [https://github.com/shivastharewaskar/employee-performance-hr-analytics](https://github.com/shivastharewaskar/employee-performance-hr-analytics)  
**Project:** Employee Performance & HR Analytics  
**Dataset:** 1,200 Enterprise Employee Records across 5 Departments  

---

## 1. Project Background
This project analyzes workforce data across 1,200 employees to understand what factors affect employee performance, salary levels, work modes, and attrition. By combining SQL queries, Python EDA, and Power BI dashboards, I examined why employees leave and how companies can retain top talent.

---

## 2. Key Observations from Data Analysis

### A. High Turnover in Sales Department
- **Finding:** The Sales department records a **24.07% attrition rate** (78 exits out of 324 employees). This is significantly higher than HR (14.17%), Finance (17.12%), and R&D (17.76%).
- **Reason:** Correlation and scatter plot analysis reveal lower base salaries and higher reliance on variable sales incentives, creating quota pressure and lower work-life balance (average 2.18 / 4.0 in Sales).

### B. Underpayment Risk for Top Performers
- **Finding:** Out of 241 employees who achieved an Outstanding performance rating (Rating 4), **92 employees (38.2%)** currently earn below their department average salary.
- **Risk:** High-performing employees who are underpaid are at high risk of being poached by competing companies.

### C. Effectiveness of Hybrid Work
- **Finding:** Hybrid workers make up 42.3% of the company, Remote workers 37.2%, and Office workers 20.5%.
- **Insight:** Performance ratings are virtually identical across all three work modes (Office: 2.89, Hybrid: 2.85, Remote: 2.81), but Hybrid workers report the highest job satisfaction scores (mean 2.62 / 4.0). Flexible work does not hurt performance.

### D. Career Progression & Early Tenure Churn
- **Finding:** While experience and salary have a very strong correlation (**r = 0.917**), voluntary departures are concentrated in employees within their first 1–3 years at the company.
- **Insight:** Employees often seek external offers after gaining 2 years of experience if internal promotions are slow.

### E. Diversity and Pay Parity
- **Finding:** The workforce is 56.3% Male and 43.8% Female.
- **Parity:** Male average salary is ₹11,03,988 and Female average salary is ₹10,99,668 (a variance of less than 0.4%), demonstrating equitable compensation.

---

## 3. Practical Recommendations

1. **Rebalance Sales Pay:** Increase the fixed base salary proportion to 70% (from 50%) and provide quarterly retention bonuses to stabilize Sales staff.
2. **Review High Performer Pay:** Conduct an off-cycle salary calibration for the 92 top-rated employees who are earning below departmental averages.
3. **Formalize 3-Day Hybrid Model:** Maintain hybrid work as the official company policy to preserve employee morale without sacrificing output.
4. **Structured Early Career Path:** Introduce 18-month career progression milestones for junior staff to reduce early tenure turnover.
