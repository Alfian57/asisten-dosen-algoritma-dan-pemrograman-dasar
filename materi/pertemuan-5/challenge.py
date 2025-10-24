print("\nProgram Bilangan Ganjil")
angka = int(input("Masukkan sebuah angka: "))

for i in range(1, angka + 1):
    if i % 2 != 0:
        print(i)