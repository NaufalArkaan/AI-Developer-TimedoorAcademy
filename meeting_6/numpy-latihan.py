# import numpy as np #Mengimport library Numpy agar bisa digunakan
# a = np.array([1,2,3,4,5]) # Membuat Numpy array 1D 
# b = np.array([6,7,8,9,10])# Membuat Numpy array 1D 
# print(a) # Menampilkan output dari Numpy array yang sudah dibuat
# print(b) # Menampilkan output dari Numpy array yang sudah dibuat

# c = np.array(['hai', 3, 2.5])
# print(c)
# print(c.dtype)

# Array2D = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(Array2D)

# array3D = np.array([[[1,2,3], [4,5,6]],
# [[7,8,9], [10,11,12]],
# [[13,14,15], [16,17,18]]])

# print(array3D)

# data = np.array([[1,2,3,4], [5,6,7,8]])
# print(data.shape)
# print(data[1, 2])

# data = np.array([[1,2,3,4], [5,6,7,8]])
# # Tambahkan code di bawah ini
# print(data[:, 2])
# print(data[1, :])

# data = np.array([[1,2,3,4], [5,6,7,8]])
# # Tambahkan code di bawah ini
# print(data[:, 1:4])
# print(data[1, 1:4])

# data = np.array([[1,2,3,4,5], [5,6,7,8,9]])
# # Tambahkan code di bawah ini
# print(data.diagonal(3))

# empty = np.zeros((4,4), dtype="int")
# empty[0, 1:4] = [1,55,3]
# empty[-1, 0] = 7 #-1 = row index terakhir
# empty[1:3, 1] = [9,5]
# empty[2:3, 3] = [70]
# empty[-1, 2:4] = [14,22]
# print(empty)   # ^
#                # | Nilai baru

# c = np.array([3,6,9,12])
# d = np.array([2,4,6,8])
# print(np.add(c,d))
# print(np.subtract(c,d))
# print(np.multiply(c,d))
# print(np.divide(c,d))
# print(c.sum(), d.sum())
# print(c.min(), d.min())
# print(c.max(), d.max())

# arr = np.array([[1,2,3], [4,5,6]])
# print(arr.shape)