print ("even Numbers\n")
usrInput=int(input("Enter any number"))

start= usrInput+1 if usrInput&1 else usrInput
x=0
while x < start:
    print (x+2)
    x=x+2