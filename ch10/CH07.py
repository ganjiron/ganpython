'''
Created on 2018. 7. 13.

@author: DS
'''

#factorial recursive function
def factorial(n):
    print(n)
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    
def factorial_d(n , depth=0):
    print(" "*depth , "factorial(",n,"):")
    if n < 2:
        result =1
    else:
        result =  n*factorial_d(n-1 , depth+1)
    print(" "*depth, "->" , result)
    return result
    
#factorial function by iterative style
def factorial_i(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
        
        
def sumlist(items):
    print(items)
    if items == []:
        return 0
    else:
        return items[0] + sumlist(items[1:])      
    
def reverse(s):
#     print(" "*depth , " reverse(" , s , ")")
    if len(s) < 1:
        return ''
    return reverse(s[1:]) + s[0]

def gcd(x,y):
    while(y>0):
        oldX = x
        x=y
        y = oldX % y
    return x

def gcd_r(x,y):
    if (y ==0):
        return x
    else:
        return gcd_r(y , x%y)
    

if __name__ == '__main__':
#     print(factorial(3))
#     print(factorial_i(3))
#     print(sumlist([1,2,3,4,5,6,7,8,9]))
#     print(reverse('hello'))
#     print(factorial_d(5))
    print(gcd(4,2))
    print(gcd_r(4,2))