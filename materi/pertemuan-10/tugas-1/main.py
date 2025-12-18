import hitung_luas as hl
import hitung_material as hm

pilihan = input("Pilih bentuk (lingkaran/persegi): ")

if pilihan == "lingkaran":
    radius = float(input("Masukkan jari-jari: "))
    luas = hl.lingkaran(radius)
elif pilihan == "persegi":
    sisi = float(input("Masukkan sisi: "))
    luas = hl.persegi(sisi)
else:
    print("Pilihan tidak valid")
    exit()

kaleng = hm.cek_kebutuhan_cat(luas)

print(f"Luas: {luas}")
print(f"Jumlah kaleng cat: {kaleng}")
