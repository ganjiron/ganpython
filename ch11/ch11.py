import copy


def write():
    myFile = open('C:\\Users\\DS\\Desktop\\foo.txt' , 'w+')

    for i in range(11):
        data = '%d줄\n' % i
        myFile.write(data)

    myFile.close()

def append():
    my = open ('C:\\Users\\DS\\Desktop\\foo.txt' , 'a')

    for i in range(11,20,1):
        data = '%d줄이다\n'%i
        my.write(data)
    my.close()


def myreadline():
    f = open("C:\\Users\\DS\\Desktop\\foo.txt" , 'r')
    f.seek(20)
    while True:
        line = f.readline()
        if not line:break
        print(line , end='')
    # f.close()

def readTest():
    f = open("C:\\Users\\DS\\Desktop\\foo.txt", 'r')
    var = f.read()
    print(var)
    f.close()

def readobj():
    filename = 'p1_digit.txt'

    with open(filename) as f:
        for i in f:
            print(i.rstrip())

def readLinesTest():
    filename = 'p1_digit.txt'

    with open(filename) as f:
        line = f.readlines()
        for i in line:
            print(i.rstrip())

# exception test 해보는 예제
def exceptionTest():
    try:
        x = 5+ "ham"
    except FileNotFoundError:
        pass
    except ZeroDivisionError:
        pass
    except:
        print('damn it')
    finally:
        print("마지막")

def memTest():
    L = [[123],[456],100000]
    S = copy.copy(L)
    print(L)
    print(S)

    L[0],L[1] = L[1],L[0]

    print(L)
    print(S)

    S = ((1,2),2,3)
    print(hash(('abcasdasdasdasdsadadasaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')))
    print(hash(('abcasdasdasdasdsadadasaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')))
    S = set(S)
    print(S)


if __name__ == '__main__':
    memTest()
    # myreadline()
    # readTest()
    # write()
    # readobj()
    # readLinesTest()
    # exceptionTest()