age=int(input("entre votre age"))
compte=0
for age in range(1,age):
    compte=compte+100
    compte=compte+2*age               

print(compte)
# def moi():
#     print("je suis vd")
# def toi():
#     print("tues vd")

# listfoction=[moi(),toi()]
# for liste in listfoction:
#     print(liste)
# class personne:
#     nom=""
#     age=0
#     def __init__(self,nom,age):
#         self.nom=nom
#         self.age=age
#     def decrir(self,nom,age):
#         self.nom=nom
#         self.age=age
#         print("vous vous appelle {} vous avez {} ans".format(nom,age))


# names=input("entre votre nom")
# ages=int(input("entre votre age"))
# personne1 = personne("volonte",2)
# personne1.decrir(names,ages)
