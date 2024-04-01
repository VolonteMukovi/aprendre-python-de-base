age=int(input("entre votre age"))
compte=0
for age in range(1,age):
    compte=compte+100
    compte=compte+2*age

print(compte)