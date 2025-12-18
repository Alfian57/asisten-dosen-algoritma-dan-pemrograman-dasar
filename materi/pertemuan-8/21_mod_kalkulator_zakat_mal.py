# CHALLENGE MODIFIKASI
# Ubah nisabnya (batas harta). Zakat hanya wajib kalau harta >= 100 juta.

# Kalkulator Zakat Mal
# Tujuan: Menghitung zakat harta

def hitung_zakat(harta):
    # MODIFIKASI: Ubah nishab jadi 100 juta
    nishab = 100000000  # Rp 100 juta
    if harta >= nishab:
        return harta * 0.025  # 2.5%
    else:
        return 0

total_harta = int(input("Masukkan total harta Anda: "))
zakat = hitung_zakat(total_harta)

print(f"Zakat yang harus dibayar: Rp {int(zakat)}.")
