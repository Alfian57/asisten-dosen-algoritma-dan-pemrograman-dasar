import numpy as np

# Contoh list bawaan python
contoh_list = [1,2,3,4,5]
hasil_list = []
for item in contoh_list:
    hasil_list.append(item * 2)

# Contoh numpy
contoh_array = np.array([1,2,3,4,5])
hasil_array = contoh_array * 2

# contoh build-in function numpy
print(contoh_array.sum())
print(contoh_array.mean())
print(contoh_array.max())