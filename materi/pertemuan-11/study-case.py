from colorama import Fore, Style
from tabulate import tabulate
import wikipedia
import qrcode

wikipedia.set_lang("id")

print(Fore.BLUE + "SMART WIKI-CARD GENERATOR")
kata_kunci = input(Style.RESET_ALL + "Masukan kata kunci : ")

print(Fore.YELLOW + "Sedang mencari...")

halaman = wikipedia.page(kata_kunci)
ringkasan = wikipedia.summary(kata_kunci, sentences=3)

data = [
    ["Judul Halaman", halaman.title],
    ["Url", halaman.url],
    ["Jumlah karakter ringkasan", len(ringkasan)],
]
print(tabulate(data, headers=["Key" ,"Value"], tablefmt="fancy_grid"))

qr = qrcode.make(halaman.url)
qr.save("qr.png")
print(Fore.GREEN + "File QR sudah tersimpan dalam qr.png")