# CHALLENGE MODIFIKASI
# Bocorkan angka rahasianya. Print angka rahasianya di awal program sebelum user menebak.

# Tebak Angka Sederhana
# Tujuan: User menebak angka rahasia (hardcoded = 7)

angka_rahasia = 7
max_tebakan = 3
tebakan_ke = 0

print("=== Game Tebak Angka ===")
# MODIFIKASI: Bocorkan angka rahasia
print(f"(BOCORAN: Angka rahasianya adalah {angka_rahasia})")
print(f"Tebak angka antara 1-10. Anda punya {max_tebakan} kesempatan.")

while tebakan_ke < max_tebakan:
    tebakan = int(input("Masukkan tebakan Anda: "))
    tebakan_ke += 1
    
    if tebakan == angka_rahasia:
        print("Selamat, tebakan benar!")
        break
    else:
        print(f"Salah, coba lagi. Sisa kesempatan: {max_tebakan - tebakan_ke}")

if tebakan != angka_rahasia:
    print(f"Game Over! Angka yang benar adalah {angka_rahasia}")
