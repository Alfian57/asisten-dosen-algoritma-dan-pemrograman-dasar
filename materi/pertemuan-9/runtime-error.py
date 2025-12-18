try:
    print("===Kalkulator Pembagian===")
    angka_pertama = int(input("Masukan angka pertama : "))
    angka_kedua = int(input("Masukan angka kedua : "))

    hasil = angka_pertama / angka_kedua
    print(f"Hasil pembagian adalah {hasil}")
except ValueError:
    print("Harus masukan angka")
except ZeroDivisionError:
    print("Tidak membagi dengan 0")
except Exception:
    print("Terjadi error")
finally:
    print("Program selesai")