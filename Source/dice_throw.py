import random
random.seed()
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for x in range(1,5000):
    random_dec = random.random()
    rand_numb = random.randint(1,6)
    if rand_numb == 1 :
        one = one + 1
    elif rand_numb == 2 :
        two = two + 1
    elif rand_numb == 3 :
        three = three + 1
    elif rand_numb == 4 :
        four = four + 1
    elif rand_numb == 5 :
        five = five + 1
    elif rand_numb == 6 :
        six = six + 1
print ( "calls to 1",one)
print ( "calls to 2",two)
print ( "calls to 3",three)
print ( "calls to 4",four)
print ( "calls to 5",five)
print ( "calls to 6",six)
print ( random_dec )
   
        
