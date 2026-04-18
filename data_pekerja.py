import pandas as pd

df = pd.read_excel("Data.xlsx", sheet_name="data", header=None)

# =========================
# 1. FILL MERGE (WAJIB)
# =========================
df = df.ffill(axis=0)   # vertical merge
df = df.ffill(axis=1)   # horizontal merge


# =========================
# 2. AMBIL HEADER (2 BARIS)
# =========================
h1 = df.iloc[1]
h2 = df.iloc[2]


# =========================
# 3. BUILD FLAT HEADER (CORE LOGIC KAMU)
# =========================
cols = []

for a, b in zip(h1, h2):

    a = str(a).strip()
    b = str(b).strip()

    # kalau sama → cukup 1
    if a == b:
        col = a

    # kalau salah satu kosong
    elif a.lower() in ["nan", "unknown", ""]:
        col = b
    elif b.lower() in ["nan", "unknown", ""]:
        col = a

    # kalau dua-duanya ada
    else:
        col = f"{a}_{b}"

    cols.append(col)


# =========================
# 4. FIX DUPLICATE COLUMN NAME
# =========================
df.columns = pd.io.common.dedup_names(cols, is_potential_multiindex=False)


# =========================
# 5. DROP HEADER ROW
# =========================
df = df.iloc[3:].reset_index(drop=True)


# =========================
# 6. CLEAN FINAL
# =========================
df = df.fillna("Unknown")
df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))


# =========================
# 7. RESULT
# =========================
print(df.head())

df.to_csv("data_clean.csv", index=False)

print("DONE - HEADER SUDAH FLATTEN")