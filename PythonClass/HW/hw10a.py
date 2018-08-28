def f2(lst):
    ret = list(filter(lambda x: x % 2 == 1, lst))
    print(ret)


# odd 의 위치 합
def f4(lst):
    tmp = 0
    a = list(filter(lambda x: x[1] % 2 == 1, list(enumerate(lst))))
    for i in range(len(a)):
        tmp += a[i][0]
    print(tmp)


def f6(lst):
    print(max(lst))


def f8(a, b, n):
    # pass
    print(*list(filter(lambda x: x % n == 0, range(a, b + 1, 1))), sep='\n')


def f10(n):
    print(*list(map(lambda x: '*' * x, range(1, n + 1))), sep='\n')


def f12(lst):
    print(all(map(lambda x: x < 0, lst)))


def f14(lst):
    print(list(filter(lambda x: x[1] < 0, enumerate(lst)))[-1][0])  # List를 뒤에서 접근할때 -1 로 가면 뒤에서 부터 접근한다


import math


def f18(n):
    print(math.factorial(n))


def f20(matrix):
    print(list(enumerate(matrix)))
    print(*list(map(lambda x: x[1][x[0]], enumerate(matrix))), sep='\n')


def test(lst):
    print(list(map(lambda x: x * x if (x > 0) else x * 10, lst)))


def f12_gs(lst):
    print(all(map(lambda x: x < 0, lst)))


def f16(n):
    print(*list(map(lambda x: '*' * x, range(n, 0, -1))), sep='\n')


def f22(lst):
    # lambda x:print(x , end='') , range(lst , 0 , -1)
    # print(*list(map(lambda x:list(range(x,-1,-1)) , lst)) , sep='\n')
    print(*list(map(lambda x: list(range(x, -1, -1)), lst)), sep='\,')


def f24(n):
    print(*list(filter(lambda x: x % 2 == 0 or x % 3 == 0, range(1, n + 1))), sep='\n')


def f26(lst):
    # print(list(sorted(lst))[-2])
    print(list(map(lambda x: x, sorted(lst)))[-2])


def f28(lst):
    print(*list(map(lambda x: max(x), lst)), sep='\n')


if __name__ == '__main__':
    f28([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    f28([[3, 2, 1], [0, -1, -2]])
    f28([[1, 2, 3, 4], [1], [34], [2], [3], [56], [67]])
    # f26([1,4,3,2,5])
    # f26([3,2])
    # f26([3,4])
    # test([1,2,-3,4])
    # f24(10)
    # f24(1)
    # f24(3)
    # f22([1,3,5])
    # f20([[1]])
    # f20([[1,0],[0,1]])
    # f20([[1,2,3],[4,5,6],[7,8,9]])
    # f18(3)

    # f16(3)
    # f16(2)
    # f16(1)
    # f14([1,2,-3])
    # f14([1,-2,-3,1,-2,-3])
    # f14([-1,1,1,1])
    # f12_gs([-1,-1,-1])

    # f10(1)
    # f10(2)
    # f10(3)

    # f8(1,10,2)
    # f8(1,10,11)
    # f8(1,10,7)

    # f6([1,2,3,4])
    # f6([1,2,3,4,5])

    # f4([1,2,3,4])
    # f4([1,2,3,4,5])

    # f2([1,2,3,4])
    # f2([1,2,3,4,5])
