import random
import time

class Sort_GS():
    def __init__(self):
        self.cnt = 0
        pass

    def ranNum(self , n , rangeS , rangeE):
        ret = []
        for i in range(n):
            ret.append(random.randint(rangeS , rangeE))
        return ret

    # Selection Sort
    def selSort(self , nums):
        n = len(nums)
        num = nums

        # start_time = time.time()
        for bottom in range(n - 1):
            mp = bottom
            for i in range(bottom + 1, n):
                self.cnt += 1
                if num[i] < num[mp]:
                    mp = i
            num[bottom], num[mp] = num[mp], num[bottom]
        # print("start_time", start_time)
        # print("selSort:{0} ,{1}번 compare {1} seconds ---".format(n  , comp , time.time() - start_time))
        return num

    def msort(self , lst):
        if len(lst) == 0 or len(lst) == 1:
            return lst[:len(lst)]

        halfway = len(lst)//2
        list1 = lst[0:halfway]
        list2 = lst[halfway:len(lst)]
        newList1 = self.msort(list1)
        newList2 = self.msort(list2)
        newList = self.merge(newList1 , newList2)
        return newList

    def merge(self,a,b):
        index_a = 0
        index_b = 0
        c = []
        self.cnt +=1
        while index_a < len(a) and index_b < len(b):
            self.cnt += 1
            if a[index_a] <= b[index_b]:
                c.append(a[index_a])
                index_a = index_a + 1
            else:
                c.append(b[index_b])
                index_b = index_b + 1
        c.extend(a[index_a:])
        c.extend(b[index_b:])
        return c

    def bubbleSort(self , items):
        tmp = items
        for i in range(len(tmp)):
            for j in range(len(tmp)-1-i):
                self.cnt+=1
                if tmp[j] > tmp[j+1]:
                    tmp[j] , tmp[j+1] = tmp[j+1],tmp[j]
        return tmp

    def insertion_sort(self,items):
        tmp = items
        for i in range(len(tmp)):
            j=i

            while j>0 and tmp[j]<tmp[j-1]:
                self.cnt += 1
                tmp[j],tmp[j-1] = tmp[j-1],tmp[j]
                j-= 1
        return tmp

    def quickSort(self,items):
        tmp = items
        if len(tmp) > 1:
            pivot_index = len(tmp) //2
            smaller_items = []
            larger_items=[]

            for i,val in enumerate(tmp):
                if i != pivot_index:
                    self.cnt+=1
                    if val < tmp[pivot_index]:
                        smaller_items.append(val)
                    else:
                        larger_items.append(val)
            self.quickSort(smaller_items)
            self.quickSort(larger_items)
            tmp[:] = smaller_items + [tmp[pivot_index]]+larger_items
        return tmp


if __name__ == '__main__':
    # a = ranNum(100, 1, 100000)
    sor = Sort_GS()
    a = sor.ranNum(10, 1, 10)

    # a = random.randrange(1,1000000)
    # start_time = time.time()
    # sor.cnt = 0
    # sor.selSort(a.copy())
    # print("selSort cnt:{1} : {0} seconds ---".format(time.time() - start_time , sor.cnt ))
    #
    # start_time = time.time()
    # sor.cnt = 0
    # sor.msort(a.copy())
    # print("msort cnt:{1} : {0} seconds ---".format(time.time() - start_time, sor.cnt))
    #
    # start_time = time.time()
    # sor.cnt = 0
    # sor.bubbleSort(a.copy())
    # print("bubbleSort cnt:{1} : {0} seconds ---".format(time.time() - start_time, sor.cnt))
    #
    # start_time = time.time()
    # sor.cnt = 0
    # sor.insertion_sort(a.copy())
    # print("insertion_sort cnt:{1} : {0} seconds ---".format(time.time() - start_time, sor.cnt))

    # start_time = time.time()
    # sor.cnt = 0
    # sor.quickSort(a.copy())
    # print("quickSort cnt:{1} : {0} seconds ---".format(time.time() - start_time, sor.cnt))
    #
    start_time = time.time()
    sorted(a.copy())
    print("sorted cnt:{1} : {0} seconds ---".format(time.time() - start_time, sor.cnt))


