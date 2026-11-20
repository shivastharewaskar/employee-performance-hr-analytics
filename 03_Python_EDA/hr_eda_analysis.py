# ==============================================================================
# Student Name: Shivastha Rewaskar
# Project: Employee Performance & HR Analytics
# GitHub Repository: https://github.com/shivastharewaskar/employee-performance-hr-analytics
# Script: hr_eda_analysis.py - Exploratory Data Analysis & Cleaning with Pandas
# ==============================================================================

import pandas as pd
import numpy as np
import os

def run_eda():
    print("Starting HR Employee Analytics EDA Pipeline...")
    print("Candidate: Shivastha Rewaskar")
    print("GitHub: https://github.com/shivastharewaskar/employee-performance-hr-analytics\n")
    
    # 1. Load the raw dataset
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "01_Dataset", "employee_data_raw.csv")
    clean_path = os.path.join(base_dir, "01_Dataset", "employee_data_cleaned.csv")
    
    df = pd.read_csv(raw_path)
    print(f"Loaded raw dataset from {raw_path}")
    print(f"Initial shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    
    # 2. Inspect column types
    print("Column Data Types:")
    print(df.dtypes)
    print("\nFirst 3 rows:")
    print(df.head(3))
    
    # 3. Handle missing values
    print("\nChecking for missing values:")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0])
    
    # Impute missing salary with the median salary of each department
    if df['Salary'].isnull().sum() > 0:
        df['Salary'] = df.groupby('Department')['Salary'].transform(lambda s: s.fillna(s.median()))
        print("-> Imputed missing salaries with department medians.")
        
    # Impute missing work mode with modal value
    if df['WorkMode'].isnull().sum() > 0:
        mode_workmode = df['WorkMode'].mode()[0]
        df['WorkMode'] = df['WorkMode'].fillna(mode_workmode)
        print(f"-> Imputed missing work modes with mode ('{mode_workmode}').")
        
    # 4. Remove duplicates
    duplicates_count = df.duplicated(subset=['EmployeeID']).sum()
    print(f"\nFound {duplicates_count} duplicate employee records.")
    if duplicates_count > 0:
        df = df.drop_duplicates(subset=['EmployeeID'], keep='first')
        print(f"Cleaned shape after deduplication: {df.shape}")
        
    # Save the cleaned dataset
    df.to_csv(clean_path, index=False)
    print(f"Cleaned dataset saved to {clean_path}\n")
    
    # 5. Descriptive statistics
    print("Descriptive Statistics for Numerical Columns:")
    num_cols = ['Age', 'YearsOfExperience', 'YearsAtCompany', 'Salary', 'PerformanceRating', 'JobSatisfaction', 'WorkLifeBalance']
    stats = df[num_cols].describe().T[['mean', 'std', 'min', '50%', 'max']].round(2)
    print(stats)
    
    # 6. Salary distribution summary
    print(f"\nAverage Salary: ₹{df['Salary'].mean():,.2f}")
    print(f"Median Salary:  ₹{df['Salary'].median():,.2f}")
    print(f"Salary Std Dev: ₹{df['Salary'].std():,.2f}")
    print(f"Salary Skewness: {df['Salary'].skew():.2f}")
    
    # 7. Department breakdown
    print("\nDepartment Summary (Headcount & Attrition):")
    dept_grp = df.groupby('Department').agg(
        TotalEmployees=('EmployeeID', 'count'),
        AvgSalary=('Salary', 'mean'),
        AvgExperience=('YearsOfExperience', 'mean'),
        AttritionRate=('Attrition', lambda x: (x == 'Yes').mean() * 100)
    ).round(2)
    print(dept_grp)
    
    # 8. Education vs Salary
    print("\nAverage Salary by Education Level:")
    edu_grp = df.groupby('Education')['Salary'].agg(['count', 'mean', 'median']).round(2)
    print(edu_grp)
    
    # 9. Correlation between Experience & Salary
    corr = df['YearsOfExperience'].corr(df['Salary'])
    print(f"\nCorrelation between Experience and Salary: {corr:.4f}")
    
    # 10. Work mode breakdown
    print("\nWork Mode Distribution:")
    mode_grp = df.groupby('WorkMode').agg(
        Count=('EmployeeID', 'count'),
        AvgSatisfaction=('JobSatisfaction', 'mean'),
        AvgPerformance=('PerformanceRating', 'mean'),
        AttritionRate=('Attrition', lambda x: (x == 'Yes').mean() * 100)
    ).round(2)
    print(mode_grp)
    
    # 11. Gender diversity and pay
    print("\nGender Distribution and Pay Parity:")
    gender_grp = df.groupby('Gender').agg(
        Count=('EmployeeID', 'count'),
        AvgSalary=('Salary', 'mean'),
        AvgPerformance=('PerformanceRating', 'mean')
    ).round(2)
    print(gender_grp)
    
    # 12. Correlation Matrix
    print("\nCorrelation Matrix:")
    print(df[num_cols].corr().round(3))
    
    print("\nEDA Completed successfully!")

if __name__ == '__main__':
    run_eda()
