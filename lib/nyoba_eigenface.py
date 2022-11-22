# %load lib/imgprocess.py
import cv2
import numpy as np
from imgprocess import load_image_data
from eigen import eigens


A = load_image_data("dataset/105_classes_pins_dataset/pins_Adriana Lima/")
gamma = []
for i in range(A.shape[0]):
    gamma.append(np.reshape(A[i], (10000, 1)))

#Menghitung rata-rata
gamma = np.array(gamma, dtype=np.uint8)
psi = gamma.sum(axis=0) / gamma.shape[0]

#Mengurangkan matriks awal dengan rata-rata
A = []
for i in range(gamma.shape[0]):
    A.append(gamma[i] - psi)
    sub_avg = A

#menghitung matriks covarian
A = np.concatenate(A, axis=1)
cov = A.T @ A

#Menghitung eigenvector
_, v = eigens(cov)

#Menghitung eigenfaces
eigenfaces = []
for i in range(213):
    eigenfaces.append(A @ v[i])

img = np.array(eigenfaces[212], dtype=np.int32)
img = np.reshape(img, (100, 100))
img = np.array(img, dtype=np.int8)
img = np.reshape(np.array(eigenfaces[0], dtype=np.int8), (100, 100))

cv2.imshow("eigenface", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
