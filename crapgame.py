import random
print("game started")
first = random.randrange(1,7)
print("your first number is ", first)
second = random.randrange(1,7)
print("your second number is ", second)
sum = first+second
print("your sum is", sum)
if ((sum==11) or (sum==7)):
    print("you won")
elif (sum==2 or sum==3 or sum==12):
    print("crap: casino won")
else:
    print(sum, "is your goal number, now you should roll the dice till u roll the goal number again")
    goal = sum
    first = random.randrange(1,7)
    second = random.randrange(1,7)
    sum = first+second
    while (sum!=goal):
        if(sum==7):
            print("you lose")
            break
        first = random.randrange (1,7)
        second = random.randrange (1,7)
        sum = first+second
    print("you won")
