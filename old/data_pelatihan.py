import pandas as pd

# =========================
# 1. LOAD DATA (RAW)
# =========================
df = pd.read_excel("Data.xlsx", sheet_name="Data Pelatihan", header=None)

print("=== RAW DATA ===")
print(df.head())


# =========================
# 2. CEK NULL (OPTIONAL DEBUG)
# =========================
print("\n=== NULL COUNT ===")
print(df.isnull().sum())


# =========================
# 3. LIHAT HEADER (BARIS 4)
# =========================
row4 = df.iloc[3].tolist()
print("\n=== HEADER BARIS 4 ===")
print(row4)


# =========================
# 4. DROP BARIS DI ATAS HEADER
# =========================
df = df.iloc[3:].reset_index(drop=True)


# =========================
# 5. SET HEADER
# =========================
df.columns = df.iloc[0]


# =========================
# 6. HAPUS BARIS HEADER DARI DATA
# =========================
df = df[1:].reset_index(drop=True)


# =========================
# 7. CLEAN HEADER (SPASI → UNDERSCORE + LOWERCASE)
# =========================
df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.replace(" ", "_")
    .str.lower()
)


# =========================
# 8. CLEAN DATA
# =========================
df = df.fillna("NULL")

df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))


# =========================
# 🔥 8B. DROP KOLOM 100% KOSONG (INI TAMBAHAN)
# =========================

# normalisasi kosong (kalau ada spasi doang)
df = df.replace(r'^\s*$', "NULL", regex=True)

# cek kolom yang akan dihapus
empty_cols = df.columns[(df == "NULL").all()]

print("\n🗑️ KOLOM DIHAPUS (100% KOSONG):")
print(empty_cols.tolist())

# drop kolom
df = df.loc[:, (df != "NULL").any()]


# =========================
# 9. BASIC AUDIT
# =========================
print("\n📊 NULL COUNT:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# =========================
# 9B. FULL DATA AUDIT
# =========================
print("\n📊 DATA OVERVIEW")
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))


# =========================
# CEK TIPE DATA
# =========================
print("\n📌 DATA TYPES:")
print(df.dtypes)


# =========================
# CEK UNIQUE VALUE
# =========================
print("\n📌 UNIQUE VALUE SAMPLE:")
for col in df.columns[:10]:
    print(f"{col}: {df[col].nunique()}")


# =========================
# CEK NUMERIC SUMMARY
# =========================
print("\n📌 NUMERIC SUMMARY:")
print(df.describe())


# =========================
# CEK DISTRIBUSI DATA KATEGORI
# =========================
print("\n📌 SAMPLE DISTRIBUTION:")

sample_cols = [
    col for col in df.columns
    if "status" in col.lower() or "pelatihan" in col.lower()
]

for col in sample_cols:
    print(f"\n{col}:")
    print(df[col].value_counts().head())


# =========================
# CEK UNKNOWN (HASIL CLEANING)
# =========================
print("\n📌 CEK 'Unknown':")
unknown_counts = (df == "Unknown").sum()
print(unknown_counts[unknown_counts > 0])


# =========================
# 9C. CEK "NULL" STRING
# =========================
print("\n📌 CEK 'NULL' STRING:")
null_string_counts = (df == "NULL").sum()
print(null_string_counts[null_string_counts > 0])


# =========================
# 9D. KOLOM DOMINAN NULL
# =========================
print("\n📊 KOLOM DOMINAN NULL:")
threshold = 0.5

for col in df.columns:
    ratio = (df[col] == "NULL").sum() / len(df)
    if ratio > threshold:
        print(f"{col}: {round(ratio*100,2)}% NULL")


# =========================
# 9E. DUPLICATE PER KOLOM
# =========================
print("\n📊 DUPLICATE PER KOLOM:")

for col in df.columns:
    dup = df[col].duplicated().sum()
    if dup > 0:
        print(f"{col}: {dup}")


# =========================
# 9F. SAMPLE VALUE ANEH
# =========================
print("\n📌 SAMPLE VALUE ANEH:")

for col in df.select_dtypes(include=["object", "string"]).columns[:5]:
    print(f"\n{col}:")
    print(df[col].unique()[:5])


# =========================
# 9G. CEK SPASI TERSEMBUNYI
# =========================
print("\n📌 CEK SPASI TERSEMBUNYI:")

for col in df.select_dtypes(include=["object", "string"]).columns:
    count = df[col].astype(str).str.startswith(" ").sum() + df[col].astype(str).str.endswith(" ").sum()
    if count > 0:
        print(f"{col}: {count} value masih ada spasi")


# =========================
# 9H. CEK POTENSI PRIMARY KEY
# =========================
print("\n📌 POTENSI PRIMARY KEY:")

for col in df.columns:
    if df[col].nunique() == len(df):
        print(f"{col} → kandidat PRIMARY KEY")


# =========================
# DATA COMPLETENESS SCORE
# =========================
total_cells = df.shape[0] * df.shape[1]
missing_cells = ((df == "NULL") | (df.isnull())).sum().sum()

completeness = 1 - (missing_cells / total_cells)

print("\n📊 DATA COMPLETENESS:", round(completeness * 100, 2), "%")


# =========================
# OPTIONAL: FLAG DATA ISSUE
# =========================
df["data_issue"] = df.isnull().any(axis=1)


# =========================
# 10. EXPORT CSV
# =========================
df.to_csv("data_pelatihan.csv", index=False)

print("\nDONE - CLEAN + DROP KOLOM KOSONG + FULL AUDIT")