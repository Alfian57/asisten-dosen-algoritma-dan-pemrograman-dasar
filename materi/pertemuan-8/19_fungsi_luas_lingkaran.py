# Fungsi Luas Lingkaran
# Tujuan: Menghitung luas lingkaran menggunakan fungsi

def luas_lingkaran(r):
    return 3.14 * r * r

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
hasil = luas_lingkaran(jari_jari)

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {hasil}.")
