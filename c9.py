userInput=input("Enter String")
cCount=0
wCount=1
for i in userInput:
    cCount=cCount+1
    if i==' ':
        wCount=wCount+1
print("No of words:",wCount)
print("No of characters:",cCount)        