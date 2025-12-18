# Menghitung Jumlah Digit
# Tujuan: Menghitung berapa digit dalam sebuah angka (mengabaikan tanda minus)

angka = int(input("Masukkan angka: "))

# Ambil nilai absolut (hilangkan tanda negatif)
angka_absolut = abs(angka)

# Ubah ke string dan hitung panjangnya
jumlah_digit = len(str(angka_absolut))

print(f"Angka {angka} memiliki {jumlah_digit} digit.")
