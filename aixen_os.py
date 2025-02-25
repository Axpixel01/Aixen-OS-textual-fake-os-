# RPG Textuel en développement...
# Aixen OS V1.4
# MAJ log : Ajout de mini-jeux...

import time
import random

start = input("Voulez-vous démarrer le système ? O/N : ")

if start == ("O"):
    print("Très bien, démarrage en cours...")
    print("Démarrage : 0%")
    time.sleep(2)
    print("Démarrage : 25%")
    time.sleep(2)
    print("Démarrage : 50%")
    time.sleep(2)
    print("Démarrage : 75%")
    time.sleep(2)
    print("Démarrage : 100%")
    print("Système démarré.")
    time.sleep(2)
    print("Bienvenue à Aixen OS. Le faux OS textuel. Démarrons...")
    time.sleep(1)
    utilisateur = input("Veuillez entrer votre nom d'utilisateur : ")
    if utilisateur == ("Aixen") or ("Test"):
        print("Nom d'utilisateur appliqué.")
        time.sleep(1)
        print("Téléchargement des applications...")
        time.sleep(5)
        print("Applications Téléchargées.")
        time.sleep(1)
        print("Bienvenue {}.".format(utilisateur))
        time.sleep(1)
        navigation = input("Que voulez-vous faire ? \n- Aller sur internet \n- Ouvrir Forza Horizon 5 \n- Ouvrir GTA X \n- Jouer a Yandere Simulator <3 \n- Cities : Skylines II  \n- Aixen Minigames \n- Log de Màj \n- ??? \n")
        if navigation == ("Aller sur internet"):
            Opera_GX = input("Sur quel site veut-tu aller ? \n- Youtube.com \n- Roblox.com \n- Pornhub.com \n- autre.com \n ")
            if Opera_GX == ("Youtube.com"):
                yt_navigation = input("A quel jeu voulez-vous jouer ? Fil de recommandations : \n- J'ai passé 24h dans un bunker de la IIcnd guerre mondiale ! de MrBeast \n- J'ai testé Slimera ! de Aixen \n- Pourquoi la lune s'éloigne de la terre ? De Science Trash \n")
                if yt_navigation == ("J'ai passé 24h dans un bunker de la IIcnd guerre mondiale !"):
                    print("Ok")
                elif yt_navigation == ("J'ai testé Slimera !"):
                    print("Très bon choix !")
                elif yt_navigation == ("Pourquoi la lune s'éloigne de la terre ?"):
                    print("Bon choix")
                else:
                    print("Vidéo non trouvée.")
            elif Opera_GX == ("Roblox.com"):
                rblx_navigation = input("A quel jeu voulez-vous jouer ? \n- Slimera \n- Fabled Legacy \n")
                if rblx_navigation == ("Slimera"):
                    print("Ok.")
                elif rblx_navigation == ("Fabled Legacy"):
                    print("Ok.")
                else:
                    print("Jeu non trouvé.")
            elif Opera_GX == ("Pornhub.com"):
                print("Ok.")
            elif Opera_GX == ("autre.com"):
                print("Ok.")
            else:
                print("Erreur inconnue.")
        elif navigation == ("Log de Màj"):
            print("Voici le dernier log de Mise à Jour d'Aixen OS v1.4 : \n- Ajout de mini-jeux")
        elif navigation == ("Aixen Minigames"):
            aixen_minigame_main_menu = input("A quel mini-jeu voulez-vous jouer ? \n- Aixen RPG \n- Aixen's Calculs \n- Arabe Simulator \n")
            if aixen_minigame_main_menu == ("Arabe Simulator"):
                arabe_simulator_first = input("Souhaitez-vous faire exploser le C4 ? \n- Oui \n- Non \n")
                if arabe_simulator_first == ("Oui"):
                    print("ALlaH AkBAr !!! ({} à fait explosé un C4 en criant : 'ALlaH AkBAr !!!')".format(utilisateur))
                elif arabe_simulator_first == ("Non"):
                    print("Az toi")
            # RPG textuel à développer
            elif aixen_minigame_main_menu == ("Aixen RPG"):
                print("En cours de développement...")
            elif aixen_minigame_main_menu == ("Aixen's Calculs"):
                calcul1_défi = input("Combien font 4+4 ?")
                if calcul1_défi == ("8"):
                    print("Bonne réponse !")
                else:
                    print("Et non ! La réponse étais évidemment 8 !")
            else:
                print("Erreur, jeu non-trouvé.")
        elif navigation == ("???"):
            puzzle = input("Choisissez deux salles : \n- Salle des ténèbres \n- Salle de la Lumière \n")
            if puzzle == ("Salle des ténèbres"):
                print("Mauvais choix. Votre vie sera remplis de mauvaises choses.")
            elif puzzle == ("Salle de la lumière"):
                print("...")
                time.sleep(5)
                print("Excellent choix {}. Votre vie sera malheureuse, mais belle et récompensée à la fin.".format(utilisateur))
        elif navigation == ("Ouvrir Forza Horizon 5"):
            print("Démarrage...")
            time.sleep(2)
            print("Optimisation pour votre pc... (10%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (20%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (30%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (40%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (50%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (60%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (70%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (80%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (90%)")
            time.sleep(2)
            print("Optimisation pour votre pc... (100%)")
            time.sleep(1)
            print("Démarrage du jeu...")
            time.sleep(1)
            print("Jeu lancé.")
            voiture_choix = input("Choisissez une voiture : ")
            print("Voiture choisie.")
        elif navigation == ("Cities : Skylines II"):
            print("Démarrage...")
            time.sleep(1)
            print("Chargement en cours... (10%)")
            time.sleep(1)
            print("Chargement en cours... (20%)")
            time.sleep(1)
            print("Chargement en cours... (30%)")
            time.sleep(1)
            print("Chargement en cours... (40%)")
            time.sleep(1)
            print("Chargement en cours... (50%)")
            time.sleep(1)
            print("Chargement en cours... (60%)")
            time.sleep(1)
            print("Chargement en cours... (70%)")
            time.sleep(1)
            print("Chargement en cours... (80%)")
            time.sleep(1)
            print("Chargement en cours... (90%)")
            time.sleep(1)
            print("Chargement en cours... (100%)")
            time.sleep(1)
            print("Démarrage du jeu...")
            time.sleep(1)
            cities2 = input("MENU : \nCréer une Nouvelle partie \nCharger une partie")
            if cities2 == ("Créer une Nouvelle partie"):
                print("Partie créer.")
            elif cities2 == ("Charger une partie"):
                villes = input("Choisissez une sauvegarde : \nVille de merde \nVille tryhard \nJsp chef")
                if villes == ("Ville de merde"):
                    print("Azé")
                elif villes == ("Ville tryhard"):
                    print("Vz")
                elif villes == ("Jsp chef"):
                    print("Bruh")
        elif navigation == ("Ouvrir GTA X"):
            print("Erreur, le fichier local nommé gta_x_play.exe n'est pas reconnu.")
        elif navigation == ("Jouer a Yandere Simulator <3"):
            print(":)")
        else:
            print("Erreur inconnue.")
    else:
        print("Erreur inconnue.")   
elif start == ("N"):
    print("Annulation du processus de démarrage.")
else:
    print("Erreur, Arguments non-reconnus.")