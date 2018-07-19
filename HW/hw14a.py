def first_perfect_square(numbers , pos = 0):
    #baseline
    position = pos
    if position == len(numbers):
        print(-1)
        return
    if numbers[position] < 0:
        position += 1
        first_perfect_square(numbers , position)
        return
    #recursive
    # if type(( numbers[pos] ** 0.5 )) == int :
    # if numbers[position] == 9:
    if ( numbers[pos] ** 0.5 ) - int( numbers[pos] ** 0.5 ) == 0:
        print(position)
        return
    else:
        position += 1
        first_perfect_square(numbers , position)
        return

def num_perfect_square(numbers):
    cnt = 0
    for i in range(0,len(numbers)):
        if numbers[i] >=0:
            if numbers[i]**0.5 - int(numbers[i]**0.5) == 0:
                cnt += 1
    print(cnt)

def second_largest(values):
    # a = sorted(values)
    L1 = values[0]
    L2 = values[0]
    for i in values:
        if L1 < i:
            L2 = L1
            L1 = i
        else:
            if i > L2:
                L2 = i
    print(L2)


if __name__ == '__main__':
    second_largest([3,-2,10,-1,5])
    second_largest([-2,1,1,-3,5])
    second_largest([1,2,3,3])
    second_largest(['alpha','gamma','b','d'])
    second_largest([3.1,3.1])
    second_largest([True,False,False,True])
    second_largest([False,False,True])

    # num_perfect_square([])
    # num_perfect_square([0])
    # num_perfect_square([0,1])
    # num_perfect_square(list(range(10)))
    # num_perfect_square([3]*10)
    # num_perfect_square([4]*10)
    # num_perfect_square([-4,-2,0,2,4])

    # first_perfect_square([2,4,6,8,10])
    # first_perfect_square([6,8,10,12,9])
    # first_perfect_square([1,1])
    # first_perfect_square([-6,6,-2,2,-3,3])