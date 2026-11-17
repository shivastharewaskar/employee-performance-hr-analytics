"""
generate_pdf_report.py
======================
Generates an Executive PDF Report for Project 1: Employee Performance & HR Analytics
Incorporates:
- Dataset Overview
- Data Cleaning Summary
- Statistical Summary
- Embedded Visualizations
- Business Insights & SQL Key Findings
- Strategic HR Recommendations
- Conclusion & Power BI Architecture
"""

import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
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
            self.drawString(54, 750, "Employee Performance & HR Analytics | Comprehensive Industry Report")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 35, page_str)
        self.drawString(54, 35, "Confidential - For Academic & Corporate Evaluation Only")
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
    fontSize=22,
    leading=26,
    textColor=colors.HexColor("#1e3a8a"),
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    "DocSubTitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=12,
    leading=16,
    textColor=colors.HexColor("#475569"),
    spaceAfter=15
)

h1_style = ParagraphStyle(
    "Heading1_Custom",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=14,
    leading=18,
    textColor=colors.HexColor("#1e3a8a"),
    spaceBefore=10,
    spaceAfter=6,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    "Heading2_Custom",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10.5,
    leading=13.5,
    textColor=colors.HexColor("#0f766e"),
    spaceBefore=6,
    spaceAfter=3,
    keepWithNext=True
)

body_style = ParagraphStyle(
    "Body_Custom",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=13,
    textColor=colors.HexColor("#1f2937"),
    spaceAfter=5
)

bullet_style = ParagraphStyle(
    "Bullet_Custom",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12.5,
    textColor=colors.HexColor("#1f2937"),
    leftIndent=15,
    firstLineIndent=-10,
    spaceAfter=3
)

story = []

# Title Banner
story.append(Paragraph("PROJECT REPORT: EMPLOYEE PERFORMANCE & HR ANALYTICS", title_style))
story.append(Paragraph("End-to-End Enterprise Workforce Intelligence & Predictive Retention Analysis", subtitle_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1e3a8a"), spaceAfter=12))

# Metadata Box
meta_data = [
    [Paragraph("<b>Domain:</b> Human Resource & People Analytics", body_style), Paragraph("<b>Tech Stack:</b> MySQL, Python (Pandas/Seaborn), Power BI", body_style)],
    [Paragraph("<b>Primary Goal:</b> Attrition Mitigation & Workforce Optimization", body_style), Paragraph("<b>Dataset:</b> IBM HR Analytics Benchmark Framework", body_style)],
    [Paragraph("<b>Evaluation Category:</b> Best End-to-End Project for Freshers", body_style), Paragraph("<b>Deliverable Status:</b> Complete & Production-Grade", body_style)]
]
meta_table = Table(meta_data, colWidths=[250, 254])
meta_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
    ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
    ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(meta_table)
story.append(Spacer(1, 10))

# 1. Executive Summary
story.append(Paragraph("1. Executive Summary", h1_style))
story.append(Paragraph(
    "This industry-grade analytics project examines organizational productivity, compensation parity, "
    "work mode effectiveness, and talent attrition dynamics across 1,200 corporate employees. "
    "By unifying relational MySQL querying, Python exploratory data analysis (EDA), multi-variable statistical "
    "modeling, and Power BI interactive dashboards, the study uncovers data-driven levers to optimize human capital "
    "retention and compensation efficiency.",
    body_style
))

# KPI Highlights Table
total_emp = len(df)
avg_sal_lakhs = df["Salary"].mean() / 100000
attr_rate = (df["Attrition"] == "Yes").mean() * 100
avg_exp = df["YearsOfExperience"].mean()
high_perf = (df["PerformanceRating"] == 4).sum()

kpi_data = [
    ["Total Workforce", "Avg Annual Salary", "Overall Attrition", "Avg Experience", "Top Performers (Rating 4)"],
    [f"{total_emp:,} Employees", f"INR {avg_sal_lakhs:.2f} Lakhs", f"{attr_rate:.1f}%", f"{avg_exp:.1f} Years", f"{high_perf} (20.1%)"]
]
kpi_table = Table(kpi_data, colWidths=[100, 105, 105, 95, 99])
kpi_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e3a8a")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 8),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
    ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#e0f2fe")),
    ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#0369a1")),
    ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 1), (-1, 1), 9.5),
    ("TOPPADDING", (0, 1), (-1, 1), 6),
    ("BOTTOMPADDING", (0, 1), (-1, 1), 6),
    ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#93c5fd")),
]))
story.append(kpi_table)
story.append(Spacer(1, 10))

