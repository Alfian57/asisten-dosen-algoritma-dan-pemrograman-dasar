# Tidak diikuti, karena masalah pada linux
import matplotlib
matplotlib.use("TkAgg")

# Tulis mulai dari ini
import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([1, 5, 2, 10, 4])
y_data = np.array([6, 3, 8, 17, 2])

plt.bar(x_data, y_data)
plt.xlabel("Data X")
plt.ylabel("Data Y")
plt.title("Belajar Matplotlib")
plt.show()