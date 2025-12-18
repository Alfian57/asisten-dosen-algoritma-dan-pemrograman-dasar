import kalkulator
from database import tambah_barang, list_barang

while True:
    print("===Kasir Sederhana===")
    print("1. Tambah barang")
    print("2. Kalkulator pembelian")
    menu = input("Masukan menu [1-2] : ")
    if menu == "1":
        tambah_barang()

    elif menu == "2":
        kalkulator.kalkulator_pembelian(list_barang)

    else:
        print("Menu tidak valid")