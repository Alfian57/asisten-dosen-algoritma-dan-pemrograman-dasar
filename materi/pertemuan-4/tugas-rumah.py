nama = "Alfian Gading"
nim = "5230411121"
password = "rahasia"
tanggal_lahir = "1 januari 1945"
alamat = "Zimbabwe"

def login(input_nim, input_password):
	if input_nim == nim and input_password == password:
		return True
	return False


def tampilkanProfil():
    print("\n===== PROFIL MAHASISWA =====")
    print(f"Nama            : {nama}")
    print(f"NIM             : {nim}")
    print(f"Tanggal Lahir   : {tanggal_lahir}")
    print(f"Alamat          : {alamat}")


def hitungRataRata(tugas_pertama, tugas_kedua, tugas_ketiga):
	rata_rata = (0.25 * tugas_pertama) + (0.25 * tugas_kedua) + (0.5 * tugas_ketiga)
	return float(rata_rata)


# Tahap login
input_nim = input("Masukkan NIM: ")
input_password = input("Masukkan password: ")

if login(input_nim, input_password):
    # Jika login berhasil, tampilkan dashboard
    print("\n===== DASHBOARD MAHASISWA =====")
    print("1. Lihat Profil Pengguna")
    print("2. Hitung Nilai Rata-rata tugas")
    print("3. Logout")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkanProfil()
    elif pilihan == "2":
        tugas_satu = float(input("Masukkan nilai tugas pertama (1-100): "))
        tugas_dua = float(input("Masukkan nilai tugas kedua (1-100): "))
        tugas_tiga = float(input("Masukkan nilai tugas ketiga (1-100): "))

        rata_rata = hitungRataRata(tugas_satu, tugas_dua, tugas_tiga)
        print(f"\nNilai rata-rata kamu adalah {rata_rata}")

    elif pilihan == "3":
        print("\nTerima kasih sudah berkunjung!")
        
    else:
        print("\nPilihan tidak valid. Silakan pilih angka 1-3.")

else:
    # Jika login gagal
    print("\nNIM atau password salah!")
    

print("\n===============")
print("Program selesai")
print("===============")
