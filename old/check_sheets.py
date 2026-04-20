import pandas as pd

file = "Data.xlsx"

excel_file = pd.ExcelFile(file)

print(excel_file.sheet_names)