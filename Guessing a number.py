import random
num = random.randint(1,100)
while True:
    n = int(input('Enter the number'))
    if n == num:
        print('Whoa! Guessed Right')
        break
    elif n < num:
        print('Try higher')
    elif n>num:
        print('Try Lower')
