from POOensegnants.main_class import *

enseignant1 = class_Enseignts("","")
decrir = enseignant1.decrire("volonte","mukovi")

enseignant_che = enseignant_chercheur("","",0)
print(enseignant1.decrire("volonte","mukovi"),"son  salaire est :",enseignant_che.calcul_salaire_cherch(12))

enseignant_doct = enseignant_doctorat("","",0)
print(enseignant1.decrire("volonte","mukovi"),"son  salaire est :",enseignant_doct.calcul_salaire_doctorat(50))