import numpy as np




matrix = [9,7,2,0,1,1,8,0,7,6,9,8,0,2,0,9,4,4,9,2,4,7,5,0,7]


#############################################sobel
# H1 = [-1,0,1,-2,0,2,-1,0,1]
# H2 = [1,2,1,0,0,0,-1,-2,-1]


#########################################prew
H1 = [0,0,0,0,-1,0,0,0,1]
H2 = [0,0,0,0,0,-1,0,1,0]
M = 5
N = 5




print(matrix)
print(H1)
print(H2)
matrix2 = []
H1_new = []
H2_new = []
matrix_news = []
def convertmatrix_MN():
	dem = 0
	for k in range(0,M):
		matrancon = []
		for i in range(0,N):
			matrancon.append(matrix[dem])
			dem = dem + 1
		matrix2.append(matrancon)
def convermatrix_H(H,H_new):
	dem = 0
	for i in range(0,3):
		matrancon = []
		for j in range(0,3):
			matrancon.append(H[dem])
			dem = dem + 1
		H_new.append(matrancon)
def convert_new_matrix_mn(M,N,matrix,matrixnews):
	for i in range(0,M+2):
		matrancon = []
		for j in range(0,N+2):
			if (i == 0):
				matrancon.append(0)
			elif (j == 0):
				matrancon.append(0)
			elif (i == M+1):
				matrancon.append(0)
			elif (j == N+1):
				matrancon.append(0)
			else:
				matrancon.append(matrix[i-1][j-1])
		matrixnews.append(matrancon)
def tinhmatran(matrix_new,H_new,matran_G,G):
	for i in range(1,len(matrix_new)-1):
		matrancon = []
		for j in range(1,len(matrix_new[i])-1):
			bien = matrix_new[i-1][j-1]*H_new[0][0] + matrix_new[i-1][j]*H_new[0][1] + matrix_new[i-1][j+1]*H_new[0][2] 
			bien = bien + matrix_new[i][j-1]*H_new[1][0] + matrix_new[i][j]*H_new[1][1] + matrix_new[i][j+1]*H_new[1][2] 
			bien = bien + matrix_new[i+1][j-1]*H_new[2][0] + matrix_new[i+1][j]*H_new[2][1] + matrix_new[i+1][j+1]*H_new[2][2]
			print('+',G,'(',i-1,',',j-1,') = ','|',matrix_new[i-1][j-1],'*',H_new[0][0],'+',matrix_new[i-1][j],'*',H_new[0][1],'+',matrix_new[i-1][j+1],'*',H_new[0][2],'+',matrix_new[i][j-1],'*',H_new[1][0],'+',matrix_new[i][j],'*',H_new[1][1],'+',matrix_new[i][j+1],'*',H_new[1][2],'+',matrix_new[i+1][j-1],'*',H_new[2][0],'+',matrix_new[i+1][j],'*',H_new[2][1],'+',matrix_new[i+1][j+1],'*',H_new[2][2],'|=',abs(bien))
			matrancon.append(abs(bien))
		matran_G.append(matrancon)
convertmatrix_MN()
convermatrix_H(H1,H1_new)
convermatrix_H(H2,H2_new)
convert_new_matrix_mn(M,N,matrix2,matrix_news)
matran_H1 = []
print("Thực hiện tính |G1|:")
print()
tinhmatran(matrix_news,H1_new,matran_H1,"G1")
print()
print("Ta có ma trận G1 :")
for i in range(len(matran_H1)):
	print(matran_H1[i])
print()
matran_H2 = []
print("Thực hiện tính |G2|:")
tinhmatran(matrix_news,H2_new,matran_H2,"G2")
print()
print("Ta có ma trận G2 :")
for i in range(len(matran_H2)):
	print(matran_H2[i])
print()
matran_G = []
for i in range(len(matran_H1)):
	matrancon_tong = []
	for j in range(len(matran_H1[i])):
		tong = matran_H1[i][j] + matran_H2[i][j]
		matrancon_tong.append(tong)
	matran_G.append(matrancon_tong)
print()
print("Ma trận G: ")
for i in range(len(matran_G)):
	print(matran_G[i])