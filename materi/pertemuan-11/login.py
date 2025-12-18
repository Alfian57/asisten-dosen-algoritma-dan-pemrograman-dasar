from colorama import Fore, Style

users = [
    {
        "username": "admin",
        "password": "rahasia"
    },
    {
        "username": "guru",
        "password": "rahasia"
    }
]

login_berhasil = False

while not login_berhasil:
    username_input = input(Style.RESET_ALL + "Masukan username : ")
    password_input = input("Masukan password : ")

    for user in users:
        if user["username"] == username_input and user["password"] == password_input:
            print(Fore.GREEN + "Login berhasil")
            login_berhasil = True

    if not login_berhasil:
        print(Fore.RED + "Login Gagal, silahkan coba lagi")
