# CHALLENGE MODIFIKASI
# Ubah jadi cek Segitiga Sama Sisi. Valid jika Sisi A == Sisi B == Sisi C.

# Validasi Segitiga
# Tujuan: Mengecek apakah 3 sisi bisa membentuk segitiga

sisi_a = float(input("Masukkan sisi A: "))
sisi_b = float(input("Masukkan sisi B: "))
sisi_c = float(input("Masukkan sisi C: "))

# MODIFIKASI: Cek segitiga sama sisi
if sisi_a == sisi_b == sisi_c:
    print("Segitiga Sama Sisi")
else:
    print("Bukan Segitiga Sama Sisi")
