a=288-6
b=394-11
d=0
print("Current percentage is",a*100/b,"%")
c=int(input("Enter percentage needed :"))

while (1):
    if c==100: #100% not possible if even 1 class is missed,causes crash
        break
    if (a*100/b)>=c:
        break
    
    else:
        a+=1
        b+=1
        d+=1

print("You need to attend",d,"classes to get",c,"% attendance")
    
