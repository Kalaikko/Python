weightInEarth = int(input("Enter your weight"))
i = 0
while i < 16:
    weightInMoon = weightInEarth * 0.165
    print("Weight In Earth: ",weightInEarth)
    print("Weight In Moon: ",weightInMoon,"\n")
    weightInEarth += 1
    i += 1
