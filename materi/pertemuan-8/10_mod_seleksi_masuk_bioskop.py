# CHALLENGE MODIFIKASI
# Ubah syarat umur jadi >= 21 tahun.

# Seleksi Masuk Bioskop
# Tujuan: Mengecek apakah pengunjung boleh menonton film rating 17+

umur = int(input("Masukkan umur Anda: "))

# MODIFIKASI: Ubah syarat umur jadi >= 21
if umur >= 21:
    print("Boleh Masuk")
else:
    print("Dilarang Masuk")
