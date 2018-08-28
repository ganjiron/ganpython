class test:
    age = 23
    name = 'Adam'


class A:
    def f(self):
        return self.g()

    def g(self):
        return 'a'


class B(A):
    def g(self):
        return 'b'


from abc import ABC


class AB(ABC):
    pass


if __name__ == '__main__':
    a = A()
    b = B()
    print(a.f(), b.f())
    print(a.g(), b.g())

# t = test()
# print(t.name , t.age)
# print(getattr(test , 'sex' , 'Male'))
# print(test.sex)
# print(getattr(test , 'sex' ))
