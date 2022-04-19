import numpy as np
import math

pi = math.pi

# nhập mảng f(x,y) vào arr
arr = np.array([[3, 3],
                [1, 3]])
M = arr.shape[0]
N = arr.shape[1]
arrF = np.zeros((M, N))

for u in range(arrF.shape[0]):
       for v in range(arrF.shape[1]):
               e = 0
               for x in range(M):
                      for y in range(N):
                            temp = -2*((u * x)/M + (v * y)/N)
                            if temp == 0:
                                   e =e +  arr[x][y]
                            else:
                                   e = e +  math.cos(temp * pi) * arr[x][y]

               arrF[u][v] = e

print(arrF)
