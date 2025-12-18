# Fungsi Cek Kelulusan
# Tujuan: Menentukan status kelulusan siswa berdasarkan nilai KKM

def cek_status(nilai):
    # Nilai >= 75 (75 pas termasuk lulus)
    if nilai >= 75:
        return "Lulus"
    else:
        return "Remidial"

nilai_siswa = int(input("Masukkan nilai siswa: "))
status = cek_status(nilai_siswa)

print(f"Status Anda: {status}.")
