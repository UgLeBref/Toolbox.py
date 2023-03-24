import os


def info():
    while True:
        os.system("clear")
        os.system("figlet -f larry3d -w 120 Informations")

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
            break

        else:
            print("\n Erreur : la saisie est incorrecte.")

        input("Continuer")


def vuln():
    while True:
        os.system("clear")
        os.system("figlet -f larry3d -w 120 Vulerabilites")

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

        if menu == '0':
            break

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

        else:
            print("\n Erreur : la saisie est incorrecte.")

        input("Continuer")


def dorks():
    while True:
        os.system("clear")
        os.system("figlet -f larry3d -w 120 Google Dorks")

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
            break

        elif menu == '8':
            os.system("clear")
            os.system("python pagodo/ghdb_scraper.py -s -j -i")
            print("Les Fichier sont à jour.")

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

            else:
                print("\n Erreur : la saisie est incorrecte.")

        input("Continuer")


def dnscan():
    while True:
        os.system("clear")
        print("(Saisir 0 pour revenir au menu.)")
        menu = input("Quel domaine scanner : ")
        os.system(f"python dnscan/dnscan.py -d {menu}")
        input("Continuer")


while True:
    os.system("clear")
    os.system("figlet -f larry3d Toolbox")

    # Afficher le menu
    print("Menu :")
    print("1. Collecte d'information.")
    print("2. Scan des vulnérabilités.")
    print("3. Google Dorks")
    print("4. Scan DNS")
    print("0. Arreter le programme.")
    choix = input("Saisir l'option : ")

    if choix == "0":
        print("Fin du programme.")
        break

    elif choix == "1":
        info()

    elif choix == "2":
        vuln()

    elif choix == "3":
        dorks()

    elif choix == "4":
        dnscan()