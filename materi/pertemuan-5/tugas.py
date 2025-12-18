print("=====================================")
print("Program Menggambar Segitiga Siku-Siku")
print("=====================================\n")
tinggi = int(input("Masukan tinggi segitiga : "))

# Cara 1
for i in range(1, tinggi + 1):
    print("*" * i)

# Cara 2
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end="")
    print()
