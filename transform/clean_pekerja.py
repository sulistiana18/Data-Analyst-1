def clean_pekerja(df):
    # ambil header multi-row
    h1 = df.iloc[1].ffill()
    h2 = df.iloc[2].ffill()

    cols = []
    for a, b in zip(h1, h2):
        a = "" if str(a).lower() in ["nan", "unknown"] else str(a).strip()
        b = "" if str(b).lower() in ["nan", "unknown"] else str(b).strip()

        if a and b:
            col = f"{a}_{b}"
        elif a:
            col = a
        elif b:
            col = b
        else:
            col = "unknown"

        cols.append(col)

    df.columns = cols

    # drop header
    df = df.iloc[3:].reset_index(drop=True)

    # clean
    df = df.fillna("NULL")
    df = df.replace(r'^\s*$', "NULL", regex=True)

    df.columns = [
        str(col).strip().replace(" ", "_").lower()
        for col in df.columns
    ]

    # drop kolom kosong
    df = df.loc[:, (df != "NULL").any()]

    return df