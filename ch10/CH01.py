"""
Created on 2018. 7. 11.
박간서
@author: ganseo.park@gmail.com
"""
import math

t1 =()
t2 = (1,)
t3 = (1,2,3)
t4 = ('1' , '2' , ['ab' , 'cd'])

print(t1 , t2 , t3 , t4)

s1 = set([1,2,3])
print(s1)

a = {1:'a'   , 3:'d', 2:'c'}

for k,v in a.items():print(k,v) #ordering �� �⺻������ �ȵǸ�
#ordering �Ϸ��� ordereddic �� ���µ� ���ʿ� ������

a = {2,5,7}
b = {2,5,'kim'}  
# c = {2,5,[3,2]} #�̰� unhashable �̸� ��������. dictionary �� key �� �����ϰ� hashable �� �� �� �ִ�
# d = {2,5,{2,3}} 
print(a,b )

# help(math.sqrt)

def main():
    c = eval(input('in : '))
    f = (9/5)*c+32
    print(c , ' to ' , f)

def fact():
    n = eval(input())
    fact = 1
    for f in range(n,1,-1):
        fact = fact*f
        
    print(fact)

def palindrome():
    var = str(input("input")) 
    var.upper()
    size = len(var)
    
    while(True):
        
    

if __name__ == '__main__':
    fact()
#     main()