import math
print ("investment:Calculate the interest over a deposit")
print ("bond: Calculate the payment on a home loan")
userReply = input("Which calculation would you like to do?")
if userReply == "investment":
    md= float (input ("Please enter the amount to deposit: "))
    ir= float (input ("Now the Interest Rate (percentage): "))
    ny= float (input ("And the number of years you want to invest: "))
    invtype= input("Simple or Compound interest?: ")
    if invtype == "Simple":
     total=md *(1+ir*ny)
    elif invtype == "Compound":
     total=md * math.pow((1+ir),ny)
     ans=float(round(total,2))
    print(total)
