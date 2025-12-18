# Menghitung Faktorial
# Tujuan: Menghitung N! (Faktorial)

n = int(input("Masukkan bilangan bulat N: "))

faktorial = 1
for i in range(n, 0, -1):
    faktorial *= i

print(f"Faktorial dari {n} adalah {faktorial}.")
