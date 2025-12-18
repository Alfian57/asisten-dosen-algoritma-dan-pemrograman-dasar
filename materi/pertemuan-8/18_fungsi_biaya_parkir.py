# Fungsi Biaya Parkir
# Tujuan: Menghitung biaya parkir dengan pembulatan waktu ke atas

import math

def hitung_parkir(lama):
    if lama <= 0:
        return 0
    elif lama <= 2:
        return 3000
    else:
        # Sisa jam dihitung per jam penuh (pembulatan ke atas)
        sisa_jam = math.ceil(lama - 2)
        return 3000 + (sisa_jam * 1000)

jam_masuk = int(input("Masukkan jam masuk (format 24 jam): "))
jam_keluar = int(input("Masukkan jam keluar (format 24 jam): "))

lama_parkir = jam_keluar - jam_masuk
biaya = hitung_parkir(lama_parkir)

print(f"Total biaya parkir: Rp {biaya}.")
