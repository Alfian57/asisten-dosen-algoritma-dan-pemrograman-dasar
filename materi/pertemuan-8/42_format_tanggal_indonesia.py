# Format Tanggal Indonesia
# Tujuan: Menampilkan tanggal dengan nama bulan

nama_bulan = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}

tanggal = int(input("Masukkan tanggal: "))
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

print(f"{tanggal} {nama_bulan[bulan]} {tahun}")
