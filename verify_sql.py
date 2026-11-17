import sqlite3, pandas as pd, os
base_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(base_dir, '01_Dataset', 'employee_data_cleaned.csv')
df = pd.read_csv(data_file)
conn = sqlite3.connect(':memory:')
df.to_sql('employees', conn, index=False)
sql_file = os.path.join(base_dir, '02_SQL_Analysis', 'hr_analytics_schema_and_queries.sql')
with open(sql_file, 'r', encoding='utf-8') as f:
    stmts = [s.strip() for s in f.read().split(';') if s.strip() and 'SELECT' in s.upper()]
for idx, s in enumerate(stmts, 1):
    clean = '
'.join([l for l in s.splitlines() if not l.strip().startswith('--')])
    if clean.strip():
        res = pd.read_sql(clean, conn)
        print(f'Query {idx}: OK ({len(res)} rows)')
print('All SQL queries passed verification!')
