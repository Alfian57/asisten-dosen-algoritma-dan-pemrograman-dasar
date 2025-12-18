# CHALLENGE MODIFIKASI
# Tambahkan satu kata baru ke dalam kamus kodemu (hardcode), misal 'Meja' = 'Table'.

# Kamus Sederhana (Dictionary)
# Tujuan: Menerjemahkan kata Indonesia ke Inggris

kamus = {
    "apel": "apple",
    "kucing": "cat",
    "anjing": "dog",
    "buku": "book",
    "rumah": "house",
    "mobil": "car",
    "makan": "eat",
    "minum": "drink",
    # MODIFIKASI: Tambah kata baru
    "meja": "table"
}

kata = input("Masukkan kata dalam Bahasa Indonesia: ").lower()

if kata in kamus:
    print(f"Terjemahan: {kamus[kata]}")
else:
    print("Kata tidak ditemukan")
