def clean_kode_pelatihan(df):
    df = df.copy()

    # langsung rapihin nama kolom saja
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.replace(r"[^\w]", "_", regex=True)
        .str.replace("__+", "_", regex=True)
        .str.lower()
    )

    return df