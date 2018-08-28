from abc import ABC, abstractmethod


class mother():
    def __init__(self):
        self.mom = 'mom'


class father(ABC):
    def __init__(self):
        self.dad = 'dad'

    def ganseos(self, name):
        print(name)

    @abstractmethod
    def testAbstract(self):
        print('asd')
        pass


class child(mother, father):
    __test = 'test'

    def __init__(self, child):
        father.__init__(self)
        # mother.__init__(self)
        super().__init__()
        self.child = child

    def ganseo(self, name, sex):
        print(name, sex)

    def printFamily(self):
        print(self.child)
        print(self.mom)
        # print(self.dad)
        raise Exception

    def __add__(self, other):
        tmp = self.child + " & " + other.child
        return child(tmp)

    def __str__(self):
        return "child is " + self.child

    def testAbstract(self):
        print('as')
        pass


if __name__ == '__main__':
    a = child("ganseo")
    b = child("jina")
    d = child("Eun")
    c = a + b + d
    print(c)
    try:
        c.printFamily()
    except Exception as e:
        print(e)
    print(c._child__test)
    # print(a.dad)
