import sys

class Person:
    'ganseo'
    test = 'aaa'
    def __init__(self,name):
        self.name = name


    def SayHel(self):
        global test

        print('hi' , self.name , self.test)

    @classmethod
    def classPerson(cls):
        cls.test = 'ccc'

    def __del__(self):
        # self.test = 'bbb'
        print('%s bye'%self.name , self.test)

if __name__ == '__main__':
    a = Person('박간서')
    a.SayHel()
    b = Person('썅')
    Person.classPerson()
    print(Person.__dict__)
    b.SayHel()
    int('1')
    # print(sys.getrefcount(a))
    # # sys.get_asyncgen_hooks(a)

    # print(sys.getrefcount(a))
    # a.SayHel()
    # print(sys.getrefcount(a))
    # # print(a.name , test)
    # a1 = a
    # print(sys.getrefcount(a))
    # a2 = a
    # print(sys.getrefcount(a))
    # print(a)
    # del a
    # print(a1)
    # del a1
    # print(a2)
    # del a2
    # print(sys.getrefcount(31))


    # print(dir(a))