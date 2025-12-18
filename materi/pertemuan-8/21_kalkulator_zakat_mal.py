# Kalkulator Zakat Mal
# Tujuan: Menghitung zakat harta

def hitung_zakat(harta):
    nishab = 85000000  # Rp 85 juta
    if harta >= nishab:
        return harta * 0.025  # 2.5%
    else:
        return 0

total_harta = int(input("Masukkan total harta Anda: "))
zakat = hitung_zakat(total_harta)

print(f"Zakat yang harus dibayar: Rp {int(zakat)}.")