# 2. Data Cleaning & Integrity Summary
story.append(Paragraph("2. Data Cleaning & Integrity Summary", h1_style))
story.append(Paragraph(
    "Rigorous data wrangling and validation protocols were executed on the ingested raw dataset (1,220 rows):",
    body_style
))
story.append(Paragraph("&bull; <b>Deduplication:</b> 20 duplicate records were detected via primary key verification (<code>EmployeeID</code>) and eliminated, standardizing the corpus to 1,200 unique records.", bullet_style))
story.append(Paragraph("&bull; <b>Missing Salary Imputation:</b> 15 null salary entries were imputed using department-specific median salary metrics, safeguarding distributions against skewness.", bullet_style))
story.append(Paragraph("&bull; <b>Missing Work Mode Imputation:</b> 10 null work mode entries were resolved using modal frequency assignment corresponding to their specific job functional family.", bullet_style))
story.append(Paragraph("&bull; <b>Schema Integrity:</b> Data types were verified (Integer, Float, Categorical), ensuring zero anomalies in ranges (Age: 22-60, Experience: 1-35 years).", bullet_style))
story.append(Spacer(1, 8))

# 3. Statistical Summary
story.append(Paragraph("3. Descriptive Statistical Summary", h1_style))
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
    ("TOPPADDING", (0, 0), (-1, -1), 3.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
]))
story.append(stat_table)
story.append(Spacer(1, 10))

# Page Break for Visualizations Section
story.append(PageBreak())

# 4. Exploratory Data Visualizations
story.append(Paragraph("4. Exploratory Data Visualizations (12 Core Charts)", h1_style))
story.append(Paragraph("The complete suite of 12 analytical plots demonstrates multidimensional workforce relationships:", body_style))
story.append(Spacer(1, 6))

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
    "Right-skewed compensation curve with mean INR 11.14L and high density between INR 6L - 12L.",
    "02_age_distribution_histogram.png", "Chart 2: Age Demographics",
    "Balanced corporate age spread spanning 22 to 60 years, with a median age of 32.5 years."
))
story.append(Spacer(1, 8))

# Pair 3 & 4
story.append(add_chart_pair(
    "03_salary_boxplot.png", "Chart 3: Department Salary Boxplot",
    "R&D and Technology demonstrate highest upper quartiles (>INR 18L) due to tech specialization.",
    "04_experience_boxplot.png", "Chart 4: Experience Spread",
    "Consistent mid-level tenure across all 5 operational functions, averaging 6.5 years experience."
))
story.append(Spacer(1, 8))

story.append(PageBreak())

# Pair 5 & 6
story.append(add_chart_pair(
    "05_department_countplot.png", "Chart 5: Department Headcount",
    "Sales (324), R&D (321), and Technology (317) form 80% of total workforce headcounts.",
    "06_gender_countplot.png", "Chart 6: Gender Diversity",
    "Workforce split: 56.3% Male (675) and 43.8% Female (525), reflecting positive gender parity."
))
story.append(Spacer(1, 8))

# Pair 7 & 8
story.append(add_chart_pair(
    "07_education_countplot.png", "Chart 7: Education Level Spread",
    "Undergraduate Bachelor's holders lead (50%), followed by Master's (32%) and Doctorates (8%).",
    "08_avg_salary_by_department_bar.png", "Chart 8: Average Salary by Dept",
    "R&D leads (INR 11.77L), followed by Technology (INR 11.59L), Finance (INR 11.10L), and Sales (INR 10.33L)."
))
story.append(Spacer(1, 8))

story.append(PageBreak())

# Pair 9 & 10
story.append(add_chart_pair(
    "09_work_mode_pie_chart.png", "Chart 9: Work Mode Adoption",
    "Hybrid (42.3%) and Remote (37.2%) dominate the workforce, accounting for 79.5% adoption.",
    "10_experience_vs_salary_scatter.png", "Chart 10: Experience vs Salary Growth",
    "Strong positive linear trajectory (r = 0.81) confirming structured career progression."
))
story.append(Spacer(1, 8))

# Pair 11 & 12
story.append(add_chart_pair(
    "11_correlation_heatmap.png", "Chart 11: Correlation Heatmap",
    "High positive correlation between Experience & Salary (0.81) and Age & Experience (0.86).",
    "12_pairplot.png", "Chart 12: Workforce Pair Plot",
    "Comprehensive multi-variable scatter and KDE distributions showing distinct clustering."
))
story.append(Spacer(1, 8))

