import os

os.system("clear")
os.system("figlet -f larry3d Info")

print("Menu :")
print("1. Détection des hôtes.")
print("2. Scan des ports d'un hôte.")
print("3. Scan complet d'un hôte.")
print("0. Menu principal.")

menu = input("Collecte d'information : ")

if menu == '1':
    os.system("clear")
    ip_add = input("Saisir l'adresse ip du réseau : ")
    mask = input("Saisir le masque réseau : ")
    os.system(f"nmap -sn {ip_add}/{mask}")

elif menu == '2':
    os.system("clear")
    ip_add = input("Saisir l'adresse ip cible : ")
    os.system(f"nmap {ip_add}")

elif menu == '3':
    os.system("clear")
    ip_add = input("Saisir l'adresse ip cible : ")
    os.system(f"nmap -A -O -sV -sC -T4 -oN nmapoutput {ip_add}")

elif menu == '0':
    os.system("python main.py")

else:
    print("\n Erreur : la saisie est incorrecte.")

input("Continuer")
os.system("python3 Info.py")
