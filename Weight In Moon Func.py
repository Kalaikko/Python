def weightInMoonFunc(weight,factor):
    i = 0
    while i < 16:
        weightInMoon = weight * 0.165
        print("Weight In Earth: ",weight)
        print("Weight In Moon: ",weightInMoon,"\n")
        weight += 1
        i += 1

weightInMoonFunc(30,0.25)
