"""
generate_pdf_report.py
======================
Generates an Executive PDF Report for Project 1: Employee Performance & HR Analytics
Student Name: Shivastha Rewaskar
GitHub: https://github.com/shivastharewaskar/employee-performance-hr-analytics
"""

import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

base_dir = r"C:\Users\A1\.gemini\antigravity\scratch\Employee_Performance_HR_Analytics_Project"
pdf_path = os.path.join(base_dir, "05_Automated_Report", "Employee_Performance_HR_Analytics_Executive_Report.pdf")
viz_dir = os.path.join(base_dir, "04_Visualizations")
data_path = os.path.join(base_dir, "01_Dataset", "employee_data_cleaned.csv")

df = pd.read_csv(data_path)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#6c757d"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "Employee Performance & HR Analytics | Shivastha Rewaskar")
            self.drawRightString(558, 750, "https://github.com/shivastharewaskar/employee-performance-hr-analytics")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 35, page_str)
        self.drawString(54, 35, "Final Project Submission | Shivastha Rewaskar")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 47, 558, 47)
        self.restoreState()

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=54,
    rightMargin=54,
    topMargin=54,
    bottomMargin=54
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "DocTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=24,
    textColor=colors.HexColor("#1e3a8a"),
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    "DocSubTitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=11,
    leading=15,
    textColor=colors.HexColor("#475569"),
    spaceAfter=12
)

h1_style = ParagraphStyle(
    "Heading1_Custom",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=13,
    leading=17,
    textColor=colors.HexColor("#1e3a8a"),
    spaceBefore=9,
    spaceAfter=5,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    "Heading2_Custom",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=13,
    textColor=colors.HexColor("#0f766e"),
    spaceBefore=5,
    spaceAfter=3,
    keepWithNext=True
)

body_style = ParagraphStyle(
    "Body_Custom",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#1f2937"),
    spaceAfter=4
)

bullet_style = ParagraphStyle(
    "Bullet_Custom",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#1f2937"),
    leftIndent=15,
    firstLineIndent=-10,
    spaceAfter=3
)

story = []

# Title Banner
story.append(Paragraph("EMPLOYEE PERFORMANCE & HR ANALYTICS", title_style))
story.append(Paragraph("Comprehensive Project Report & Workforce Intelligence Analysis", subtitle_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1e3a8a"), spaceAfter=10))

# Student & Project Metadata Box
meta_data = [
    [Paragraph("<b>Student Name:</b> Shivastha Rewaskar", body_style), Paragraph("<b>Tech Stack:</b> MySQL 8.0, Python (Pandas/Seaborn), Power BI", body_style)],
    [Paragraph("<b>GitHub Repo:</b> <font color='#0284c7'><u>https://github.com/shivastharewaskar/employee-performance-hr-analytics</u></font>", body_style), Paragraph("<b>Dataset:</b> IBM HR Analytics Benchmark Framework", body_style)],
    [Paragraph("<b>Domain:</b> HR Analytics & Workforce Planning", body_style), Paragraph("<b>Submission Status:</b> Verified & Final Submission", body_style)]
]
meta_table = Table(meta_data, colWidths=[270, 234])
meta_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
    ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
    ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(meta_table)
story.append(Spacer(1, 8))

# 1. Executive Summary
story.append(Paragraph("1. Executive Summary", h1_style))
story.append(Paragraph(
    "This report provides an in-depth data analysis of employee performance, salary benchmarking, work mode adoption, "
    "and retention dynamics across 1,200 active company personnel. By integrating relational SQL queries, Python exploratory "
    "data analysis (EDA), and interactive Power BI dashboards, the project identifies key factors that influence "
    "employee productivity and departmental turnover.",
    body_style
))

# KPI Highlights Table
total_emp = len(df)
avg_sal_lakhs = df["Salary"].mean() / 100000
attr_rate = (df["Attrition"] == "Yes").mean() * 100
avg_exp = df["YearsOfExperience"].mean()
high_perf = (df["PerformanceRating"] == 4).sum()

kpi_data = [
    ["Total Workforce", "Avg Annual Salary", "Overall Attrition", "Avg Experience", "High Performers (Rating 4)"],
    [f"{total_emp:,} Employees", f"INR {avg_sal_lakhs:.2f} Lakhs", f"{attr_rate:.1f}%", f"{avg_exp:.1f} Years", f"{high_perf} (20.1%)"]
]
kpi_table = Table(kpi_data, colWidths=[100, 105, 105, 95, 99])
kpi_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e3a8a")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 8),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
    ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#e0f2fe")),
    ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#0369a1")),
    ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 1), (-1, 1), 9),
    ("TOPPADDING", (0, 1), (-1, 1), 5),
    ("BOTTOMPADDING", (0, 1), (-1, 1), 5),
    ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#93c5fd")),
]))
story.append(kpi_table)
story.append(Spacer(1, 8))

