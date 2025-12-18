# CHALLENGE MODIFIKASI
# Ubah hitung mundurnya jadi lompat 2 angka (10, 8, 6...).

# Hitung Mundur Roket
# Tujuan: Simulasi hitung mundur peluncuran

angka_mulai = int(input("Masukkan angka mulai hitung mundur: "))

# MODIFIKASI: Ubah step jadi -2 (lompat 2)
for i in range(angka_mulai, 0, -2):
    print(i)

print("Meluncur!")
