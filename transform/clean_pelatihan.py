def clean_pelatihan(df):
    # =========================
    # HEADER DI BARIS KE-4
    # =========================
    df = df.iloc[3:].reset_index(drop=True)
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    # =========================
    # CLEAN HEADER
    # =========================
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.replace(r"[^\w]", "_", regex=True)  # hapus simbol aneh
        .str.replace("__+", "_", regex=True)     # double underscore
        .str.lower()
    )

    # =========================
    # FIX NAMA KOLOM JELEK
    # =========================
    rename_map = {
        "valid_for_'year": "valid_for_year",
        "nama_lembaga_provider_sertifikasi": "nama_lembaga_sertifikasi",
        "tgl_terima__sertifikat": "tgl_terima_sertifikat"
    }

    df = df.rename(columns=rename_map)

    # =========================
    # CLEAN DATA
    # =========================
    df = df.fillna("NULL")
    df = df.replace(r'^\s*$', "NULL", regex=True)

    df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

    # =========================
    # DROP KOLOM 100% NULL
    # =========================
    df = df.loc[:, (df != "NULL").any()]

    return df