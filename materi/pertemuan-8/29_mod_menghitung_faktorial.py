# CHALLENGE MODIFIKASI
# Tampilkan proses perkaliannya (print angka i di dalam loop).

# Menghitung Faktorial
# Tujuan: Menghitung N! (Faktorial)

n = int(input("Masukkan bilangan bulat N: "))

faktorial = 1
for i in range(n, 0, -1):
    # MODIFIKASI: Tampilkan proses perkalian
    print(f"Mengalikan dengan: {i}")
    faktorial *= i

print(f"Faktorial dari {n} adalah {faktorial}.")