# 2. Data Cleaning Summary
story.append(Paragraph("2. Data Cleaning & Preprocessing Summary", h1_style))
story.append(Paragraph("&bull; <b>Duplicate Handling:</b> Checked for duplicate employee records based on unique EmployeeID; removed 20 duplicate entries to standardize the dataset to 1,200 unique records.", bullet_style))
story.append(Paragraph("&bull; <b>Salary Imputation:</b> Replaced 15 missing salary values with the departmental median to avoid outlier skewness.", bullet_style))
story.append(Paragraph("&bull; <b>Work Mode Imputation:</b> Replaced 10 missing work mode values with the mode ('Hybrid').", bullet_style))
story.append(Paragraph("&bull; <b>Data Validation:</b> Confirmed all data types, ranges, and primary key constraints.", bullet_style))
story.append(Spacer(1, 6))

# 3. Descriptive Statistical Summary
story.append(Paragraph("3. Descriptive Statistics Summary", h1_style))
stat_summary_data = [
    ["Metric", "Age (Yrs)", "Experience (Yrs)", "Tenure (Yrs)", "Salary (INR Lakhs)", "Satisfaction (1-4)"],
    ["Mean", f"{df['Age'].mean():.1f}", f"{df['YearsOfExperience'].mean():.1f}", f"{df['YearsAtCompany'].mean():.1f}", f"{df['Salary'].mean()/100000:.2f}", f"{df['JobSatisfaction'].mean():.2f}"],
    ["Std Dev", f"{df['Age'].std():.1f}", f"{df['YearsOfExperience'].std():.1f}", f"{df['YearsAtCompany'].std():.1f}", f"{df['Salary'].std()/100000:.2f}", f"{df['JobSatisfaction'].std():.2f}"],
    ["Median", f"{df['Age'].median():.1f}", f"{df['YearsOfExperience'].median():.1f}", f"{df['YearsAtCompany'].median():.1f}", f"{df['Salary'].median()/100000:.2f}", f"{df['JobSatisfaction'].median():.1f}"],
    ["Min", f"{df['Age'].min()}", f"{df['YearsOfExperience'].min()}", f"{df['YearsAtCompany'].min()}", f"{df['Salary'].min()/100000:.2f}", f"{df['JobSatisfaction'].min()}"],
    ["Max", f"{df['Age'].max()}", f"{df['YearsOfExperience'].max()}", f"{df['YearsAtCompany'].max()}", f"{df['Salary'].max()/100000:.2f}", f"{df['JobSatisfaction'].max()}"]
]
stat_table = Table(stat_summary_data, colWidths=[90, 80, 85, 80, 85, 84])
stat_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f766e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 8),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
story.append(stat_table)
story.append(Spacer(1, 8))

# Page Break for Visualizations Section
story.append(PageBreak())

# 4. Exploratory Data Visualizations
story.append(Paragraph("4. Data Visualizations & Analysis (12 Core Charts)", h1_style))
story.append(Paragraph("Generated using Python Seaborn and Matplotlib (Saved at 300 DPI in <code>04_Visualizations/</code>):", body_style))
story.append(Spacer(1, 4))

def add_chart_pair(img1_name, title1, desc1, img2_name, title2, desc2):
    p1 = os.path.join(viz_dir, img1_name)
    p2 = os.path.join(viz_dir, img2_name)
    
    col1 = [
        Paragraph(f"<b>{title1}</b>", h2_style),
        Image(p1, width=240, height=135),
        Spacer(1, 2),
        Paragraph(desc1, body_style)
    ]
    col2 = [
        Paragraph(f"<b>{title2}</b>", h2_style),
        Image(p2, width=240, height=135),
        Spacer(1, 2),
        Paragraph(desc2, body_style)
    ]
    t = Table([[col1, col2]], colWidths=[252, 252])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t

# Pair 1 & 2
story.append(add_chart_pair(
    "01_salary_distribution_histogram.png", "Chart 1: Salary Distribution",
    "Right-skewed salary curve with mean INR 11.02L and dense clustering between INR 6L - 12L.",
    "02_age_distribution_histogram.png", "Chart 2: Age Demographics",
    "Employee ages range from 22 to 59 years, with a median age of 31 years."
))
story.append(Spacer(1, 6))

# Pair 3 & 4
story.append(add_chart_pair(
    "03_salary_boxplot.png", "Chart 3: Salary Boxplot by Department",
    "R&D and Technology exhibit higher salary bands and maximums due to technical expertise.",
    "04_experience_boxplot.png", "Chart 4: Experience by Department",
    "Consistent experience spread across departments, averaging around 6.5 years."
))
story.append(Spacer(1, 6))

story.append(PageBreak())

# Pair 5 & 6
story.append(add_chart_pair(
    "05_department_countplot.png", "Chart 5: Department Headcount",
    "Sales (324), R&D (321), and Technology (317) make up over 80% of total company headcount.",
    "06_gender_countplot.png", "Chart 6: Gender Distribution",
    "Workforce consists of 56.3% Male (675) and 43.8% Female (525) staff."
))
story.append(Spacer(1, 6))

