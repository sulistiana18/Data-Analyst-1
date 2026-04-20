def split_tables(df_pekerja, df_pelatihan):

    # df = df.copy()

    # =========================
    # DIM PEKERJA
    # =========================
    pekerja = df_pekerja[
        ["bagian", "fungsi", "nama", "nopek"]
    ].drop_duplicates().reset_index(drop=True)

    # =========================
    # DIM PELATIHAN
    # =========================
    pelatihan = df_pelatihan[
        ["training_id", "nama_pelatihan", "jenis_pelatihan", "skill_group",]
    ].drop_duplicates().reset_index(drop=True)

    # =========================
    # FACT TABLE
    # =========================
    training_record = df_pelatihan[
        [
            "id_pekerja",
            "training_id",
            "start_date",
            "end_date",
            "bulan",
            "lokasi",
            "dur",
            "status",
            "expire_date",
            "month_ed",
            "year_ed",
            "sumber_data"
        ]
    ].reset_index(drop=True)

    training_record.insert(0, "record_id", range(1, len(training_record) + 1))

    return pekerja, pelatihan, training_record