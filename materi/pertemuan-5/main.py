# ===== WHILE LOOP =====
# Digunakan saat kita tahu seberapa banyak perulangannya
# Ataupun
# Digunakan saat kita tidak tahu seberapa banyak perulangannya

# angka = 1
# print(angka)

# syntax
# while kondisi:
#     isinya

angka = 1
while angka <= 5:
    print(angka)
    angka += 1

print("Program selesai")
print()


# ===== Continue dan Break =====
# continue untuk menghentikan iterasi
angka = 1
while angka <= 5:
    if angka == 2:
        angka += 1
        continue

    print(angka)
    angka += 1

print("Program selesai")
print()


# untuk keluar langsung dari perulangan
angka = 1
while angka <= 5:
    if angka == 2:
        angka += 1
        break

    print(angka)
    angka += 1

print("Program selesai")
print()


# ===== range() =====
# Argumen pertama adalah stopnya
angka = range(7) # 0, 1, 2, 3, 4, 5, 6
print(list(angka))

# Argumen pertama adalah startnya
# Argumen kedua adalah stopnya
angka = range(1, 7) # 1, 2, 3, 4, 5, 6
print(list(angka))

# Argumen pertama adalah startnya
# Argumen kedua adalah stopnya
# Argumen ketiga adalah stepnya
angka = range(0, 11, 2) # 0, 2, 4, 6, 8, 10
print(list(angka))

angka = range(10, 0, -1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
print(list(angka))

# ===== For Loop =====
# Digunakan saat kita tahu seberapa banyak perulangannya

# 0, 1, 2, 3, 4
for i in range(0, 5):
    print(f"Sekarang adalah perulangan ke-{i}")