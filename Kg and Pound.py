"""left 1-20 pounds
right kg
1 kg = 2.2 pound"""
pd=1
kg=2.2*pd
print("--------------------------------------")
print("|Pound  |\t\t KG")
print("--------------------------------------")

for i in range(1,21):
    print("|",i,"\t|\t" ,round(i*kg,2))

print("--------------------------------------")

