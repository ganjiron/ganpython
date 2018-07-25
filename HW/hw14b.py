def count_matches(somelist , value ):
    # pos = position
    if somelist == []:
        return 0
    if somelist.pop() == value:
        return 1 + count_matches(somelist , value )
    else:
        # position += 1
        return count_matches(somelist , value )

def double_each(some_list , position = 0):
    ret = []
    if position == len(some_list):
        return []
    ret.append(some_list[position])
    ret.append(some_list[position])
    return ret + double_each(some_list , position+1)

def sums_to(nums,k):
    if nums == [] and k == 0:
        return True
    elif nums == [] and k != 0:
        return False
    else:
        k -= nums[0]
        return sums_to(nums[1:] , k)

def is_reverse(string1 , string2):
    if string1 == '' and string2 == '':
        return True
    elif string1 == '' or string2 == '':
        return False
    else:
        if string1[0] == string2[-1] :
            return is_reverse(string1[1:] , string2[0:-1])
        else:
            return False

def sort_repeated(L):
    s = set()
    for i in range(len(L)):
        if L[i] in L[i+1:]:
            s.add(L[i])
    print(sorted(list(s)))

def makeDick(lst):
    tmp = dict()
    if len(lst) == 1: #base
        tmp[lst[0]] = 1
        # print(tmp)
        return tmp
    tmp.update(makeDick(lst[1:]))
    #recursive
    if lst[0] in tmp.keys() :
        tmp[lst[0]] += 1
    else:
        tmp[lst[0]] =1
    return tmp

def mostF(lst):
    tmp = makeDick(lst)
    print(max(tmp , key=tmp.get))
    print(max(tmp.values()))

def histogram(letters):
    # print(letters)
    a = list(letters.values())
    dicTmp = dict()
    for i in a:
        dicTmp[i] = a.count(i)
    return dicTmp


if __name__ == '__main__':
    letters = {1:'a' , 2:'b' , 3:'a'}
    print(histogram(letters))
    letters = {1: 'a', 2: 'b', 3: 'c'}
    print(histogram(letters))
    print(letters)
    letters[4]  ='a'
    letters[5] = 'b'
    letters[6] = 'a'
    print(letters)
    print(histogram(letters))
    # print(makeDick([2,5,3,4,6,4,2,4,5]))
    # mostF([2, 5, 3, 4, 6, 4, 2, 4, 5])
    # lst = [1,2,3]
    # tmp = dict()
    # tmp[lst[0]] = 1
    # print(tmp)
    # sort_repeated([3,1,2,3,2,1])
    # print(is_reverse('abc' , 'cba'))
    # print(is_reverse('abc', 'abc'))
    # print(is_reverse('abc', 'dcba'))
    # print(is_reverse('abc', 'cb'))
    # print(is_reverse('', ''))

    # nums = [1,2,3]
    # print(sums_to(nums, 6))
    # print(sums_to(nums, 5))
    # print(sums_to([], 1))

    # print(double_each(nums))
    # print (nums)
    # print(double_each([]))
    # print(count_matches([0,1,0,4,2,0],0))