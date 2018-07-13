'''
Created on 2018. 7. 11.

@author: ganseo.park
'''

def f2(n):
    pointer = 1
    for i in range(n):
        for j in range(i+1):
            print(pointer , end=' ')
            pointer+=1
        print()

def f4(n):
    tmp = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(tmp , end=' ')
            tmp +=1
        print()
    for i in range(n-1,0,-1):
        for j in range(0,i):
            print(tmp,end=' ')
            tmp +=1
        print()

def f6(matrix):
    pointer = 0
    for n in range(0 , len(matrix)):
        print(matrix[n][pointer])
        pointer +=1

def f8(matrix):
    tmp = 0
    for n in range(0 , len(matrix)):
        for m in range(0 ,len(matrix[n])):
           tmp += matrix[n][m]
    print(tmp)

def f10(matrix):
    for n in range(0 , len(matrix)):
        for m in range(0 , len(matrix[n])):
            if(matrix[n][m]%2 ==1):
                print(matrix[n][m] , end=' ')
        print()

def f12(matrix1 , matrix2):
    tmpMat = []
    inn = []
    for n1 in range(0,len(matrix1)):
        tmp = 0
        for m1 in range(0 , len(matrix1[n1])):
            # print(matrix1 , matrix2 , matrix1[n1][m1] , matrix2[m1][n1])
            tmp += matrix1[n1][m1] * matrix2[m1][n1]
        inn.append(tmp)
        # print(inn)
    tmpMat.append(inn)
    print(tmpMat)

def f14(rows , cols):
    tmp = 0
    tmpx = []
    tmpy = []
    for i in range(rows):
        for j in range(cols):
            if j+1 < cols: tmp+=1
            if j-1 >= 0 : tmp +=1
            if i+1 < rows : tmp += 1
            if i-1 >= 0 : tmp += 1
            tmpx.append(tmp)
            tmp = 0
        tmpy.append(tmpx)
        tmpx = []
    print(tmpy)


if __name__ == '__main__':
    # f14(3,3)
    # f14(5,1)
    # f14(5,0)
    # f14(0,5)
    # f14(2,2)
    # f12([[1,0],[0,1]],[[1,0],[0,1]])
    # f12([[1,2,3],[4,5,6]],[[-1,-1],[-1,-1],[-1,-1]])
    # f12([[4,3,2,1]],[[1],[2],[3],[4]])
    # f10([[1,0],[0,1]])
    # f10([[1,2,3],[4,5,6]])
    # f10([[1],[2],[3],[4]])
    # f8([[1,0],[0,1]])
    # f8([[1,2,3],[4,5,6]])
    # f8([[1],[2],[3],[4]])


    # f6([[1,0] , [0,1]])
    # f6([[1,2,3],[4,5,6],[7,8,9]])
    # f6([[1]])
    # f4(3)
    # f4(0)
    # f4(1)
    # f2(3)
    # f2(0)
    # f2(1)
    # f2(5)