# Menghitung Umur dalam Hari
# Tujuan: Mengestimasi total hari hidup

usia = int(input("Masukkan usia Anda (tahun): "))

# Hitung total hari (abaikan kabisat)
total_hari = usia * 365

print(f"Anda telah hidup selama +/- {total_hari} hari.")
