import os

os.system("clear")
os.system("figlet -f larry3d Databases")

print("Menu :")
print("1. Scipvul db.")
print("2. CVE.")
print("3. Security Focus.")
print("4. Xforce.")
print("5. Exploit db.")
print("6. Openvas.")
print("7. Security Tracker.")
print("8. OSV db.")
print("9. Rechercher dans toutes les bases.")
print("0. Menu principal.")

menu = input("Base de données de vulnérabilités : ")
ip_add = input("Saisir l'adresse ip cible : ")
os.system("clear")

if menu == '1':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=scipvuldb.csv -sV {ip_add}")

elif menu == '2':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=cve.csv -sV {ip_add}")

elif menu == '3':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=securityfocus.csv -sV {ip_add}")

elif menu == '4':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=xforce.csv -sV {ip_add}")

elif menu == '5':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=exploitdb.csv -sV {ip_add}")

elif menu == '6':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=openvas.csv -sV {ip_add}")

elif menu == '7':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=securitytracker.csv -sV {ip_add}")

elif menu == '8':
    os.system(f"nmap --script vulscan/ -script-args vulscandb=osvdb.csv -sV {ip_add}")

elif menu == '9':
    os.system(f"nmap --script vulscan/ -sV {ip_add}")

elif menu == '0':
    os.system("python main.py")

else:
    print("\n Erreur : la saisie est incorrecte.")

input("Continuer")
