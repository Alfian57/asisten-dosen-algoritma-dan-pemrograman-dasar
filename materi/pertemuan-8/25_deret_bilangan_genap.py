# Deret Bilangan Genap
# Tujuan: Menampilkan bilangan genap dari 1 sampai N

n = int(input("Masukkan angka maksimal (N): "))

print("Bilangan genap dari 1 sampai", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()
