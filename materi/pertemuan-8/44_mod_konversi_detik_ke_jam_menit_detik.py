# CHALLENGE MODIFIKASI
# Inputnya diganti jadi Menit (integer). Konversi ke Jam dan Sisa Menit.

# Konversi Detik ke Jam Menit Detik
# Tujuan: Membalikkan konversi waktu

# MODIFIKASI: Input jadi Menit, konversi ke jam dan sisa menit
total_menit = int(input("Masukkan total menit: "))

jam = total_menit // 60
sisa_menit = total_menit % 60

print(f"{jam} jam, {sisa_menit} menit")
