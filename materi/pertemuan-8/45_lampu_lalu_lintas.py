# Lampu Lalu Lintas
# Tujuan: Simulasi aksi berdasarkan warna lampu

warna = input("Masukkan warna lampu (Merah/Kuning/Hijau): ").lower()

if warna == "merah":
    print("Berhenti")
elif warna == "kuning":
    print("Bersiap")
elif warna == "hijau":
    print("Jalan")
else:
    print("Warna tidak valid")
