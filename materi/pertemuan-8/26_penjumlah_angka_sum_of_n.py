# Penjumlah Angka (Sum of N)
# Tujuan: Menjumlahkan angka dari 1 sampai N

n = int(input("Masukkan angka N: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"Total penjumlahan: {total}.")
