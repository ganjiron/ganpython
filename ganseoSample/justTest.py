class JustCounter():
    # global secretCount
    secretCount = 0
    def __init__(self , cnt=0):
        global secretCount
        secretCount = cnt
        # self.cnt = cnt
        pass

    def count(self , cnt = 0):
        global secretCount
        secretCount += cnt
        # JustCounter.secretCount += cnt
        # print(secretCount)

    def printCnt(self):
        global secretCount
        print(secretCount)
        # print(JustCounter.secretCount)

    @classmethod
    def printClass(cls):
        print(JustCounter.secretCount)
        pass

if __name__ == '__main__':
    counter1 = JustCounter(1)
    counter1.printCnt()
    counter1.count(3)
    counter1.printCnt()
    counter2 = JustCounter(2)
    counter1.printCnt()
    counter2.printCnt()
    counter2.count(4)
    counter1.printCnt()
    # print(JustCounter.secretCount)
    JustCounter.printClass()