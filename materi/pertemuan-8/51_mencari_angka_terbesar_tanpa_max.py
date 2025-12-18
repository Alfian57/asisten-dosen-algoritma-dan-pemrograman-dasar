# Mencari Angka Terbesar (Tanpa Max)
# Tujuan: Mencari angka terbesar dari inputan user

n = int(input("Berapa banyak angka yang akan diinput? "))

# Input pertama sebagai angka terbesar sementara
angka_max = int(input(f"Masukkan angka ke-1: "))

# Loop untuk sisa input
for i in range(2, n + 1):
    angka = int(input(f"Masukkan angka ke-{i}: "))
    if angka > angka_max:
        angka_max = angka

print(f"Angka terbesar adalah: {angka_max}")
