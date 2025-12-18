# CHALLENGE MODIFIKASI
# Ubah KKM-nya jadi 80. Dan return teksnya ganti jadi 'Competent' / 'Not Competent'.

# Fungsi Cek Kelulusan
# Tujuan: Menentukan status kelulusan siswa berdasarkan nilai KKM

def cek_status(nilai):
    # MODIFIKASI: KKM jadi 80, return Competent/Not Competent
    if nilai >= 80:
        return "Competent"
    else:
        return "Not Competent"

nilai_siswa = int(input("Masukkan nilai siswa: "))
status = cek_status(nilai_siswa)

print(f"Status Anda: {status}.")
