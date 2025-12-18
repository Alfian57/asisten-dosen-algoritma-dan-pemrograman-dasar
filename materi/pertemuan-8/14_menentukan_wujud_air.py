# Menentukan Wujud Air
# Tujuan: Menentukan wujud air berdasarkan suhu

suhu = float(input("Masukkan suhu (Celcius): "))

if suhu <= 0:
    wujud = "Padat (Es)"
elif suhu > 0 and suhu < 100:
    wujud = "Cair"
else:
    wujud = "Gas (Uap)"

print(f"Pada suhu ini air berwujud {wujud}.")
