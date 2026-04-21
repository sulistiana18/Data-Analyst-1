import pandas as pd

def split_tables(df_pekerja, df_pelatihan, df_kode_pelatihan):

    # =========================
    # DIM PEKERJA
    # =========================
    pekerja = df_pekerja[
        ["id_pekerja", "nama", "fungsi", "bagian", "gender"]
    ].drop_duplicates().reset_index(drop=True)

    # =========================
    # FACT PELATIHAN
    # =========================
    pelatihan = df_pelatihan[
        [
            "id_pekerja",
            "training_id",
            "jenis_pelatihan",
            "layering",
            "skill_group",
            "educational_establishment",
            "start_date",
            "end_date",
            "bulan",
            "lokasi",
            "dur",
            "status",
            "expire_date",
            "month_ed",
            "year_ed",
            "nama_lembaga_sertifikasi",
            "tgl_terima_sertifikat",
            "sumber_data"
        ]
    ].copy()
    
    # 🔥 NORMALISASI NULL DULU
    pelatihan = pelatihan.replace("NULL", pd.NA)
    pelatihan = pelatihan.replace("", pd.NA)

    # 🔥 HAPUS DUPLIKAT
    pelatihan = pelatihan.drop_duplicates()

    # 🔥 HAPUS ROW YANG BENAR-BENAR KOSONG
    pelatihan = pelatihan.dropna(how='all')

    # 🔥 RESET INDEX
    pelatihan = pelatihan.reset_index(drop=True)

    # 🔥 GENERATE ET ID
    pelatihan.insert(0, "record_id", pelatihan.index + 1)
    pelatihan["record_id"] = pelatihan["record_id"].apply(lambda x: f"ET{x:05}")



    # =========================
    # KODE PELATIHAN
    # =========================
    kode_pelatihan = df_kode_pelatihan.copy()

    return pekerja, pelatihan, kode_pelatihan