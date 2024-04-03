
class class_Enseignts:
    nom = ""
    postnom = ""

    def __init__(self,co_nom,co_postnom):
        self.nom = co_nom
        self.postnom = co_postnom

    def decrire(self,de_nom,de_postnom):
        self.nom = de_nom
        self.postnom = de_postnom
        description = "Lenseignat {}  {}",de_nom,de_postnom
class enseignant_chercheur(class_Enseignts):
    heure_complem_cherch = 0
    def __init__(self, co_nom, co_postnom,co_heure_complem_cherch):
        class_Enseignts.__init__(self,co_nom,co_postnom)
        self.heure_complem_cherch = co_heure_complem_cherch

    def calcul_salaire_cherch(heure_complem_cherch):
        if(heure_complem_cherch>192):
            resultat=(2000*12)+heure_complem_cherch*40
            return resultat
        elif(heure_complem_cherch<=192):
            resultat=(2000*12)
            return resultat
class enseignant_doctorat(class_Enseignts):
    def __init__(self, co_nom, co_postnom,co_heure_doctorat):
        class_Enseignts.__init__(self,co_nom,co_postnom)
        self.heure_doctorat = co_heure_doctorat
    
    def calcul_salaire_doctorat(heure_doctorat):
            if(heure_doctorat<=96):
                resultat=heure_doctorat*30
                return resultat
            
            elif(heure_doctorat>96):
                resultat=96*30
                return resultat
print("fin du programme de classe")