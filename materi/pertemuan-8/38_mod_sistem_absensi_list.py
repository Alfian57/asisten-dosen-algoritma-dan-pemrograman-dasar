# CHALLENGE MODIFIKASI
# Ubah kuota absennya. Jadi hanya bisa menampung 3 nama, setelah itu program berhenti.

# Sistem Absensi (List)
# Tujuan: Mencatat nama unik kehadiran (menghindari duplikat)

daftar_hadir = []

print("=== Sistem Absensi ===")
# MODIFIKASI: Ubah kuota jadi 3
print("Masukkan nama 3 orang (duplikat akan ditolak):")

for i in range(3):
    nama = input(f"Nama ke-{i+1}: ")
    
    if nama in daftar_hadir:
        print(f"'{nama}' sudah absen.")
    else:
        daftar_hadir.append(nama)
        print(f"'{nama}' berhasil absen.")

print("\n=== Daftar Hadir ===")
for i, nama in enumerate(daftar_hadir, 1):
    print(f"{i}. {nama}")
