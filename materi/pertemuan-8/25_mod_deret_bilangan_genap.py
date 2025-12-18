# CHALLENGE MODIFIKASI
# Ubah jadi deret bilangan Ganjil (1, 3, 5...).

# Deret Bilangan Genap
# Tujuan: Menampilkan bilangan genap dari 1 sampai N

n = int(input("Masukkan angka maksimal (N): "))

# MODIFIKASI: Ubah jadi deret bilangan ganjil
print("Bilangan ganjil dari 1 sampai", n, ":")
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i, end=" ")
print()
