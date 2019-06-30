pos=0
zer=0
neg=0
print("Enter -1 to exit ")
while(1):
    num=int(input("Enter :"))
    if num==-1:
        break
    if num==0:
        zer=zer+1
    elif num>0:
        pos=pos+1
    else:
        neg=neg+1
print("Positives :",pos)
print("Negatives :",neg)
print("Zeroes :",zer)
