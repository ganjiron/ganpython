'''
Created on 2018. 7. 11.

@author: DS
'''

def f2(args):
    size = len(args)
    pointer = 0;
    for n in args:
        if(n%2 == 1):
            print(n)
            pointer += 1
            if(pointer ==size):
                break
            
def f2_doc(lst):
    for i in range(0,len(lst)):
        if lst[i] % 2 == 1:
            print(lst[i])
            
def f4(lst):
    addPointer = 0
    for n in range(0 , len(lst)):
        if lst[n]%2 == 1:
            addPointer += n
    print(addPointer)
            
def f6(lst):
    largest = 0;
    for n in range(0 , len(lst)):
        if largest < lst[n]: 
            largest = lst[n] 
    print(largest)
     
def f8(a,b,n):
    for i in range(a,b):
        if i % n == 0:
            print(i)

def f10_1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*" , end='')
        print()

def f10_2(n):
    for i in range(0,n):
        print('*' * (i+1))
        
def f12(list):
    ret = 'True'
    for n in list:
        if n > 0:
            ret = 'False'
    print(ret)
        
def f14(lst):
    for n in range(len(lst)-1 , -1 , -1):
        if lst[n] < 0:
            print(n)
            return
        
def f16(n):
    for i in range(n+1, 0, -1):
        for j in range(i-1):
            print('*' , end='')
        print()

def f18(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    print(result)

def f20(list):
    for n in list:
        for i in range (n , -1 , -1):
            print(i , end=' ')
        print()

def f22(n):
    for i in range(1 , n+1):
        if i %2 ==0 or i%3 ==0:
            print(i)

def f24(list):
    first , second = 0,0
    for n in list:
        if n >= second:
            if n >= first:
                second = first
                first = n
            else:
                second = n
    print(second)
        
def f26(lst):
    top = 0
    for n in range(0,len(lst)):
        for m in range(0,len(lst[n])):
            if top < lst[n][m]:
                top = lst[n][m]
        print(top)
        top = 0    
    
                  

if __name__ == '__main__':
#     f2([1,2,3,4,5])
#     f2_doc([1,2,3,4,5])
    
#     f4([1,2,3,4])
#     f4([1,2,3,4,5])
#     
#     f6([1,2,3,4])
#     f6([1,2,3,4,5])
#  
#     f8(1,10,2)
#     f8(1,10,11)
#     f8(1,10,7)   
# 
#     f10_1(1)
#     f10_1(2)
#     f10_1(3)
#      
#     f10_2(1)
#     f10_2(2)
#     f10_2(3)

#     f12([])
#     f12([-1,-2,-3,-4,5])
#     f12([1,2,3,4,5])
#     f12([-1,-2,-3])

#     f14([1,2,-4])
#     f14([1,-2,-3,1,-2,-3])
#     f14([-1,1,1,1])

#     f16(3)
#     f16(2)
#     f16(1)
#     
#     f18(0)
#     f18(2)
#     f18(3)

#     f20([])
#     f20([1,3,5])
#     f20([5,3,6,2])
#
#     f22(10)
#     f22(1)
#     f22(3)

    # f24([1,4,3,2,5])
    # f24([3,2])
    # f24([3,4])

#     f26([[1,2,3],[4,5,6],[7,8,9]])
#     f26([[3,2,1],[0,-1,-2]])
#     f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]])
    