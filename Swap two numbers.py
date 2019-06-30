a=10
b=15
a,b = b,a

print (a)
print (b)

a=10
b=5
print ("Original numbers are :" ,a,"and",b)
a=a+b
b=a-b
a=a-b
print ("Swapped numbers are :" ,a,"and",b)

a = 10
b = 5
print ("Numbers before swapping are :", a,",",b)
a = a^b
b = a^b
a = a^b
print ("Numbers after swapping are :", int(a),",",int(b))


