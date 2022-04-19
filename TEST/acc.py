import numpy as np
matrix = [3,9,2,7,1,4,3,5,8,4,2,9,1,3,7,1,8,4,4,0,6,8,7,7,4]

M = 5
N = 5


print(matrix)



matrix2 = []
dem = 0
for k in range(0,M):
    matrancon = []
    for i in range(0,N):
        matrancon.append(matrix[dem])
        dem = dem + 1
    matrix2.append(matrancon)
matrix_Itb = []
matrix_news = []
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
            matrancon.append(matrix2[i-1][j-1])
    matrix_news.append(matrancon)
def trungbinh():
    print("Lọc trung bình: ")
    print("- Áp dụng công thức ta được kết quả:")
    matrix_cuoi = []
    for i in range(1,len(matrix_news)-1):
        matrancon = []
        for j in range(1,len(matrix_news[i])-1):
            bien = round(((matrix_news[i-1][j-1] + matrix_news[i-1][j] + matrix_news[i-1][j+1] + matrix_news[i][j-1]+ matrix_news[i][j]+ matrix_news[i][j+1] + matrix_news[i+1][j-1]+ matrix_news[i+1][j]+ matrix_news[i+1][j+1])/9),0)
            matrancon.append(int(bien))
            print('+ Itb(',i-1,',',j-1,') = ','round(((',matrix_news[i-1][j-1],' + ',matrix_news[i-1][j],' + ',matrix_news[i-1][j+1],' + ',matrix_news[i][j-1],' + ',matrix_news[i][j],' + ',matrix_news[i][j+1],' + ',matrix_news[i+1][j-1],' + ',matrix_news[i+1][j],' + ',matrix_news[i+1][j+1],')/9))= ',int(bien))

        matrix_cuoi.append(matrancon)
    print("Sau khi lọc trung bình ta được : ")
    print("Ma trận cũ" )
    for i in range(len(matrix2)):
        print(matrix2[i])
        
    print("Ma trận mới" )
    for i in range(len(matrix_cuoi)):
        print(matrix_cuoi[i])
def trungvi():
    print("Lọc trung vị: ")
    print("- Áp dụng công thức ta được kết quả:")
    matrix_cuoi = []
    for i in range(1,len(matrix_news)-1):
        matrancon = []
        for j in range(1,len(matrix_news[i])-1):
            bien = [matrix_news[i-1][j-1],matrix_news[i-1][j],matrix_news[i-1][j+1],matrix_news[i][j-1],matrix_news[i][j],matrix_news[i][j+1],matrix_news[i+1][j-1],matrix_news[i+1][j],matrix_news[i+1][j+1]]
            print('+ M(',i-1,',',j-1,') = Median(',sorted(bien),') = ',sorted(bien)[4])
            matrancon.append(sorted(bien)[4])
        matrix_cuoi.append(matrancon)
    print("Sau khi lọc trung vị ta được : ")
    print("Ma trận cũ ")
    for i in range(len(matrix2)):
        print(matrix2[i])
        
    print("Ma trận mới ")
    for i in range(len(matrix_cuoi)):
        print(matrix_cuoi[i])
trungbinh()
trungvi()