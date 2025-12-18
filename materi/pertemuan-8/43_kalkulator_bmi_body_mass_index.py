# Kalkulator BMI (Body Mass Index)
# Tujuan: Menghitung BMI dan kategorinya

berat = float(input("Masukkan berat badan (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

# Ubah tinggi ke meter
tinggi_m = tinggi_cm / 100

# Hitung BMI
bmi = berat / (tinggi_m ** 2)

# Tentukan kategori
if bmi < 18.5:
    kategori = "Kurus"
elif bmi >= 18.5 and bmi <= 24.9:
    kategori = "Normal"
else:
    kategori = "Gemuk"

print(f"BMI Anda: {bmi:.2f}, Kategori: {kategori}")