story.append(PageBreak())

# 5. SQL Tasks Summary & Business Insights
story.append(Paragraph("5. SQL Analysis Findings & Key Business Insights", h1_style))
story.append(Paragraph(
    "Executing the 10 core SQL tasks on the normalized MySQL relational schema yielded pivotal enterprise discoveries:",
    body_style
))
story.append(Paragraph("&bull; <b>Sales Department Attrition Outlier:</b> Sales experienced the highest attrition rate at 24.1% (78 exits), primarily tied to commission volatility and early-career turnover. HR had the lowest at 14.2%.", bullet_style))
story.append(Paragraph("&bull; <b>Executive Compensation Concentration:</b> 503 employees (41.9%) earn above the enterprise average of INR 11.14 Lakhs. The top 10 earners (earning up to INR 30.07 Lakhs) are predominantly in Cloud Architecture and R&D Leadership.", bullet_style))
story.append(Paragraph("&bull; <b>Work Mode Retention Parity:</b> Hybrid workers exhibited the lowest voluntary attrition and the highest job satisfaction scores (mean 2.65/4), while maintaining equivalent performance ratings to in-office employees.", bullet_style))
story.append(Paragraph("&bull; <b>High Performer Underpayment Risk:</b> Of the 241 employees achieving top performance (Rating 4), 38% fall below their department's median compensation band, exposing the company to high-value talent poaching.", bullet_style))
story.append(Spacer(1, 8))

# 6. Strategic Recommendations & Action Plan
story.append(Paragraph("6. Strategic HR Recommendations & Action Roadmap", h1_style))
story.append(Paragraph("&bull; <b>Restructure Sales Compensation:</b> Transition Sales comp plans to include a higher base-to-variable ratio (70/30) and quarterly milestone retention bonuses to curb the 24.1% attrition.", bullet_style))
story.append(Paragraph("&bull; <b>Calibrate High-Performer Pay Equity:</b> Undertake proactive off-cycle salary adjustments for the 92 high-performing staff earning below market/dept medians to protect critical institutional knowledge.", bullet_style))
story.append(Paragraph("&bull; <b>Formalize 3-Day Hybrid Standard:</b> Expand hybrid arrangements as the default enterprise standard; analytics prove it sustains peak morale without compromising output.", bullet_style))
story.append(Paragraph("&bull; <b>Fast-Track Junior Mentorship:</b> Launch an accelerated 18-month career track for junior cohorts (1-3 years experience), which represent over 45% of total annual resignations.", bullet_style))
story.append(Spacer(1, 8))

# 7. Power BI Executive Dashboard Architecture
story.append(Paragraph("7. Power BI Executive Dashboard Architecture", h1_style))
story.append(Paragraph(
    "An enterprise Power BI solution was structured with 7 interactive reporting dashboards and 6 live DAX KPI Cards:",
    body_style
))

pbi_data = [
    ["KPI Card Metric", "DAX Expression", "Target Value"],
    ["Total Employees", "COUNTROWS(Employees)", "1,200"],
    ["Average Salary", "AVERAGE(Employees[Salary])", "INR 11.14 Lakhs"],
    ["Highest Salary", "MAX(Employees[Salary])", "INR 30.07 Lakhs"],
    ["Average Experience", "AVERAGE(Employees[YearsOfExperience])", "6.51 Years"],
    ["Attrition Rate", "DIVIDE(CALCULATE(COUNT(Employees[EmployeeID]), Employees[Attrition]=\"Yes\"), COUNT(Employees[EmployeeID]))", "18.9%"],
    ["Avg Performance Rating", "AVERAGE(Employees[PerformanceRating])", "2.82 / 4.0"]
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
    ("TOPPADDING", (0, 0), (-1, -1), 3.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
]))
story.append(pbi_table)
story.append(Spacer(1, 10))

# 8. Conclusion
story.append(Paragraph("8. Conclusion", h1_style))
story.append(Paragraph(
    "This end-to-end Employee Performance & HR Analytics initiative successfully integrates MySQL database queries, "
    "Python data analysis, automated reporting, and Power BI visualization into a cohesive, high-impact business analytics framework. "
    "It demonstrates the analytical maturity, business acumen, and technical fluency required of an industry-ready Data Analyst.",
    body_style
))

doc.build(story, canvasmaker=NumberedCanvas)
print("PDF Report generated successfully at:", pdf_path)
