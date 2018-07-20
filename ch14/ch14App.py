# from random import randint
import random
# a = [random.randint(0,99) for i in range(99)]
# print(a)
# print(random.choice(a))
# print(random.choice(a))
# random.shuffle(a)
# b = random.shuffle(['a','b','c'])
# print(b)
# print(a)

def shu():
    a = [lambda x:x , range(24)]
    b = [lambda x:x , range(24)]
    count = 0
    while True:
        random.shuffle(a)
        if a == b:
            print(count)
            break
        count +=1

ra = random.random() < 0.4
print(ra)

class Base():
    def printX(self):
        print('ham')

class Inhe(Base):
    pass

if __name__ == '__main__':
    a = Inhe()
    a.printX()