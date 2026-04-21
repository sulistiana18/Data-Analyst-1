CREATE TABLE pekerja (
    id_pekerja VARCHAR(50) PRIMARY KEY,
    nama TEXT,
    fungsi TEXT,
    bagian TEXT,
    gender TEXT
);

CREATE TABLE kode_pelatihan (
    training_id VARCHAR(50),
    nama_pelatihan TEXT,
    jenis_pelatihan TEXT,

);

CREATE TABLE pelatihan (
    record_id VARCHAR(10) PRIMARY KEY,

    id_pekerja VARCHAR(50),
    training_id VARCHAR(50),
    jenis_pelatihan TEXT,

    layering TEXT,
    skill_group TEXT,
    educational_establishment TEXT,

    start_date DATE,
    end_date DATE,
    bulan VARCHAR(20),
    lokasi TEXT,
    dur INTEGER,
    status TEXT,

    expire_date DATE,
    month_ed INTEGER,
    year_ed INTEGER,

    nama_lembaga_sertifikasi TEXT,
    tgl_terima_sertifikat DATE,
    sumber_data TEXT,

    -- 🔗 RELASI KE PEKERJA
    FOREIGN KEY (id_pekerja)
        REFERENCES pekerja(id_pekerja),

    -- 🔗 RELASI KE KODE PELATIHAN (COMPOSITE)
    --FOREIGN KEY (training_id)
        --REFERENCES kode_pelatihan(training_id)
);