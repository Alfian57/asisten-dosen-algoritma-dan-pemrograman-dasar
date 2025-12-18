# CHALLENGE MODIFIKASI
# Ubah fungsinya jadi menghitung Keliling Lingkaran (2 × π × r).

# Fungsi Luas Lingkaran
# Tujuan: Menghitung luas lingkaran menggunakan fungsi

# MODIFIKASI: Ubah fungsi untuk menghitung keliling
def keliling_lingkaran(r):
    return 2 * 3.14 * r

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
hasil = keliling_lingkaran(jari_jari)

print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah {hasil}.")
