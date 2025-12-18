# CHALLENGE MODIFIKASI
# Tambah warna Biru. Jika input Biru, outputnya 'Rusak'.

# Lampu Lalu Lintas
# Tujuan: Simulasi aksi berdasarkan warna lampu

warna = input("Masukkan warna lampu (Merah/Kuning/Hijau/Biru): ").lower()

if warna == "merah":
    print("Berhenti")
elif warna == "kuning":
    print("Bersiap")
elif warna == "hijau":
    print("Jalan")
# MODIFIKASI: Tambah kondisi untuk warna biru
elif warna == "biru":
    print("Rusak")
else:
    print("Warna tidak valid")
