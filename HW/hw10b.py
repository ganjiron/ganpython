
def f6(matrix):
    # print(*list(lambda x : x += matrix[x][y] , matrix[0],))
    print(sum(list(map(lambda x:sum(x) , matrix))))

def f8(matrix):
    for i in range(0 , len(matrix)):
        print(*list(filter(lambda  x: x%2 , matrix[i])), sep=' ')
if __name__ == '__main__':
    # f8([[1,2,3] , [4,5,6]])
    f6([[1,2,3],[4,5,6]])