# CHALLENGE MODIFIKASI
# Ubah rate USD jadi tetap (5000 per dolar). Tidak usah input rate lagi.

# Konversi Mata Uang Sederhana
# Tujuan: Mengkonversi Rupiah ke Dolar AS

jumlah_rupiah = int(input("Masukkan jumlah Rupiah: "))

# MODIFIKASI: Rate tetap 5000, tidak perlu input
kurs_dolar = 5000  # 1 Dolar = Rp 5.000
hasil_dolar = jumlah_rupiah / kurs_dolar

print(f"Rp.{jumlah_rupiah} setara dengan ${hasil_dolar:.2f}")
