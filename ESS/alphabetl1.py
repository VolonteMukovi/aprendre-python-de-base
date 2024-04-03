import os
import shutil
# feilllessimple = ["calptuse","anana","levre"]
# feilllescompose = ["jus","pelouse","avoca"]

# fell=input("entre la famiile de votre feillle")
# if(fell=="simple"):
#     for i in range(0,len(feilllessimple)):
#         print("")
#     print("\n", feilllessimple)
# elif(fell=="compose"):
#      for i in range(0,len(feilllescompose)):
#         print(i,feilllescompose)



# Chemin du dossie
# Chemin du dossier où vous souhaitez organiser les fichiers
dossier_cible = "D:\z"

#Créez les dossiers de A à Z
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for lettre in lettres:
    chemin_dossier = os.path.join(dossier_cible, lettre)
    os.makedirs(chemin_dossier, exist_ok=True)
    print(lettre,lettres)# Choisissez le dossier source contenant vos fichiers
dossier_source = "E:\English musics"

# Parcourez les fichiers dans le dossier source
for nom_fichier in os.listdir(dossier_source):
    chemin_fichier_source = os.path.join(dossier_source, nom_fichier)
    if os.path.isfile(chemin_fichier_source):
        # Obtenez la première lettre du nom de fichier
        premiere_lettre = nom_fichier[0].upper()
        # Vérifiez si le dossier de destination existe
        if premiere_lettre in lettres:
            chemin_dossier_destination = os.path.join(dossier_cible, premiere_lettre)
            # Déplacez le fichier vers le dossier de destination
            shutil.move(chemin_fichier_source, chemin_dossier_destination)
            print(f"Le fichier '{nom_fichier}' a été déplacé vers '{chemin_dossier_destination}'.")

print("Organisation terminée !")
