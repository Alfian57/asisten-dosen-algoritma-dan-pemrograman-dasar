# CHALLENGE MODIFIKASI
# Saat menampilkan data, hanya tampilkan Nama-nya saja. Nilainya tidak usah.

# Data Mahasiswa (List of Dictionary)
# Tuju an: Menyimpan data nama dan nilai mahasiswa

data_mhs = []

print("=== Data Mahasiswa ===")
while True:
    nama = input("\nMasukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    
    data_mhs.append({'nama': nama, 'nilai': nilai})
    
    lagi = input("Ingin menambahkan data lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        break

# MODIFIKASI: Hanya tampilkan nama saja
print("\n=== Daftar Mahasiswa ===")
for i, mhs in enumerate(data_mhs, 1):
    print(f"{i}. Nama: {mhs['nama']}")