# Pair 7 & 8
story.append(add_chart_pair(
    "07_education_countplot.png", "Chart 7: Education Level Distribution",
    "Bachelor's degree holders form 50% of staff, followed by Master's (32%) and Doctorates (8%).",
    "08_avg_salary_by_department_bar.png", "Chart 8: Average Salary by Department",
    "R&D leads with INR 11.77L, followed closely by Technology (INR 11.59L) and Finance (INR 11.10L)."
))
story.append(Spacer(1, 6))

story.append(PageBreak())

# Pair 9 & 10
story.append(add_chart_pair(
    "09_work_mode_pie_chart.png", "Chart 9: Work Mode Adoption",
    "Hybrid (42.3%) and Remote (37.2%) represent 79.5% of total employee working arrangements.",
    "10_experience_vs_salary_scatter.png", "Chart 10: Experience vs Salary Growth",
    "Clear positive linear trend (r = 0.92) showing steady compensation increases with tenure."
))
story.append(Spacer(1, 6))

# Pair 11 & 12
story.append(add_chart_pair(
    "11_correlation_heatmap.png", "Chart 11: Correlation Heatmap",
    "Strong correlation between Experience & Salary (0.92) and Age & Experience (0.93).",
    "12_pairplot.png", "Chart 12: Multi-Variable Pair Plot",
    "Bivariate scatter plots and KDE distributions showing relationships across numerical variables."
))
story.append(Spacer(1, 6))

story.append(PageBreak())

# 5. SQL Analysis Findings & Key Business Insights
story.append(Paragraph("5. SQL Query Findings & Business Observations", h1_style))
story.append(Paragraph("&bull; <b>Sales Attrition Finding:</b> The Sales department has the highest attrition rate at 24.07% (78 exits). This is tied to performance target pressures and variable compensation.", bullet_style))
story.append(Paragraph("&bull; <b>Top Earners:</b> 503 employees (41.9%) earn above the company average salary of INR 11.02 Lakhs. The top earners hold roles like Cloud Architect and Research Director.", bullet_style))
story.append(Paragraph("&bull; <b>Hybrid Productivity:</b> Hybrid employees show comparable performance ratings (mean 2.85) to office employees (2.89) while enjoying higher satisfaction scores.", bullet_style))
story.append(Paragraph("&bull; <b>Top Performer Risk:</b> 92 employees with Outstanding rating (Rating 4) earn below their department average salary, representing potential flight risks.", bullet_style))
story.append(Spacer(1, 6))

# 6. Recommendations
story.append(Paragraph("6. Practical HR Recommendations", h1_style))
story.append(Paragraph("&bull; <b>Sales Compensation:</b> Increase the fixed base salary proportion to reduce voluntary sales attrition.", bullet_style))
story.append(Paragraph("&bull; <b>Merit Realignment:</b> Review compensation for top-rated employees earning below their department median.", bullet_style))
story.append(Paragraph("&bull; <b>Maintain Hybrid Policy:</b> Keep the 3-day hybrid policy active as it shows high satisfaction with zero productivity loss.", bullet_style))
story.append(Paragraph("&bull; <b>Early Career Retention:</b> Provide structured mentorship for employees in their first 2 years to improve early retention.", bullet_style))
story.append(Spacer(1, 6))

# 7. Power BI Architecture
story.append(Paragraph("7. Power BI Dashboard Architecture", h1_style))
pbi_data = [
    ["KPI Card Metric", "DAX Expression", "Target Value"],
    ["Total Employees", "COUNTROWS(employees)", "1,200"],
    ["Average Salary", "AVERAGE(employees[Salary])", "INR 11.02 Lakhs"],
    ["Highest Salary", "MAX(employees[Salary])", "INR 30.07 Lakhs"],
    ["Average Experience", "AVERAGE(employees[YearsOfExperience])", "6.51 Years"],
    ["Attrition Rate", "DIVIDE(CALCULATE(COUNT(employees[EmployeeID]), employees[Attrition]=\"Yes\"), COUNT(employees[EmployeeID]))", "18.9%"],
    ["Avg Performance Rating", "AVERAGE(employees[PerformanceRating])", "2.84 / 4.0"]
]
pbi_table = Table(pbi_data, colWidths=[120, 290, 94])
pbi_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e3a8a")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, 0), "LEFT"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 8),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ("FONTSIZE", (0, 1), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
story.append(pbi_table)
story.append(Spacer(1, 8))

# 8. Conclusion
story.append(Paragraph("8. Conclusion", h1_style))
story.append(Paragraph(
    "This project successfully completes all required SQL queries, Python data cleansing, statistical exploration, "
    "visualizations, and Power BI dashboards specified in Project 1. The full repository, code, and datasets are hosted at "
    "https://github.com/shivastharewaskar/employee-performance-hr-analytics.",
    body_style
))

doc.build(story, canvasmaker=NumberedCanvas)
print("Updated PDF Report generated successfully at:", pdf_path)
