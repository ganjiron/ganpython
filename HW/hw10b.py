
def f6(matrix):
    # print(*list(lambda x : x += matrix[x][y] , matrix[0],))
    print(sum(list(map(lambda x:sum(x) , matrix))))

def f8(matrix):
    for i in range(0 , len(matrix)):
        print(*list(filter(lambda  x: x%2 , matrix[i])), sep=' ')
import math
def f2(n):
    tmp = 1
    # print( math.factorial(n) )
    # print(list(map(lambda x: sum(range(x+1)) , range(1,n+1))) )
    a = list(map(lambda y: range(sum(range(y + 1)) - y + 1, sum(range(y + 1))+1), range(1, n + 1)))
    for i in a:
        print(*list(map(lambda x:x , i)) , sep = ' ')
    # print(list(map(lambda y : range(sum(range(y+1))-y+1 , sum(range(y+1))), range(1 , n+1) )))
def f2_s(n):
    cnt = 1
    for i in range(n):
        for j in range(i+1):
            print(cnt , end=' ')
            cnt = cnt+1
        print()

def f4_s(n):
    cnt = 1
    for i in range(n):
        for j in range(i+1):
            print(cnt , end=' ')
            cnt = cnt+1
        print()
    for i in range(n-1):
        for j in range(n-i-1):
            print(cnt, end=' ')
            cnt = cnt + 1
        print()
def f4(n):
    # b = list(map(lambda x: range(1, n + 1) if x < n + 1 else range(n, 1, -1), range(1, n * 2)))
    # print(b)
    # a = list(map(lambda y: range(sum(range(y + 1)) - y + 1, sum(range(y + 1)) + 1) if y < n+1 else range(sum(range(y + 1)), sum(range(y + 1))),
    #              list(map(lambda x: range(1, n+1) if x < n+1 else range(n , 1 , -1) , range(1 , n*2 )))))
    # print(a)
    # for i in a:
    #     print(*list(map(lambda x: x, i)), sep=' ')
    a = n**2
    print(range(1 , n**2+1) , range(1,n+1) , range(n , 0 ,-1))
    print(*list(map(lambda x: range(1,x+1) if x < n+1 else range(x , 0 ,-1) , range(1 , n**2+1))))

if __name__ == '__main__':
    # f4_s(4)
    f4(5)
    # f2(3)
    # f2(0)
    # f2(1)
    # f2(10)
    # f2_s(10)

    # f8([[1,2,3] , [4,5,6]])
    # f6([[1,2,3],[4,5,6]])