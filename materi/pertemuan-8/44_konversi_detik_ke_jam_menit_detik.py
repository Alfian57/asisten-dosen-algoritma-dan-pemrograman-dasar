# Konversi Detik ke Jam Menit Detik
# Tujuan: Membalikkan konversi waktu

total_detik = int(input("Masukkan total detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik_akhir = sisa_detik % 60

print(f"{jam} jam, {menit} menit, {detik_akhir} detik")
