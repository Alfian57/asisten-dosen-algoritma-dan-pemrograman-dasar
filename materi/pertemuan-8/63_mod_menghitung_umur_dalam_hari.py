# CHALLENGE MODIFIKASI
# Hitung juga dalam Jam. (Output Hari dikali 24).

# Menghitung Umur dalam Hari
# Tujuan: Mengestimasi total hari hidup

usia = int(input("Masukkan usia Anda (tahun): "))

# Hitung total hari (abaikan kabisat)
total_hari = usia * 365

print(f"Anda telah hidup selama +/- {total_hari} hari.")

# MODIFIKASI: Hitung juga dalam jam
total_jam = total_hari * 24
print(f"Atau sekitar {total_jam} jam.")
