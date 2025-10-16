def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(jari_jari):
    return (22 / 7) * jari_jari * jari_jari


print("===== Kalkulator Luas Bangun Datar =====")
print("1. Persegi Panjang")
print("2. Persegi")
print("3. Lingkaran")

menu = input("Masukkan pilihan (1-3): ")

# Logika Program
if menu == "1":
    panjang = float(input("Masukkan panjang (cm): "))
    lebar = float(input("Masukkan lebar (cm): "))
    luas = luas_persegi_panjang(panjang, lebar)
    print(f"Luas Persegi Panjang: {luas} cm²")

elif menu == "2":
    sisi = float(input("Masukkan sisi (cm): "))
    luas = luas_persegi(sisi)
    print(f"Luas Persegi: {luas} cm²")

elif menu == "3":
    jari_jari = float(input("Masukkan jari-jari (cm): "))
    luas = luas_lingkaran(jari_jari)
    print(f"Luas Lingkaran: {luas} cm²")

else:
    print("Input tidak valid! Silakan pilih 1, 2, atau 3.")
