# CHALLENGE MODIFIKASI
# Hapus menu 2 (Fahrenheit ke Celcius). Jadi program langsung otomatis
# konversi Celcius ke Fahrenheit tanpa tanya menu.

# Kalkulator Suhu (Fungsi)
# Tujuan: Konversi suhu dengan pilihan menu menggunakan fungsi

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# MODIFIKASI: Hapus fungsi fahrenheit_to_celcius dan menu
# Langsung konversi Celcius ke Fahrenheit

suhu = float(input("Masukkan suhu dalam Celcius: "))
hasil = celcius_to_fahrenheit(suhu)
print(f"{suhu}°C = {hasil:.2f}°F")
