import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("nilai_mahasiswa.csv")

df["Tugas_Akhir"] = (df["Tugas"] + df["UTS"] + df["UAS"]) / 3

plt.plot(df["Nama"], df["Tugas_Akhir"])
plt.xlabel("Nama")
plt.ylabel("Tugas Akhir")
plt.title("Nilai Mahasiswa")
plt.show()