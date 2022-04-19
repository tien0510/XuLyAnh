import numpy as np
import math

pi = math.pi

# nhập mảng F(x,y) vào arrF
arrF = np.array([[2, 0],
       [0, -2]])

M = arrF.shape[0]
N = arrF.shape[1]
size = M * N

arr = np.zeros((M, N))

for x in range(arr.shape[0]):
       for y in range(arr.shape[1]):
               e = 0
               for u in range(M):
                      for v in range(N):
                            temp = 2*((u * x)/M + (v * y)/N)
                            if temp == 0:
                                   e = e + (arrF[u][v])
                            else:
                                   e = e + math.cos(temp * pi) * arrF[u][v]
                           
               arr[x][y] = e/size

print(arr)