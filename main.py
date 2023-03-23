import os

os.system("clear")

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
    ip_add = input("Saisir l'adresse ip cible : ")
    os.system(f"nmap -sV --script=vulscan/ {ip_add}")

elif choix == "5":
    print("Fin du programme.")

else:
    print("Choix invalide")

input("Continuer")
