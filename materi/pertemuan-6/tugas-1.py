# Variable list_teman berisi nama-nama teman
list_teman = ["rasyid", "arfan", "rifqi", "dery", "leon"]

# Menampilkan nama teman pada elemen pertama
print(list_teman[0])

# Menampilkan nama teman pada elemen terakhir
print(list_teman[4])

# Menampilkan nama teman pada elemen kedua
list_teman.insert(2, "ajie")

# Menghapus nama teman "dery" dari list_teman
list_teman.remove("dery")

# Menghapus nama teman pada elemen terakhir dan menampilkannya
teman_yang_di_pop = list_teman.pop()
print(teman_yang_di_pop)

print(list_teman)

# Mengurutkan nama teman secara alfabetis
list_teman.sort()
print(list_teman)