import pandas as pd 

file = 'Data.xlsx'

# Load Data Pelatihan
Data_Pelatihan = pd.read_excel(file, sheet_name='Data Pelatihan')

# Load Data blm update SAP
need_updt = pd.read_excel(file, sheet_name='need update SAP')

# Load Data Pekerja
data_pekerja = pd.read_excel(file, sheet_name='data')

# Olah Sheet Data Pelatihan
   
#print(Data_Pelatihan.head(5)) # Menampilkan 5 baris pertama dari Data Pelatihan

# menampilkan semua nama kolom (di baris 1) dari Data Pelatihan
#print(Data_Pelatihan.columns)

# info dari Data Pelatihan kolom yang ada, jumlah data, tipe data, dan penggunaan memori
#print(Data_Pelatihan.info())

# karena tidak ditemukan header pada baris pertama maka kita akan cek kembali
#print(Data_Pelatihan.head(10)) # Menampilkan 5 baris pertama dari Data Pelatihan

# setelah ditemukan header ada di baris ke empat:
print(Data_Pelatihan.iloc[2]) # Menampilkan baris keempat dari Data Pelatihan