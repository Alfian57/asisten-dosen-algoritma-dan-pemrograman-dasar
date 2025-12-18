# CHALLENGE MODIFIKASI
# Ganti karakter bintang * jadi tanda pagar #.

# Pola Segitiga Bintang Terbalik
# Tujuan: Membuat pola bintang menurun

tinggi = int(input("Masukkan tinggi segitiga: "))

# MODIFIKASI: Ganti * jadi #
for i in range(tinggi, 0, -1):
    for j in range(i):
        print("#", end="")
    print()
