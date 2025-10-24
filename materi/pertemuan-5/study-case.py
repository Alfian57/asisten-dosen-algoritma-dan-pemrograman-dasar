nim = "5230411121"
password = "rahasia"

def print_menu():
    print("===== Sistem Akademik =====")
    print("1. Login")
    print("2. Batal")

def login(nim_input, password_input):
    if nim_input == nim and password_input == password:
        return True
    else:
        return False

while True:
    print_menu()
    menu = input("Masukan pilihan menu [1-2] : ")

    if menu == "1":
        nim_input = input("Masukan nim : ")
        password_input = input("Masukan password : ")

        if login(nim_input, password_input):
            print('Login berhasil')
            print('Ini ceritanya dashboard')
            break
        else:
            print('Login gagal')

    elif menu == "2":
        break
    else:
        print("Input tidak valid")

print("Program Selesai")