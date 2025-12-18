# CHALLENGE MODIFIKASI
# Hitung penjumlahannya mulai dari angka 10 sampai N. Bukan dari 1.

# Penjumlah Angka (Sum of N)
# Tujuan: Menjumlahkan angka dari 1 sampai N

n = int(input("Masukkan angka N: "))

total = 0
# MODIFIKASI: Mulai dari 10 sampai N
for i in range(10, n + 1):
    total += i

print(f"Total penjumlahan: {total}.")
