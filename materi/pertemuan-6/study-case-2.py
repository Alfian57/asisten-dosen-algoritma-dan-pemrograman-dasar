users = [
    {
        "username": "admin",
        "password": "admin"
    },
    {
        "username": "alfian",
        "password": "rahasia"
    },
    {
        "username": "charles",
        "password": "rahasia123"
    },
]

def login():
    username_input = input("Masukan username baru : ")
    password_input = input("Masukan password baru : ")

    for user in users:
        if user["username"] == username_input and user["password"] == password_input:
            return True
        
    return False

def register():
    username_input = input("Masukan username baru : ")
    password_input = input("Masukan password baru : ")

    users.append({
        "username": username_input,
        "password": password_input,
    })

    print("Register berhasil")

def print_menu():
    print("1. Login")
    print("2. Register")
    print("3. Exit")

while True:
    print_menu()
    menu = input("Masukan menu [1-3] : ")

    if menu == "1":
        login_sukses = login()
        if login_sukses:
            print("Login berhasil")
            break
        else:
            print("Login gagal")

    
    elif menu == "2":
        register()

    elif menu == "3":
        break
    
    else:
        print("Menu tidak valid")