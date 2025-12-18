# Konversi Mata Uang Sederhana
# Tujuan: Mengkonversi Rupiah ke Dolar AS

jumlah_rupiah = int(input("Masukkan jumlah Rupiah: "))

kurs_dolar = 15500  # 1 Dolar = Rp 15.500
hasil_dolar = jumlah_rupiah / kurs_dolar

print(f"Rp.{jumlah_rupiah} setara dengan ${hasil_dolar:.2f}")
