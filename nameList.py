nameList=[]

while True:
    name=input("Input Student name: ").lower()
    if name == "stop":
        break
    nameList.append(name)

print ("Students:" ,nameList)    