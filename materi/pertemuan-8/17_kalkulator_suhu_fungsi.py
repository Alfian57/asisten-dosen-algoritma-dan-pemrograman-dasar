# Kalkulator Suhu (Fungsi)
# Tujuan: Konversi suhu dengan pilihan menu menggunakan fungsi

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("=== Kalkulator Suhu ===")
print("1. Celcius ke Fahrenheit")
print("2. Fahrenheit ke Celcius")

pilihan = int(input("Pilih menu (1/2): "))

if pilihan == 1:
    suhu = float(input("Masukkan suhu dalam Celcius: "))
    hasil = celcius_to_fahrenheit(suhu)
    print(f"{suhu}°C = {hasil:.2f}°F")
elif pilihan == 2:
    suhu = float(input("Masukkan suhu dalam Fahrenheit: "))
    hasil = fahrenheit_to_celcius(suhu)
    print(f"{suhu}°F = {hasil:.2f}°C")
else:
    print("Pilihan tidak valid")
