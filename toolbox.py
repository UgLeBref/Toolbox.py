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


def dns():
    while True:
        os.system("clear")
        os.system("figlet -f larry3d Recherche de domaine.")
        print("Menu :")
        print("1. DNScan.")
        print("2. Domain Hunter.")
        print("0. Menu principal.")
        menu = input("Recherche de domaine : ")

        if menu == '0':
            break
        elif menu == '1':
            dns_cible = input("Quel est le domaine cible ? :")
            os.system(f"python dnscan/dnscan.py -d {dns_cible}")
        elif menu == '2':
            dns_cible = input("Quel est le domaine cible ? :")
            os.system(f"python domainhunter/domainhunter.py -s {dns_cible}")
        input("Continuer")


def shodan():
    while True:
        os.system("clear")
        os.system("figlet -f larry3d Shodan.")
        print("\nMon ip sur internet : ", end=" ")
        os.system("shodan myip")
        print("\nMenu :")
        print("1. Compter les résultat.")
        print("2. Enregistrer dans un fichier.")
        print("3. Information disponibles sur une IP.")
        print("4. Vue rapide : IP/Ports/Org/Hostname.")
        print("0. Menu principal.")
        menu = input("Shodan : ")

        if menu == '0':
            break
        elif menu == '1':
            name = input("Quel est la recherche ? :")
            os.system(f"shodan count {name}")
        elif menu == '2':
            name = input("Quel est la recherche ? :")
            os.system(f"shodan download recherche_{name} {name}")
        elif menu == '3':
            ip = input("Quel est l'ip cible' ? :")
            os.system(f"shodan host {ip}")
        elif menu == '4':
            name = input("Quel est la recherche ? :")
            os.system(f"shodan search --fields ip_str,port,org,hostnames {name}")
        input("Continuer")


while True:
    os.system("clear")
    os.system("figlet -f larry3d Toolbox")

    # Afficher le menu
    print("Menu :")
    print("1. Collecte d'information.")
    print("2. Scan des vulnérabilités.")
    print("3. Google Dorks.")
    print("4. Recherche de domaine.")
    print("5. Shodan.")
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
        dns()

    elif choix == "4":
        shodan()
