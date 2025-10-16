# ===== Sub Program / Fungsi / Function =====
# sapa_orang itu nama Sub Program/Fungsi/Function
# nama itu adalah parameter
def sapa_orang(nama, waktu):
    print("Halo " + nama)
    print("Selamat " + waktu)
    print("Apa kabar ?")
    print()

# "Charles" adalah argument
# "pagi" adalah argument
sapa_orang("Charles", "pagi")
sapa_orang("Dika", "malam")
sapa_orang("Rasyid", "pagi")

def cek_bilangan_genap(angka):
    if angka % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")

cek_bilangan_genap(9)
cek_bilangan_genap(10)

print()


# ===== VARIABLE SCOPE =====
def say_hello():
    nama = "Diva" # local variable
    print("Halo " + nama)
    print(nama)

# error
# print(nama)

umur = 19 # global variable
def katakan_umurku():
    print(umur)
def katakan_umurku_dua():
    print(umur)

say_hello()

nama = input("Masukan nama : ")
print(nama)


# ===== Fungsi dengan return =====

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil_luas = luas_persegi_panjang(10, 5)
print("Luas persegi panjang adalah " + str(hasil_luas))
