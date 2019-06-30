for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

print("------------------")

for i in range(1,8):
    for j in range(i,8):
        print(j,end="")
    for k in range(i):
        if k==0:
            continue
        print(k,end="")
    print()

print("------------------")

for i in range(1,6): 
    for j in range(1,i+1):
        if i%2==1:
            print(j%2,end=" ")
        elif i%2==0:
            print((j+1)%2,end=" ")
        
            
    print()

print("------------------")

x=1
for i in range(1,6):
    for j in range(1,i+1):
        print(x,end=" ")
        x+=1
    print()

print("------------------")
n=int(input("Enter a number :"))
print("1.All upto",n,"?")
print("2.Only",n,"?")
x=int(input("Choice :"))
if x==1:    
    for i in range(1,n+1):
        for j in range(1):
            if i%2==0:
                print(i,"is not prime")
            elif i==1:
                print(i,"is neither prime nor composite")
            elif i%2==1:
                for k in range(2,i):
                    if i%k==0:
                        print(i,"is not prime")
                        break
                else:
                    print(i,"is prime")
elif x==2:
    if n==1: 
        print("Neither Prime nor Composite")
    elif n%2==0: #for even numbers
        print(n,"is not prime")
    elif n%2==1:
        for i in range(2,n):
            if n%i==0:
                print(n," is not prime")
                break
        else:
            print("Prime")
else:
      print("Invalid Input")
print("------------------")

    


        
        


