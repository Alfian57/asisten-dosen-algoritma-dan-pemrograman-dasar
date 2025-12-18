file = open("test.txt", 'r')
# Dia akan membaca semua datanya
print(file.read())

# Dia akan membaca perbaris
print(file.readline())
print(file.readline())

# Dia akan membaca semua nya namun dalam bentuk
print(file.readlines())

# Dia akan menuliskan data baru pada file
# file.write("remote\n")

file.close()