

listOfMountains = ["Mount Evetes", "Timpanogoes","Provo Peak","Volcano"]

print("Oh it was a sunny morning but than something terrible happend the "+listOfMountains[3]+" erupted!")

Dormant_Volcano = listOfMountains.pop(3)

print(listOfMountains)


Old_Volcano = [Dormant_Volcano,"DeadMountain"]

print(Old_Volcano)

del Old_Volcano[-1]

print(Old_Volcano)

listOfMountains.append("DeadHorseMountain")

print(listOfMountains)

listOfMountains.insert(2,"Sunshine Mountain")

print(listOfMountains)

listOfMountains.sort()

print(listOfMountains)

listOfMountains.sort(reverse=True)

print(listOfMountains)

listOfMountains.reverse()

sorted(listOfMountains)

print(listOfMountains)

listOfMountains.remove("Sunshine Mountain")


print(listOfMountains)