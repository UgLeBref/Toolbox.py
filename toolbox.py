import os


def info():  # La fonction info est le menu qui permet la collecte d'informations
    while True:  # Boucle infinie pour relancer le menu après chaque utilisation
        os.system("clear")  # Vide l'invité de commande pour une meilleure lisibilité
        # appel de figlet qui créé les bannières que l'on voit en haut des menus
        os.system("figlet -f larry3d -w 120 Informations")

        print("Menu :")  # affichage du menu
        print("1. Détection des hôtes.")
        print("2. Scan des ports d'un hôte.")
        print("3. Scan complet d'un hôte.")
        print("0. Menu principal.")

        menu = input("Collecte d'informations : ")  # récupération de l'option choisie par l'utilisateur

        # En fonction de l'option choisie par l'utilisateur, on lance la commande associée
        if menu == '1':  # option 1 scan les hôtes présents sur le réseau choisi
            os.system("clear")
            ip_add = input("Saisir l'adresse ip du réseau : ")
            mask = input("Saisir le masque réseau : ")
            os.system(f"nmap -sn {ip_add}/{mask}")

        elif menu == '2':  # option 2 lance un nmap sans aucune option sur l'IP choisi pour scanner les ports
            os.system("clear")
            ip_add = input("Saisir l'adresse ip cible : ")
            os.system(f"nmap {ip_add}")

        elif menu == '3':  # option 3 affiche des informations supplémentaires et enregistre grâce à -oN nmapoutput
            os.system("clear")
            ip_add = input("Saisir l'adresse ip cible : ")
            os.system(f"nmap -A -O -sV -sC -T4 -oN nmapoutput {ip_add}")

        elif menu == '0':  # ici si l'utilisateur a choisi 0 on quitte la boucle et la fonction se termine
            break

        else:  # quand l'utilisateur saisi une option qui ne fait pas partie du menu
            print("\n Erreur : la saisie est incorrecte.")

        input("Continuer")


def vuln():  # La fonction vuln correspond au menu scan des vulnérabilités
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

        # ici chaque if envoie la même commande avec une base de données différente
        # la commande permet d'utiliser le script vulscan développé pour améliorer nmap
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


def dorks():  # La fonction dorks correspond au menu Google Dorks
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

        menu = input("Quels Google Dorks analyser ? : ")

        if menu == '0':
            break

        elif menu == '8':
            os.system("clear")
            # ghdb_scrapper.py est le programme qui récupère les fichiers Dorks à jour
            os.system("python pagodo/ghdb_scraper.py -s -j -i")

        else:
            # si l'utilisateur veut faire une recherche, on lui demande un domaine cible
            cible = input("Quel est le domaine cible : ")

            # Chaque commande lance Pagodo.py avec un fichier Dorks différent sauf la 1 qui les recherche tous
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


def dns():  # correspond au menu Recherche de domaine
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
        os.system("shodan myip")  # On affiche notre IP publique
        print("\nMenu :")
        print("1. Compter les résultats.")
        print("2. Enregistrer dans un fichier.")
        print("3. Information disponibles sur une IP.")
        print("4. Vue rapide : IP/Ports/Org/Hostname.")
        print("0. Menu principal.")
        menu = input("Shodan : ")

        if menu == '0':
            break
        elif menu == '1':
            name = input("Quel materiel chercher ? :")
            os.system(f"shodan count {name}")  # la fonction pour compter les résultats
        elif menu == '2':
            name = input("Quel materiel chercher ? :")
            os.system(f"shodan download recherche_{name} {name}")  # la fonction pour télécharger le résultat
        elif menu == '3':
            ip = input("Quelle est l\'ip cible ? :")
            os.system(f"shodan host {ip}")  # la fonction pour cibler un hôte précis
        elif menu == '4':
            name = input("Quel materiel chercher ? :")
            os.system(f"shodan search --fields ip_str,port,org,hostnames {name}")  # la fonction qui affiche les infos
        input("Continuer")


while True:  # boucle infini
    os.system("clear")
    os.system("figlet -f larry3d Toolbox")

    # Afficher le menu principal
    print("Menu :")
    print("1. Collecte d'informations.")
    print("2. Scan des vulnérabilités.")
    print("3. Google Dorks.")
    print("4. Recherche de domaine.")
    print("5. Shodan.")
    print("0. Arreter le programme.")
    choix = input("Saisir l'option : ")  # demande le choix de l'utilisateur

    if choix == "0":
        print("Fin du programme.")
        break  # ce break met fin au programme

    # chaque autre if lance une fonction qui correspond au menu choisi
    elif choix == "1":
        info()

    elif choix == "2":
        vuln()

    elif choix == "3":
        dorks()

    elif choix == "4":
        dns()

    elif choix == "5":
        shodan()
