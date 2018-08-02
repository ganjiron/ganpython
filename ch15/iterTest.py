class IterableClass():
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index  = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        # print('test')
        return n

    def gen(self):
        yield list(range(5))
        yield list(range(5,10))
        yield list(range(10,15))

if __name__ == '__main__':
    ite = IterableClass()
    for i in ite:
        print(i)

    for j in ite.gen():
        print(j)
