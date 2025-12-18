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
    "minum": "drink"
}

kata = input("Masukkan kata dalam Bahasa Indonesia: ").lower()

if kata in kamus:
    print(f"Terjemahan: {kamus[kata]}")
else:
    print("Kata tidak ditemukan")
