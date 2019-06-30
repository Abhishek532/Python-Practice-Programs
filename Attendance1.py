a=288-6 #Classes attended
b=394-11 #Total classes held

e=0 # New classes attended 
run=1

while (run!=0):
    print("Current Attendance is ",a,"/",b,"=",a*100/b,"%")
    d=int(input("\nEnter number of new classes attended ,press 0 to exit\n"))
    if d!=0:
        a+=d
        b+=d
        e+=d
        print("New classes attended:",e)
    elif d==0:
        run=0
        print("Attendance is ",a,"/",b,"=",a*100/b)
        print("Total Classes :",e)

    
