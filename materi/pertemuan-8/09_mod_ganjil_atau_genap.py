# CHALLENGE MODIFIKASI
# Ubah logikanya jadi cek apakah angka habis dibagi 3 atau tidak.

# Ganjil atau Genap?
# Tujuan: Menentukan apakah sebuah angka ganjil atau genap

angka = int(input("Masukkan angka: "))

# MODIFIKASI: Cek apakah habis dibagi 3
if angka % 3 == 0:
    print(f"{angka} habis dibagi 3.")
else:
    print(f"{angka} tidak habis dibagi 3.")
