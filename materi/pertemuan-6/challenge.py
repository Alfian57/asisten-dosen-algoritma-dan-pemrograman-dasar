users = [
    {
        "username": "admin",
        "password": "admin"
    },
    {
        "username": "alfian",
        "password": "rahasia"
    },
]

data_mahasiswa = []


def print_menu_tamu():
    print("\n======================")
    print("SISTEM NILAI MAHASISWA")
    print("======================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

def print_menu_utama():
    print("\n=========")
    print("Dashboard")
    print("=========")
    print("1. Tambah data mahasiswa")
    print("2. Lihat semua data")
    print("3. Logout")

def login():
    username_input = input("\nMasukkan username: ")
    password_input = input("Masukkan password: ")
    
    for user in users:
        if user["username"] == username_input and user["password"] == password_input:
            return True
    
    return False

def register():
    username_input = input("Masukkan username baru: ")
    password_input = input("Masukkan password baru: ")
    
    # Tambahkan pengguna baru ke list
    users.append({
        "username": username_input,
        "password": password_input
    })
    
    print("\nRegistrasi berhasil! Silakan login.")


def tambah_data():
    nama = input("\nMasukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    nilai = int(input("Masukkan nilai mahasiswa (0-100): "))
    
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "nilai": nilai
    })
    
    print(f"\nData mahasiswa {nama} berhasil ditambahkan.")


def lihat_data():
    if not data_mahasiswa:
        print("\nBelum ada data mahasiswa.")
        return
    
    nomor = 1
    print("\nDaftar Mahasiswa:")
    print("-----------------")
    for mhs in data_mahasiswa:
        print(f"{nomor}. Nama: {mhs['nama']}, NIM: {mhs['nim']}, Nilai: {mhs['nilai']}")
        nomor += 1
    


    
while True:
    print_menu_tamu()
    menu_tamu = input("\nPilih menu [1-3]: ")

    if menu_tamu == "1":
        login_berhasil = login()

        if not login_berhasil:
            print("❌ Login gagal! Username atau password salah.")
            continue
        else:
            while True:
                print_menu_utama()
                menu_utama = input("\nPilih menu (1-3): ")
                
                if menu_utama == "1":
                    tambah_data()
                elif menu_utama == "2":
                    lihat_data()
                elif menu_utama == "3":
                    break
                else:
                    print("Pilihan tidak valid! Masukkan angka 1-3.")

    elif menu_tamu == "2":
        register()

    elif menu_tamu == "3":
        break

    else:
        print("\n❌ Pilihan tidak valid! Masukkan angka 1-3.")


print("\nTerima kasih telah menggunakan program ini!")


