from random import shuffle

def stu(pairs,samples):
    num_correct = 0
    matching = list(range(pairs))

    for i in range(samples):
        shuffle(matching)
        # print(i , matching)
        for j in range(pairs):
            if matching[j] == j:
                num_correct +=1
                # print(i,j , i*j,num_correct)
                break

    return num_correct / samples
a= 10
b = 10
print(stu(a,b*1))
print(stu(a,b*10))
print(stu(a,b*100))
print(stu(a,b*1000))
print(stu(a,b*10000))