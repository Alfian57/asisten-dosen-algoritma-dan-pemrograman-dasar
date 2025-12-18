# Konversi Nilai ke Bobot (List Comprehension - Opsional)
# Tujuan: Mengubah list nilai angka menjadi list bobot (A/B/C) sekaligus

def konversi_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    else:
        return "D"

nilai_list = [80, 60, 90, 75, 55]
bobot_list = []

print(f"List nilai: {nilai_list}")

for nilai in nilai_list:
    bobot = konversi_nilai(nilai)
    bobot_list.append(bobot)

print(f"List bobot: {bobot_list}")
