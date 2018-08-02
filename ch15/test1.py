class test:
    age = 23
    name = 'Adam'

t = test()
print(t.name , t.age)
print(getattr(test , 'sex' , 'Male'))
print(test.sex)
# print(getattr(test , 'sex' ))