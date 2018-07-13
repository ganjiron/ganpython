'''
Created on 2018. 7. 13.

@author: DS
'''

def f2(n , depth=1):
    if n == 1:
        return depth
    
    if n%2 == 0:
        return f2(n//2 , depth + 1)
    else:
        return f2(3*n+1 , depth + 1)
        
def f4(lst):
#     print(lst)
    if lst == []:
        return
    if lst[0] %2 == 1:
        print(lst[0]*3)        
    f4(lst[1:])
    
def f6(lst):
    if lst == [] or type(lst) != list:
        return lst
    elif type(lst[0]) != list:
        return [lst[0]] + f6(lst[1:])
    else:
        return f6(lst[0]) + f6(lst[1:])
    


def f10(list):
    #baseline
    if list == []:
        return 0
        
    #reculsive
    return 1 + f10(list[1:])

def f14(lst):
    print(lst)
    if lst == []:
        return ''
    
    if lst[0] % 2 == 1:
        return lst[0]
    else:
        return f14(lst[1:])

if __name__ == '__main__':
#     print(f2(1))
#     print(f2(6))
#     print(f2(11))
#     print(f2(637228127))
#     f4([1,2,3,4])
#     f4([2,4])
#     f4([11,42,63,15])
    print(f6(['baa']))
    print(f6(['baa' , [4,1,3,[1,3]]]))
    print(f6([]))
    print(f6([[[[[[[[[[23]]]]]]]]]]))
#     print(f10([1,2,3]))
#     print(f10([]))
#     print(f10([2]))
#     print(f14([1,2,3]))
#     print(f14([2,4]))
#     print(f14([2,4,6,8,10,3]))