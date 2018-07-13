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

def f6(matrix):
    pointer = 0
    for n in range(0 , len(matrix)):
        print(matrix[n][pointer])
        pointer +=1
    

if __name__ == '__main__':
#     f2(3)
#     f2(0)
#     f2(1)
#     f2(5)

    f6([[1,0] , [0,1]])
    f6([[1,2,3],[4,5,6],[7,8,9]])
    f6([[1]])