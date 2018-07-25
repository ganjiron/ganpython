import sys

class Person:
    global test
    def __init__(self,name):
        self.name = name


    def SayHel(self):
        global test
        test = 'aaa'
        print('hi' , self.name , test)

    def __del__(self):
        print('%s bye'%self.name , test)

if __name__ == '__main__':
    a = Person('박간서')
    print(sys.getrefcount(a))
    # sys.get_asyncgen_hooks(a)
    a.SayHel()
    print(sys.getrefcount(a))
    a.SayHel()
    print(sys.getrefcount(a))
    # print(a.name , test)
    a1 = a
    print(sys.getrefcount(a))
    a2 = a
    print(sys.getrefcount(a))
    print(a)
    del a
    print(a1)
    del a1
    print(a2)
    del a2
    print(sys.getrefcount(31))

    b = Person('썅')
    b.SayHel()
    # print(dir(a))