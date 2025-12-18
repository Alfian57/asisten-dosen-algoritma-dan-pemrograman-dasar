# CHALLENGE MODIFIKASI
# Ubah syaratnya. Minta user input angka Genap. Kalau Ganjil, minta input ulang.

# Validasi Input (While Loop)
# Tujuan: Meminta user memasukkan angka positif

# MODIFIKASI: Validasi untuk angka genap
while True:
    angka = int(input("Masukkan angka genap: "))
    
    if angka % 2 != 0:
        print("Angka harus genap! Coba lagi.")
    else:
        print("Terima kasih, Anda memasukkan angka genap.")
        break
