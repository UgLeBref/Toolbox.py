import os

os.system("clear")
os.system("figlet -f Toolbox")

# Afficher le menu
print("Menu :")
print("1. Collecte d'information.")
print("2. Scan des vulnérabilités.")
print("3. ")
print("4. ")
print("5 . Arreter le programme.")
choix = input("Saisir l'option : ")

if choix == "1":
    os.system("python3 Info.py")

if choix == "2":
    os.system("python Vuln.py")

elif choix == "5":
    print("Fin du programme.")
    exit()

else:
    os.system("python main.py")

input("Continuer")
