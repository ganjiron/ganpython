# print(eval('1+2'))
# print(eval("'hi' +'3'"))
# print(eval('divmod(4,3)'))
#
# python = '0123456789'
# print(python[slice(0,9,1)])
#
# items = [1,2,3,4,5]
# squared = list(map(lambda x:x**2 , items))
# print(squared)
#
# def mul(x):
#     return x*x
# def add(x):
#     return x+x
# funcs = [mul , add]
# for i in range(5):
#     val = list(map(lambda x:x(i) , funcs))
#     print(val)
#
# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11,12]
# print(list(map(lambda x,y:x+y , a,b)))
#
# num = range(-5, 5)
# print(list(filter( lambda x: x<0 , num)))
#
# fib = [0,1,1,2,3,5,8,13,21,34,55]
# result = list(filter(lambda x: x%2 , fib))
# print(result)
# result = list(filter(lambda x: x%2 == 0 , fib))
# print(result)
#
# from functools import reduce
# red = reduce(lambda x,y:x+y , [1,2,3,4,5])
# print(red)
#
# a = ['a','b']
# b = [1,2]
# di = dict(zip(a,b))
# print(di)

def f8(a, b, n):
    return list(filter(lambda x: x % n == 0, range(a, b + 1)))


if __name__ == '__main__':
    print(f8(1, 10, 2))
