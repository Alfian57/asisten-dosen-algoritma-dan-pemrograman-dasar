from tabulate import tabulate

mahasiswa = [
    ["Gading", "5230411121"],
    ["Chaless", "5230411122"],
    ["Rasyid", "5230411123"],
]

print(tabulate(mahasiswa, headers=["Nama", "NIM"], tablefmt="fancy_grid"))