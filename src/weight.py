import numpy as np


def weight(eigenfaces, matrixnew, avg):
    # Pemampatan matriks baru
    new = []
    new.append(np.reshape(matrixnew, (10000, 1)))

    # Pengurangan dengan matriks rata-rata
    subt = []
    subt.append(new - avg)
    # ukuran N^2 x 1

    # Weight
    w = []
    for i in range(len(subt)):
        # eigenfaces[i] = N^2 X 1, transposed = 1 X N^2
        w.append(eigenfaces[i].T @ subt)
    # w adalah array yang berisi weight
    return w


def euc_distance(weight, threshold):
    jarak = []
    for i in range(weight):
        fac = weight[i]
        sum = 0
        for j in range(weight):
            curr = weight[j] - fac
            sum += curr**2
        dist = sum ** (0.5)
        jarak.append(dist)
    min = jarak[0]
    idxmin = 0
    for k in range(1, len(jarak)):
        if jarak[k] < min:
            min = jarak[k]
            idxmin = k
    if min < threshold:
        return idxmin
    else:
        # Tidak ada wajah yang cocok
        return -1
