# CHALLENGE MODIFIKASI
# Ubah biaya 2 jam pertamanya jadi Gratis (Rp 0). Jam berikutnya baru bayar.

# Fungsi Biaya Parkir
# Tujuan: Menghitung biaya parkir dengan pembulatan waktu ke atas

import math

def hitung_parkir(lama):
    if lama <= 0:
        return 0
    # MODIFIKASI: 2 jam pertama gratis
    elif lama <= 2:
        return 0
    else:
        # Sisa jam dihitung per jam penuh (pembulatan ke atas)
        sisa_jam = math.ceil(lama - 2)
        return sisa_jam * 1000

jam_masuk = int(input("Masukkan jam masuk (format 24 jam): "))
jam_keluar = int(input("Masukkan jam keluar (format 24 jam): "))

lama_parkir = jam_keluar - jam_masuk
biaya = hitung_parkir(lama_parkir)

print(f"Total biaya parkir: Rp {biaya}.")
