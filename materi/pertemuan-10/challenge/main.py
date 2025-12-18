from logika_nilai import cek_status

# Baca file data_mentah.txt dan proses
with open("data_mentah.txt", "r") as file_input:
    data = file_input.readlines()

# Proses setiap baris dan tulis ke laporan_hasil.txt
with open("laporan_hasil.txt", "w") as file_output:
    for baris in data:
        baris = baris.strip()
        if baris:  # Skip baris kosong
            data_perbaris = baris.split(",")
            nama = data_perbaris[0]
            nilai = data_perbaris[1]
            nilai = int(nilai)
            status = cek_status(nilai)
            file_output.write(f"{nama} - {nilai} - {status}\n")

print("Laporan berhasil dibuat! Cek file laporan_hasil.txt")
