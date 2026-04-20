def export_csv(pekerja, pelatihan, training_record):
    pekerja.to_csv("dim_pekerja.csv", index=False)
    pelatihan.to_csv("dim_pelatihan.csv", index=False)
    training_record.to_csv("fact_training.csv", index=False)

    print("✅ Export CSV selesai")