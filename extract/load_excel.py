import pandas as pd

def load_sheet(file_path, sheet_name, header=0):
    return pd.read_excel(file_path, sheet_name=sheet_name, header=header)