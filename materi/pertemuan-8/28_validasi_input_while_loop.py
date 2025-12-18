# Validasi Input (While Loop)
# Tujuan: Meminta user memasukkan angka positif

while True:
    angka = int(input("Masukkan angka positif: "))
    
    if angka < 0:
        print("Angka harus positif! Coba lagi.")
    else:
        print("Terima kasih, Anda memasukkan angka positif.")
        break
