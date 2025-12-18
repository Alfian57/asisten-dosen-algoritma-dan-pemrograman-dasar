# CHALLENGE MODIFIKASI
# Tambah konversi ke Minggu (1 minggu = 7 hari).

# Penghitung Detik
# Tujuan: Mengubah satuan jam menjadi total detik

jumlah_jam = int(input("Masukkan jumlah jam: "))

total_detik = jumlah_jam * 3600

print(f"{jumlah_jam} jam sama dengan {total_detik} detik.")

# MODIFIKASI: Tambah konversi ke minggu
total_hari = jumlah_jam / 24
total_minggu = total_hari / 7
print(f"{jumlah_jam} jam sama dengan {total_hari:.2f} hari.")
print(f"{jumlah_jam} jam sama dengan {total_minggu:.2f} minggu.")
