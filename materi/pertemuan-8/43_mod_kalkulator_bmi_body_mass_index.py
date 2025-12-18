# CHALLENGE MODIFIKASI
# Hilangkan kategori 'Kurus' dan 'Gemuk'. Tampilkan saja nilai BMI-nya tanpa kategori.

# Kalkulator BMI (Body Mass Index)
# Tujuan: Menghitung BMI dan kategorinya

berat = float(input("Masukkan berat badan (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

# Ubah tinggi ke meter
tinggi_m = tinggi_cm / 100

# Hitung BMI
bmi = berat / (tinggi_m ** 2)

# MODIFIKASI: Hilangkan kategori, hanya tampilkan nilai BMI
print(f"BMI Anda: {bmi:.2f}")
