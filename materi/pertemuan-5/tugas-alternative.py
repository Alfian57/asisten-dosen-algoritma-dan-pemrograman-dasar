print("=========")
print("Faktorial")
print("=========\n")
angka = int(input("Masukkan angka: "))

if angka < 0:
    print("Faktorial tidak terdefinisi untuk bilangan negatif.")

else:
    hasil = 1
    for i in range(angka, 0, -1):
        hasil = hasil * i

    print(f"\nFaktorial dari {angka} adalah {hasil}")