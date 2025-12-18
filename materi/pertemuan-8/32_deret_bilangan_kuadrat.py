# Deret Bilangan Kuadrat
# Tujuan: Menampilkan deret angka hasil pemangkatan dua (kuadrat)

n = int(input("Masukkan jumlah bilangan (N): "))

print("Deret bilangan kuadrat:")
for i in range(1, n + 1):
    kuadrat = i ** 2
    print(kuadrat, end=" ")
print()
