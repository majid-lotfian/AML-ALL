import pandas as pd

file_path = r"I:\AML_ALL\Data\BC_labuitslag_13-04-2026.csv"

try:
    df = pd.read_excel(file_path, nrows=10)
    print("SUCCESS: It is actually an Excel file")
    print(df.head())
except Exception as e:
    print("FAILED:", e)
