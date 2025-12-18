# CHALLENGE MODIFIKASI
# Saat menampilkan isi kamus, gunakan loop for untuk print satu per satu.

# Kamus Sinonim (Update Dictionary)
# Tujuan: Menambah kosakata baru ke kamus

kamus_sinonim = {
    "bahagia": "senang",
    "sedih": "duka",
    "besar": "raksasa"
}

print("=== Kamus Sinonim ===")
kata = input("Masukkan kata: ")
sinonim = input("Masukkan sinonim: ")

if kata in kamus_sinonim:
    print(f"Kata '{kata}' sudah ada dengan sinonim '{kamus_sinonim[kata]}'")
else:
    kamus_sinonim[kata] = sinonim
    print(f"Kata '{kata}' berhasil ditambahkan!")

# MODIFIKASI: Gunakan loop for untuk print satu per satu
print("\n=== Isi Kamus Terbaru ===")
for k, v in kamus_sinonim.items():
    print(f"{k}: {v}")
