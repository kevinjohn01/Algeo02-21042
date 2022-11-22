# %load lib/imgprocess.py
import cv2
import numpy as np
from imgprocess import load_image_data
from eigen import eigens


A = load_image_data("dataset/105_classes_pins_dataset/pins_Adriana Lima/")
gamma = []
for i in range(A.shape[0]):
    gamma.append(np.reshape(A[i], (10000, 1)))

# Menghitung rata-rata
gamma = np.array(gamma, dtype=np.uint8)
psi = gamma.mean(axis=0)

# Mengurangkan matriks awal dengan rata-rata
A = []
normalized_faces = []
for i in range(gamma.shape[0]):
    normalized_face = gamma[i] - psi
    normalized_faces.append(normalized_face)
    A.append(normalized_face)

# menghitung matriks covarian
A = np.column_stack(A)
cov = A.T @ A

# Menghitung eigenvector
_, v = eigens(cov)

# Menghitung eigenfaces
eigenfaces = []
for i in range(v.shape[0]):
    eigenfaces.append(A @ v[i])

for i in range(len(eigenfaces)):
    img = np.reshape(np.array(eigenfaces[i], dtype=np.int8), (100, 100))
    cv2.imwrite(f"eigenfaces/custom_eigen/eigenface{i+1}.jpg", img)
