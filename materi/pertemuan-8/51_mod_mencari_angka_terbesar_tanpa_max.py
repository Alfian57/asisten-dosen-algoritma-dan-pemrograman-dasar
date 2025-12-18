# CHALLENGE MODIFIKASI
# Ubah logikanya untuk mencari angka Terkecil (Min).

# Mencari Angka Terbesar (Tanpa Max)
# Tujuan: Mencari angka terbesar dari inputan user

n = int(input("Berapa banyak angka yang akan diinput? "))

# MODIFIKASI: Input pertama sebagai angka terkecil sementara
angka_min = int(input(f"Masukkan angka ke-1: "))

# Loop untuk sisa input
for i in range(2, n + 1):
    angka = int(input(f"Masukkan angka ke-{i}: "))
    # MODIFIKASI: Ubah logika untuk mencari terkecil
    if angka < angka_min:
        angka_min = angka

print(f"Angka terkecil adalah: {angka_min}")
