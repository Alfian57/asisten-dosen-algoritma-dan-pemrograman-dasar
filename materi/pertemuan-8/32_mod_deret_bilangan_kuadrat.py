# CHALLENGE MODIFIKASI
# Ganti jadi deret Pangkat Tiga (Kubik).

# Deret Bilangan Kuadrat
# Tujuan: Menampilkan deret angka hasil pemangkatan dua (kuadrat)

n = int(input("Masukkan jumlah bilangan (N): "))

# MODIFIKASI: Ganti jadi pangkat tiga (kubik)
print("Deret bilangan kubik:")
for i in range(1, n + 1):
    kubik = i ** 3
    print(kubik, end=" ")
print()
