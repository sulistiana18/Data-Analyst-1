from extract.load_excel import load_sheet
from transform.clean_pekerja import clean_pekerja
from transform.clean_pelatihan import clean_pelatihan
from transform.clean_kode_pelatihan import clean_kode_pelatihan
from transform.split_tables import split_tables
from load.export_csv import export_csv

FILE_PATH = "Data.xlsx"


def print_columns(title, df):
    print(f"\n📌 KOLOM {title}:")
    for i, col in enumerate(df.columns):
        print(f"{i}. {col}")


def print_sample(title, df):
    print(f"\n📊 SAMPLE {title}:")
    print(df.head(3))


def main():
    # =========================
    # LOAD
    # =========================
    df_pekerja_raw = load_sheet(FILE_PATH, "Data Pekerja", header=None)
    df_pelatihan_raw = load_sheet(FILE_PATH, "Data Pelatihan", header=None)
    df_kode_pelatihan_raw = load_sheet(FILE_PATH, "Kode Pelatihan", header=0)

    print("✅ Load selesai")

    # =========================
    # CLEAN
    # =========================
    df_pekerja = clean_pekerja(df_pekerja_raw)
    df_pelatihan = clean_pelatihan(df_pelatihan_raw)
    df_kode_pelatihan = clean_kode_pelatihan(df_kode_pelatihan_raw)

    print("✅ Cleaning selesai")

    # =========================
    # PRINT KOLOM
    # =========================
    print_columns("DATA PEKERJA", df_pekerja)
    print_columns("DATA PELATIHAN", df_pelatihan)
    print_columns("KODE PELATIHAN", df_kode_pelatihan)

    # =========================
    # PRINT SAMPLE
    # =========================
    print_sample("DATA PEKERJA", df_pekerja)
    print_sample("DATA PELATIHAN", df_pelatihan)
    print_sample("DATA KODE PELATIHAN", df_kode_pelatihan)

    # =========================
    # SPLIT (KE DEPAN UNTUK SQL)
    # =========================
    pekerja, pelatihan, kode_pelatihan = split_tables(df_pekerja, df_pelatihan, df_kode_pelatihan)
    
    ''' # CEK DUPLIKAT DIMANA SAJA
    print("\n jumlah duplicate di pelatihan ", pelatihan.duplicated().sum())
    dup = pelatihan[pelatihan.duplicated(keep=False)]
    
    print(dup)
    '''

    print("\n✅ Split tabel selesai")

    # =========================
    # EXPORT
    # =========================
    export_csv(pekerja, pelatihan, kode_pelatihan)


if __name__ == "__main__":
    main()