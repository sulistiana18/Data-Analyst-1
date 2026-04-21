def export_csv(pekerja, pelatihan, kode_pelatihan):
    pekerja.to_csv("clean_pekerja.csv", index=False)
    pelatihan.to_csv("clean_pelatihan.csv", index=False)
    kode_pelatihan.to_csv("kode_pelatihan.csv", index=False)

    print("✅ Export CSV selesai")