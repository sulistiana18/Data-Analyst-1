import pandas as pd

df = pd.read_excel("Data.xlsx", sheet_name="Data Pekerja", header=None)

# =========================
# 1. AMBIL HEADER DULU (JANGAN FILL DULU)
# =========================
h1 = df.iloc[1]
h2 = df.iloc[2]


# =========================
# 2. FILL KHUSUS HEADER SAJA (Bukan seluruh data)
# =========================
h1 = h1.ffill()
h2 = h2.ffill()


# =========================
# 3. BUILD HEADER FINAL
# =========================
cols = []

for a, b in zip(h1, h2):

    a = "" if pd.isna(a) else str(a).strip()
    b = "" if pd.isna(b) else str(b).strip()

    if a.lower() in ["nan", "unknown"]:
        a = ""
    if b.lower() in ["nan", "unknown"]:
        b = ""

    if a and b:
        col = f"{a}_{b}"
    elif a:
        col = a
    elif b:
        col = b
    else:
        col = "Unknown"

    cols.append(col)


# =========================
# 4. SET COLUMN
# =========================
df.columns = pd.io.common.dedup_names(cols, is_potential_multiindex=False)


# =========================
# 5. DROP HEADER ROWS
# =========================
df = df.iloc[3:].reset_index(drop=True)


# =========================
# 6. CLEAN DATA (ONLY DATA, NOT HEADER)
# =========================
df = df.fillna("Unknown")

df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))


# =========================
# 7. CLEAN HEADER SPASI → UNDERSCORE
# =========================
df.columns = [
    str(col).strip().replace(" ", "_").lower()
    for col in df.columns
]

print(df.head())


# =========================
# OPTIONAL: ANONYMIZE NAMA (DISABLE SEKARANG)
# =========================
'''
col_index = 7

df.iloc[:, col_index] = df.iloc[:, col_index].astype(str)

df.iloc[:, col_index] = [
    f"employee_name_{i+1}" for i in range(len(df))
]
'''


# =========================
# 8. BASIC AUDIT
# =========================
print("\n📊 NULL COUNT:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# =========================
# 8B. FULL DATA AUDIT (TAMBAHAN)
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
    if "status" in col.lower() or "bagian" in col.lower()
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
# DATA COMPLETENESS SCORE
# =========================
total_cells = df.shape[0] * df.shape[1]
missing_cells = df.isnull().sum().sum()

completeness = 1 - (missing_cells / total_cells)

print("\n📊 DATA COMPLETENESS:", round(completeness * 100, 2), "%")


# =========================
# OPTIONAL: FLAG DATA ISSUE
# =========================
df["data_issue"] = df.isnull().any(axis=1)


# =========================
# 9. EXPORT (PALING AKHIR)
# =========================
df.to_csv("data_pekerja.csv", index=False)

print("\nDONE - STABLE + CLEAN + FULL AUDIT")