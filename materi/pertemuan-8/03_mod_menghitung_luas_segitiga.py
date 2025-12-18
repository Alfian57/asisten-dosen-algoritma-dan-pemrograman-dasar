# CHALLENGE MODIFIKASI
# Hitung juga keliling segitiga (jumlah ketiga sisi).

# Menghitung Luas Segitiga
# Tujuan: Menghitung luas segitiga

alas = float(input("Masukkan alas segitiga (cm): "))
tinggi = float(input("Masukkan tinggi segitiga (cm): "))

luas = 0.5 * alas * tinggi

print(f"Luas segitiga adalah {luas} cm².")

# MODIFIKASI: Hitung keliling segitiga
# Untuk menghitung keliling, kita perlu sisi miring
sisi_c = float(input("Masukkan sisi miring segitiga (cm): "))
keliling = alas + tinggi + sisi_c
print(f"Keliling segitiga adalah {keliling} cm.")
