# CHALLENGE MODIFIKASI
# Balik logikanya. Cek apakah A Bukan kelipatan B.

# Cek Kelipatan
# Tujuan: Mengecek apakah angka A adalah kelipatan angka B

angka_a = int(input("Masukkan angka A: "))
angka_b = int(input("Masukkan angka B: "))

# MODIFIKASI: Balik logikanya, cek bukan kelipatan
if angka_a % angka_b != 0:
    print(f"Benar, {angka_a} bukan kelipatan {angka_b}")
else:
    print(f"Salah, {angka_a} adalah kelipatan {angka_b}")
