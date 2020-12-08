inputList = [1,2,3,4,5,6]
sizeOfList = len(inputList)
flag = True
while(flag):
    sizeOf1stList = int(input("Enter size of 1st list: "))
    sizeOf2ndList = int(input("Enter size of 2nd list: "))
    if(sizeOfList >= sizeOf1stList):
        print('Size of 1st List ',inputList[0:sizeOf1stList])
        print('Size of 2nd List ',inputList[sizeOf1stList:sizeOf1stList+sizeOf2ndList])
        print('Size of 3rd List ',inputList[sizeOf1stList+sizeOf2ndList:len(inputList)])
        break
    else:
        print('ERROR: Enter size less than ',sizeOfList)
        
