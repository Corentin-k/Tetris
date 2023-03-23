###########################################################
#####            Projet Tetris                     ########
##### Auteur : Corentin KERVAGORET et Jonathan REN ########
#####            Version : 2                       ########
###########################################################

# Importation des modules et des fichiers nécessaires au fonctionnement du programme

from Fonction import *
from Fonctions_Saisie import *
from Fonctions_Affichage import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    choix = 4
    choix_score = 30  # initialisation du score à 30, pourra être modifié

    ### Page d'accueil
    print()
    print("Bonjour, Bienvenue dans le jeu Tetris 2.0\n")
    while choix!= "2" :
        print("MENU : \n")
        print("- Tapez 1 si vous voulez voir les règles du jeu ")
        print("- Tapez 2 si vous voulez commencer le jeu")
        print("- Tapez 3 si vous voulez modifier le score \n")

        # Position de deux choix avant de commencer le jeu afficher les règles ou commencer

        choix = (input("Que voulez-vous faire ? "))
        print()
        if choix == "1":
            a_regle(choix_score)
        if choix== "3":
            # Sélection du score
            choix_score = s_choix_score()
    

    print("Le jeu va commencer...\n")

    # Sélection du mode de jeu
    mode = s_mode()


    # Ouverture du fichier et stockage de la matrice
    grille, plateau = s_choix_plateau()  # variable qui va prendre la forme du plateau
    a_afficher_grille(grille)
    liste = liste_bloc(plateau)
    print(" ###########################################")
    
    print("\nTous vos choix ont été pris en compte : \nVous allez jouer avec le mode", mode + ", sur le plateau :", plateau,
          "et vous devez atteindre un score de", choix_score, "points pour gagner.")
    print(input("Bonne chance, le jeu est prêt à commencer, appuyez sur entrée..."))
    print()

    # Permet de calculer le nombre de tests pour placer un bloc
    Arret = False  # Variable pour arrêter le programme si l'utilisateur le demande
    alea = []     # initialisation de la liste mais sera inutile si l'option choisie est 1 et sera remplie avec
                  # la fonction bloc_aleatoire

    # Boucle qui s'arrête que si l'utilisateur le demande ou que le score atteigne un certain niveau
    while Arret is False and mise_a_jour_score("Affichage") < choix_score:

        if mode == "2":
            alea = a_bloc_aleatoire(liste)
            nbr_bloc = len(alea)  # Permettra de faire une saisie sécurisée pour le choix du bloc

        if mode == "1":
            a_afficher_bloc(liste, plateau)

            nbr_bloc = len(liste_bloc(plateau))  # Permettra de faire une saisie sécurisée pour le choix du bloc

        # Affichage du plateau
        a_afficher_grille(grille)

        print("Vous avez", mise_a_jour_score("Affichage"), "point(s)")  # -1 car on relance la fonction update_score

        # Sélection du bloc par l'utilisateur
        choix_bloc = s_choix_bloc(nbr_bloc,mode)

        Compteur = 0
        position = False

        # Boucle qui s'arrête que si l'utilisateur ne se trompe pas dans les coordonnées
        # (coordonnées valides et position valide)
        while 3 > Compteur >= 0 and position is False:

            position_x, position_y = s_positions(grille)  # Demande de la position du bloc
            # Vérification de la position
            position = valider_position(choix_bloc, alea, position_x, position_y, grille, mode, liste)

            if position is True:  # Positioner le bloc si l'emplacement est valide
                placer_bloc(choix_bloc, alea, position_x, position_y, grille, mode, liste)
                a_afficher_grille(grille)  # Affichage de la grille modifiée
                Compteur = -1
            elif position is False:  # Sinon on augmente le compteur pour pouvoir arrêter le jeu au bout de 3 tentatives
                Compteur += 1
                print()
                print("Impossible de placer ce bloc à cet endroit")
                print("Il vous reste", 3-Compteur, "tentatives")
                print()

        effacer_col(etat_col(grille), grille)
        effacer_lig(etat_lig(grille), grille)

        if Compteur == 3:  # Arrêt du jeu si l'utilisateur s'est trompé 3 fois
            print("Perdu")
            print("Vous avez gagnez", mise_a_jour_score("Affichage"), "points")
            Arret = True
        else:  # Sinon on regarde si l'utilisateur veut arrêter de jouer
            arret = input("Voulez-vous arrêter de jouer ? O/N")
            if arret == "oui" or arret == "O" or arret == "Oui" or arret == "o":
                Arret = True

                print("Vous avez gagnez", mise_a_jour_score("Affichage"), "points")
                print("A bientôt")

        print()

    if Arret is False :
        a_afficher_grille(grille)
        print("Vous avez gagnez", mise_a_jour_score("Affichage"), "points\n")
        print("Bravo vous avez gagnez")
