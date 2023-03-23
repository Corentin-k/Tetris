###########################################################
#####            Projet Tetris                     ########
##### Auteur : Corentin Kervagoret et Jonathan REN ########
#####            Version : 2                       ########
###########################################################

###### Toutes les fonctions qui permettent un affichage #########
###                Notifiés par un a                          ###
### Fonctions : a_afficher_grille, a_afficher_bloc, A_bloc_aleatoire ###


####################################################################################################

import random  # utilisation de la bibliothèque random pour la fonction A_bloc_aleatoire

'''
    Affichage des régles du jeu
    Prend en argument le choix du score pour pouvoir modifier le score à atteindre 
    si le jouer le modifie
'''
def a_regle(choix_score) :
    print("Voici les règles du jeu :\n")
    print("Le jeu consiste à remplir les lignes et les colonnes d'un plateau de jeu grâce à des blocs. \n"
          "A chaque fois que vous remplissez une colonne ou une ligne, celle-ci se supprime, "
          "et vous gagnez autant de points que de pions supprimés.\n"
          "Si une ligne est supprimée toutes les lignes au-dessus descendent d'une ligne.\n"
          )
    print("Vous avez la possibilité entre trois plateaux : le triangle, le losange ou le cercle.\n")
    print("Vous avez également un mode de jeu à choisir : \n")
    print("\t - Un mode de jeu où vous pouvez afficher tous les blocs possibles pour la grille choisie.")
    print("\t - Et un autre ou vous aurez le choix entre 3 blocs choisis aléatoirement. \n")
    print("Vous avez 3 tentatives pour placer correctement un bloc sinon le jeu s'arrête.  \n"
          "Vous avez la possibilité d'arrêter le jeu après avoir placé un bloc. \n \n"
          "Attention : Le bloc se place de façon à ce que le point le plus en bas à gauche, du bloc à afficher,"
          " se place à la position que vous allez choisir !!! \n\n"
          "Le jeu se joue en", choix_score, "points.(Pourra être modifié une fois le jeu lancé) \n\n"
                                             "BONNE CHANCE !\n")
    lance = input("Appuyez sur entrée pour retourner au menu...")  # Pause dans le programme
    print()

################### Affichage de la grille #####################################################
'''
    Affichage de la matrice grille
    Prend en argument la matrice pour pouvoir la parcourir et l'afficher
'''


def a_afficher_grille(grille):
    # Affichage du plateau
    print('  ', end='')
    # Parcours de chaque ligne de la matrice
    for ligne in range(len(grille)-1):
        # Parcours de chaque colonne de la matrice
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne] != '0' and grille[ligne][colonne] != '1' and grille[ligne][colonne] != '2':
                print(grille[ligne][colonne], end=' ')
            elif grille[ligne][colonne] == '1':
                # 25FC 2B1B \U00002B1B \U00002B1C □ \U000025A0
                print('\U000025A1', end=' ')
            elif grille[ligne][colonne] == '0':
                # 25FB  \U00002B1C ■ \U000025A1
                print('.', end=' ')
            elif grille[ligne][colonne] == '2':
                print("■", end=' ')
        print()
    print('  ', end='')
    # Affichage de la dernière ligne de la matrice, lettres majuscules en bas du tableau
    for colonne in range(len(grille[-1])):
        print(grille[-1][colonne], end=' ')

    print()
    print()

################### Affichage des blocs POLITIQUE 1 #####################################################


"""
    Affichage de tous les bloc associés au plateau
    Correspondant a la politique numéro une du jeu
    Argument : plateau : la forme du plateau choisie
    et la liste de tous les bloc a affiché en fonction du plateau
"""


def a_afficher_bloc(liste, plateau):
    print("Voici les blocs proposés: ")
    # Pour afficher les blocs manquants après les 30, déjà affiché
    if plateau == "triangle":
        fin = 1  # 31 blocs dans la liste du triangle, il manquera donc un bloc à afficher
    if plateau == "losange":
        fin = 4  # 34 blocs dans la liste du losange, il manquera donc 4 blocs à afficher
    if plateau == "cercle":
        fin = 2  # 32 blocs dans la liste du losange, il manquera donc 2 blocs à afficher
    indice = 1  # indice pour pouvoir afficher un numéro à chaque bloc
    # Parcours de toute la liste des blocs et affichage des 30 premiers blocs
    for k in range(0, len(liste)-fin, 10):
        for i in range(5):

            for l in range(10):
                if i == 0:
                    if indice < 10:
                        # Affichage d'un indice sur les premieres lignes (i=0) et devant chaque bloc
                        print(" " + str(indice) + ") ", end='')
                    else:
                        print(str(indice) + ") ", end='')
                else:
                    print("    ", end='')
                for j in range(5):
                    if liste[k+l][i][j] == 1:
                        print('\U000025A0', end=' ')
                    elif liste[k+l][i][j] == 0:
                        print('.', end=' ')
                print('  ', end='')
                if i == 0:
                    indice += 1
            print()

        print()
    # Affichage des blocs manquants
    for i in range(5):
        for k in range(len(liste)-fin, len(liste)):
            if i == 0:
                if indice < 9:
                    print(" " + str(indice) + ") ", end='')
                else:
                    print(str(indice) + ") ", end='')
            else:
                print("    ", end='')
            for j in range(5):
                if liste[k][i][j] == 1:
                    print('\U000025A0', end=' ')
                elif liste[k][i][j] == 0:
                    print('.', end=' ')
            if i == 0:
                indice += 1
        print()

    print()

################### Affichage des blocs POLITIQUE 2#####################################################


"""
    Affichage aléatoire de 3 bloc associé au plateau
    Et retourne la liste des numéros des trois bloc choisis aléatoirement
    Utilisation de la bibliothèque random
"""


def a_bloc_aleatoire(liste):
    # Afficher les blocs possibles option 2
    print("Voici les blocs proposés: ")
    alea = []  # Variable qui va contenir 3 blocs sélectionnés aléatoirement
    x = int
    for k in range(3):  # ajout des nombres aléatoires dans la liste aléa
        x = random.randint(0, len(liste)-1)  # incrémentation d'un nombre généré aléatoirement
        if x in alea:  # Pour ne pas avoir trois chiffres identiques
            x = random.randint(0, len(liste) - 1)
        alea.append(x)
    # Affichage des trois blocs aléatoires
    for i in range(5):
        if i == 0:
            print("1) ", end='')
        else:
            print("   ", end='')
        # Bloc 1
        for j in range(len(liste[alea[0]][i])):

            if liste[alea[0]][i][j] == 1:
                print('\U000025A0', end=' ')
            elif liste[alea[0]][i][j] == 0:
                print('.', end=' ')
        print("  ", end='')
        if i == 0:
            print("2) ", end='')
        else:
            print("   ", end='')
        # Bloc 2
        for j in range(len(liste[alea[1]][i])):

            if liste[alea[1]][i][j] == 1:
                print('\U000025A0', end=' ')
            elif liste[alea[1]][i][j] == 0:
                print('.', end=' ')
        print("  ", end='')
        if i == 0:
            print("3) ", end='')
        else:
            print("   ", end='')
        # Bloc 3
        for j in range(len(liste[alea[2]][i])):
            if liste[alea[2]][i][j] == 1:
                print('\U000025A0', end=' ')
            elif liste[alea[2]][i][j] == 0:
                print('.', end=' ')
        print()
    print()

    return alea  # retourne la liste des blocs aléatoires

####################################################################################################

