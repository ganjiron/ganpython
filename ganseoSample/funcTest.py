
class FuncTest():
    def __init__(self):
        self.funcName = [self.aaa, self.bbb, self.ccc]
        pass

    def aaa(self):
        print('aaa')

    def bbb(self):
        print('bbb')

    def ccc(self):
        print('ccc')

class Func(FuncTest):
    def __init__(self):
        super().__init__()
        self.funcName.append(self.ddd)

    def ddd(self):
        print('ddd')


if __name__ == '__main__':
    tmp = Func()
    for i in range(len(tmp.funcName)):
        tmp.funcName[i]()
