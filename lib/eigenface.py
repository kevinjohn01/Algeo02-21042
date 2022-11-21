import numpy as np

def multiply(a,b):
  arr1 = np.array(a)
  arr2 = np.array(b)
  arr3 = arr2.T

  M = [[0 for j in range(len(b[0]))] for i in range(len(a))]
  for i in range(len(a)):
    for j in range(len(b[0])):
      M[i][j] = np.dot(arr1[i],arr3[j])
  return M

#step 2
#Menghitung matriks rata-rata
def average(matriks):
  matrixavg = np.zeros((N,N))
  for k in range(count):
    currmatrix = np.array(matriks[k])
    matrixavg += currmatrix
  for i in range(N):
    for j in range(N):
      matrixavg[i][j] = matrixavg[i][j]/count
  #print(matrixavg)
  return matrixavg

#step 3
#Menghitung selisih matriks dengan rata-rata
def selisih(matriks,matrixavg):
  for k in range(count):
    selisih = [[0 for j in range(len(matriks[0]))] for i in range(len(matriks[0][0]))]
    for i in range(len(matriks[0])):
      for j in range(len(matriks[0][0])):
        matriks[k][i][j] = float(matriks[k][i][j]) - float(matrixavg[i][j])
  return matriks
#matsel = np.array(matriks)
#print("setelah dikurangi dengan rata2: ")
#print(matriks)

#step 4
def covarian2(m):
  matrix = m
  arraym = np.array(m)
  transposed = arraym.T
  hasil = multiply(matrix,transposed)

  return hasil

#Menghitung matriks covarian
def covarian(matriks):
  A = [[0 for j in range (N)] for i in range(N*count)]
  for i in range(N*count):
    for j in range(N):
      if i<N :
        A[i][j] = matriks[0][i][j]
      else:
        k = i//N
        A[i][j] = matriks[k][i-(k*N)][j] 
  #print(A)
  arrayA = np.array(A).T

  C = covarian2(arrayA)
  return C
  #print("matriks kovarian: ")
  #print(C)

#step 5
def eigenvector(matriks):
  evalues, evectors = np.linalg.eig(matriks)
  return evectors

#print("eigen vektor:")
#print(eigen)

#step 6
def eigenface(matriks, eigen):
  eigenface = [[[0 for j in range(N)] for i in range(N)] for k in range(count)]
  for k in range(count):
    array1 = np.array(matriks[k])
    eigenface[k] = multiply(eigen,array1)
  #print("eigenface:")
  #print(eigenface)
  return eigenface

def selisihnew(matrixnew,matrixavg):
  selisihn = [[0 for j in range(len(matrixnew[0]))] for i in range(len(matrixnew))]
  for i in range(len(matrixnew)):
    for j in range(len(matrixnew[0])):
      selisihn[i][j] = matrixnew[i][j] - matrixavg[i][j]
  return selisihn

def process(matriks,matrixnew):
  avg = average(matriks)
  matriks = selisih(matriks,avg)
  C = covarian(matriks)
  eigen = eigenvector(C)
  eigenfaces = eigenface(matriks,eigen)
  m = selisihnew(matrixnew,avg)
  #print("m: ",m)
  eigenfacenew = multiply(eigen,m)
  #print(eigenfacenew)

  #mencari euclidean distance
  panjangnew = 0
  for i in range(N):
    for j in range(N):
      panjangnew += eigenfacenew[i][j]**2
  panjangnew = panjangnew**(0.5)
  #print(panjangnew)

  arrpanjang = [0 for k in range(count)]
  for k in range(count):
    panjang = 0
    for i in range(N):
      for j in range(N):
        panjang += eigenfaces[k][i][j]**2
    panjang = panjang**(0.5)
    arrpanjang[k] = panjang
  #print(arrpanjang)

  #mencari jarak terdekat
  for k in range(count):
    arrpanjang[k] = abs(arrpanjang[k]-panjangnew)
  #print(arrpanjang)

  min = arrpanjang[0]
  idxmin = 0
  for k in range(1,count):
    if arrpanjang[k] < min:
      min = arrpanjang[k]
      idxmin = k
  print(min,idxmin)


#TAHAP PENGENALAN WAJAH
#testing
N = 4
count = 12
matriks =[[[4,5,6,1],[1,2,3,4],[7,8,9,3],[7,8,9,3]],
          [[1,1,1,1],[0,1,0,1],[1,2,2,5],[1,2,2,5]], 
          [[1,2,3,4],[4,5,6,7],[7,8,9,1],[4,5,6,7]],
          [[0,2,2,3],[4,5,3,2],[1,6,3,5],[4,5,3,2]],
          [[1,1,1,1],[0,1,0,0],[1,2,2,2],[1,1,1,1]],
          [[1,9,1,2],[0,1,0,3],[1,2,2,3],[1,9,1,2]],
          [[8,1,8,3],[9,1,0,1],[1,3,2,2],[8,1,8,3]],
          [[8,1,8,3],[9,1,0,1],[1,9,2,2],[8,1,8,3]],
          [[8,1,9,3],[9,1,0,1],[1,4,2,2],[8,1,8,3]],
          [[8,1,9,3],[9,1,0,1],[1,5,2,2],[8,1,8,3]],
          [[8,1,9,3],[9,1,0,1],[1,6,2,2],[8,1,8,4]],
          [[1,1,1,1],[2,2,2,2],[2,2,2,2],[1,1,1,1]]]

matrixnew = [[8,1,8,3],[9,1,0,1],[1,9,2,2],[8,1,8,3]]
process(matriks,matrixnew)

