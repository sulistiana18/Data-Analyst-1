import pandas as pd

file = 'Data.xlsx'

data_pekerja = pd.read_excel(file, sheet_name='data')

print(data_pekerja.head(5))

print(data_pekerja.info)

print(data_pekerja.describe)

