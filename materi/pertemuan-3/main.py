# ===== OPERATOR PERBANDINGAN =====
# <, <=, >, >=, ==, !=

# 1. <
# LEBIH KECIL
print(5 < 3) # False
print(5 < 5) # False
print()

# 2. <=
# LEBIH KECIL ATAU SAMA DENGAN
print(5 <= 3) # False
print(5 <= 5) # True
print()

# 3. >
# LEBIH BESAR
print(5 > 3) # True
print(5 > 5) # False
print()

# 4. >=
# LEBIH BESAR ATAU SAMA DENGAN
print(5 >= 3) # True
print(5 >= 5) # True
print()

# 5. ==
# SAMA DENGAN
print("apel" == "apel") # True
print("apel" == "Apel") # False
print(1.1 == 1.1) # True
print(True == True) # True
print(True == False) # False
print(False == False) # True
print()

# 6. !=
# TIDAK SAMA DENGAN
print("apel" != "apel") # False
print("apel" != "Apel") # True
print(1.1 != 1.1) # False
print(True != True) # False
print(True != False) # True
print(False != False) # False
print()


# ===== GERBANG LOGIKA =====
# not, and, or

# not
print(not True) # False
print(not False) # True
print()

# and
# KEDUANYA HARUS TRUE UNTUK MENDAPATKAN TRUE
# JIKA ADA SALAH SATU YANG FALSE, MAKA HASILNYA AKAN FALSE 
print(False and False) # False
print(False and True) # False
print(True and False) # False
print(True and True) # True
print()

# or
# JIKA ADA SALAH SATU YANG TRUE, MAKA HASILNYA AKAN TRUE 
print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True) # True
print()


# ===== PERCABANGAN =====
# if, elif, else
harga_jual = 50000
if harga_jual >= 250000:
    print("Anda mendapatkan diskon")
    print("Diskon adalah 50%")
elif harga_jual >= 100000:
    print("Anda mendapatkan diskon")
    print("Diskon adalah 25%")
else:
    print("Anda tidak mendapatkan diskon")

print("Program selesai")