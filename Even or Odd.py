def printAge(value,myAge):
    while(True):
        print(value)
        value+=2
        if(value>myAge):
            break

myAge = int(input("Enter your age"))
if(myAge%2 == 0):
    printAge(2,myAge)
else:
    printAge(1,myAge)

#x = 1
#for i in ingredients:
#    print('%s %s' % (x, i))
 #   x = x + 1
