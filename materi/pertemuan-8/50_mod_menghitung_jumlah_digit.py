# CHALLENGE MODIFIKASI
# Langsung print jumlah digitnya dikali 10.

# Menghitung Jumlah Digit
# Tujuan: Menghitung berapa digit dalam sebuah angka (mengabaikan tanda minus)

angka = int(input("Masukkan angka: "))

# Ambil nilai absolut (hilangkan tanda negatif)
angka_absolut = abs(angka)

# Ubah ke string dan hitung panjangnya
jumlah_digit = len(str(angka_absolut))

# MODIFIKASI: Print jumlah digit dikali 10
print(f"Angka {angka} memiliki {jumlah_digit} digit, dikali 10 = {jumlah_digit * 10}.")
