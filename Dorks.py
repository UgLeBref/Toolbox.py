import os

os.system("clear")
os.system("figlet -f larry3d Pagodo")

print("Menu :")
print("1. Tous les Google Dorks disponibles.")
print("2. Mots de passe.")
print("3. Noms de comptes.")
print("4. Données sensibles de commerce en ligne.")
print("5. Portails de connexion.")
print("6. Fichiers vulnérables.")
print("7. Serveurs vulnérables.")
print("8. MàJ des Google Dorks.")
print("0. Menu principal.")

menu = input("Quels Google Dorks analyser : ")

if menu == '0':
    os.system("python main.py")
else:
    cible = input("Quel est le domaine cible : ")

    if menu == '1':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/all_google_dorks.txt")

    elif menu == '2':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/files_containing_passwords.dorks")

    elif menu == '3':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/files_containing_usernames.dorks")

    elif menu == '4':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/sensitive_online_shopping_info.dorks")

    elif menu == '5':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/pages_containing_login_portals.dorks")

    elif menu == '6':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/vulnerable_files.dorks")

    elif menu == '7':
        os.system("clear")
        os.system(f"python pagodo/pagodo.py -s -d {cible} -g pagodo/dorks/vulnerable_servers.dorks")

    elif menu == '8':
        os.system("clear")
        os.system("python pagodo/ghdb_scrapper.py -s -j -i")

    else:
        print("\n Erreur : la saisie est incorrecte.")

    input("Continuer")
    os.system("python Dorks.py")