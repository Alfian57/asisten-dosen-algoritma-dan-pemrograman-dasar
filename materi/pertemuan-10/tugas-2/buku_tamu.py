print("--- INPUT ---")
nama_tamu = input("Masukkan Nama Tamu: ")

with open("daftar_tamu.txt", "a") as file:
    file.write(nama_tamu + "\n")

print("\n--- DAFTAR TAMU SAAT INI ---")

with open("daftar_tamu.txt", "r") as file:
    isi_file = file.read()
    print(isi_file, end="")
