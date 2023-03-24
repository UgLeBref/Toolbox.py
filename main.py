import os, sys

os.system("clear")
os.system("figlet -f larry3d Toolbox")

# Afficher le menu
print("Menu :")
print("1. Collecte d'information.")
print("2. Scan des vulnérabilités.")
print("3. Google Dorks")
print("4. ")
print("0 . Arreter le programme.")
choix = input("Saisir l'option : ")

if choix == "1":
    os.system("python3 Info.py")

if choix == "2":
    os.system("python Vuln.py")

if choix == "3":
    os.system("python Dorks.py")

elif choix == "0":
    print("Fin du programme.")
    sys.exit()

else:
    os.system("python main.py")

input("Continuer")
