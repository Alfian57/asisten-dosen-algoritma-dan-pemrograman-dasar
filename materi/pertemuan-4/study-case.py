def penjumlahan(angka_pertama, angka_kedua):
    hasil = angka_pertama + angka_kedua
    return hasil

def pengurangan(angka_pertama, angka_kedua):
    hasil = angka_pertama - angka_kedua
    return hasil

def perkalian(angka_pertama, angka_kedua):
    hasil = angka_pertama * angka_kedua
    return hasil

def pembagian(angka_pertama, angka_kedua):
    hasil = angka_pertama / angka_kedua
    return hasil

print("===== Kalkulator Sederhana =====")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
menu = input("Pilih operasi [1-4] : ")

if menu == "1":
    angka_pertama = float(input("Masukan angka pertama : "))
    angka_kedua = float(input("Masukan angka kedua : "))
    hasil = penjumlahan(angka_pertama, angka_kedua)
    print("Hasil Penjumlahan: " + str(hasil))

elif menu == "2":
    angka_pertama = float(input("Masukan angka pertama : "))
    angka_kedua = float(input("Masukan angka kedua : "))
    hasil = pengurangan(angka_pertama, angka_kedua)
    print("Hasil pengurangan: " + str(hasil))

elif menu == "3":
    angka_pertama = float(input("Masukan angka pertama : "))
    angka_kedua = float(input("Masukan angka kedua : "))
    hasil = perkalian(angka_pertama, angka_kedua)
    print("Hasil perkalian: " + str(hasil))

elif menu == "4":
    angka_pertama = float(input("Masukan angka pertama : "))
    angka_kedua = float(input("Masukan angka kedua : "))
    hasil = pembagian(angka_pertama, angka_kedua)
    print("Hasil pembagian: " + str(hasil))

else:
    print("Operasi tidak dikenal.")

