import pandas as pd

# =========================
# 1. LOAD FILE
# =========================
file = "Data.xlsx"

try:
    df = pd.read_excel(file, sheet_name="data", header=None)
    print("✅ File berhasil dibaca (tanpa asumsi header)")
except Exception as e:
    print("❌ Gagal baca file:", e)
    exit()


# =========================
# 2. CEK STRUKTUR AWAL (RAW)
# =========================
print("\n📌 SHAPE DATA:", df.shape)

print("\n📌 SAMPLE DATA (RAW):")
print(df.head(10))


# =========================
# 3. DETEKSI HEADER OTOMATIS
# =========================
# cari baris yang paling banyak string (indikasi header)
row_scores = df.apply(lambda row: row.astype(str).str.contains(r'[A-Za-z]').sum(), axis=1)

header_row_index = row_scores.idxmax()

print(f"\n📌 Kandidat header di baris: {header_row_index}")

# set ulang header
df.columns = df.iloc[header_row_index]
df = df.drop(index=range(0, header_row_index + 1)).reset_index(drop=True)

print("\n✅ Header sudah diset otomatis")


# =========================
# 4. CEK DUPLIKASI / DATA KOTOR
# =========================
print("\n📌 CEK DUPLIKAT ROW:")
print(df.duplicated().sum())

df = df.drop_duplicates()


# =========================
# 5. CEK MERGED CELL / DATA KOSONG ANEH
# =========================
print("\n📌 CEK MISSING VALUE:")
print(df.isnull().sum())

# cek apakah ada pola merged cell (NaN panjang berurutan)
merged_detect = df.isnull().rolling(3).sum().max().max()

if merged_detect > 3:
    print("\n⚠️ Kemungkinan ada merged cell / data tidak rapi")
else:
    print("\n✅ Tidak terdeteksi merged cell signifikan")


# =========================
# 6. NORMALISASI DATA (AMAN UNTUK DB)
# =========================

# trim string
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace("nan", None)


# =========================
# 7. INFO FINAL (DATABASE READY CHECK)
# =========================
print("\n📌 FINAL INFO DATA:")
print(df.info())

print("\n📌 PREVIEW CLEAN DATA:")
print(df.head(10))


# =========================
# 8. EXPORT SIAP DATABASE
# =========================
output_file = "data_pekerja_clean.csv"
df.to_csv(output_file, index=False)

print(f"\n✅ Data siap database disimpan: {output_file}")