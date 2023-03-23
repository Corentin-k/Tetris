###########################################################
#####            Projet Tetris                     ########
##### Auteur : Corentin Kervagoret et Jonathan REN ########
#####            Version : 2                       ########
###########################################################

####################################################################################################

########################### Vérification de la position ########################################
"""
    Fonction permettant de verifier si la position choisie par l'utilisateur est bonne
    Arguments : Le bloc choisi (bloc)
                Alea : liste des trois blocs aléatoire si le mode de jeu vaut 2
                x et y la position choisie par l'utilisateur
                grille : la grille de jeuS
                mode : Le mode de jeu choisi par l'utilisateur
    Retourne un booléen en fonction si la position choisie est valable
"""


def valider_position(bloc, alea, x, y, grille, mode, liste):
    if mode == "2":
        h = 0
        for i in range(len(liste[alea[bloc]]) - 1, 0, -1):
            for j in range(len(liste[alea[bloc]][i])):
                if (liste[alea[bloc]][i][j] == 1) and (grille[ord(y) - 64 - h][ord(x) - 96 + j] == "0" or (grille[ord(y) - 64 - h][ord(x) - 96 + j] > chr(64) and grille[ord(y) - 64 - h][ord(x) - 96 + j] < chr(122)) or grille[ord(y) - 64 - h][ord(x) - 96 + j] == "2"):
                    return False

            h = h + 1
        return True
    if mode == "1":
        h = 0
        for i in range(len(liste[bloc]) - 1, 0, -1):

            for j in range(len(liste[bloc][i])):

                if liste[bloc][i][j] == 1 and (grille[ord(y) - 64 - h][ord(x) - 96 + j] == "0" or (grille[ord(y) - 64 - h][ord(x) - 96 + j] > chr(64) and grille[ord(y) - 64 - h][ord(x) - 96 + j] < chr(122)) or grille[ord(y) - 64 - h][ord(x) - 96 + j] == "2"):

                    return False
            h = h + 1
        return True

########################### Placement du bloc choisi  ########################################


"""
    Fonction permettant de placé le bloc choisi a l'emplacement x,y
    Arguments : Le bloc choisi (bloc)
                Alea : liste des trois bloc aléatoire si le mode de jeu vaut 2
                x et y la position choisie par l'utilisateur
                grille : la grille de jeu
                mode : Le mode de jeu choisi par l'utilisateur
    Aucun retour mais affichage de la grille a la fin et modification de a grille
"""


def placer_bloc(bloc, alea, x, y, grille, mode, liste):
    if mode == "2":
        h = 0
        for i in range(len(liste[alea[bloc]])-1, 0, -1):
            for j in range(len(liste[alea[bloc]][i])):
                if liste[alea[bloc]][i][j] == 1:
                    grille[ord(y)-64 - h][ord(x)-96 + j] = "2"  # Placement du bloc donc modification des 1 en 2
            h = h+1

    if mode == "1":
        h = 0
        for i in range(len(liste[bloc]) - 1, 0, -1):
            for j in range(len(liste[bloc][i])):
                if liste[bloc][i][j] == 1:
                    grille[ord(y) - 64 - h][ord(x) - 96 + j] = "2"  # Placement du bloc donc modification des 1 en 2
            h = h + 1

########################### Mise a jour du score  ########################################


'''
    Fonction qui met a jour le score a chaque fois qu'un pion est supprimé
    Utilise une variable global : score 
    Prend en argument un str en fonction de si on veut afficher le score ou mettre à jour le score
    et retourne le score mise a jour a chaque appel dans les fonction clearLig et clearCol
'''

score = 0


def mise_a_jour_score(var):
    global score
    if var == "Affichage":
        return score
    else:
        score = score + 1

########################### Vérification des lignes du plateau  ########################################


'''
    Fonction booléen qui permet de vérifier si une ligne est remplie ou pas.
    Retourne la liste (Lig) de toutes les lignes remplies
'''


def etat_lig(grille):
    etatlig = True
    lig = []
    for x in range(1, len(grille)-1):
        for j in range(len(grille[x])):
            if grille[x][j] == "1":
                etatlig = False
        if etatlig is True:
            lig.append(x)  # liste qui va contenir toute les ligne qui ne comporte pas de "1"
        etatlig = True
    return lig  # retourne les lignes complétées

########################### Suppression des lignes du plateau  ########################################


'''
    Fonction qui nettoie la grille dans le cas où une ligne est remplie 
    et accorde un score par rapport au nombre de case "éliminé"
    
    Argument : La liste lig qui contient toutes les lignes à supprimer
'''


def effacer_lig(lig, grille):
    # Changement de tous les 2 de la ligne en 1 pour supprimer les pions
    for i in lig:
        for j in range(1, len(grille[1])-1):
            if grille[i][j] == "2":
                grille[i][j] = "1"
                mise_a_jour_score("score")

    # Descendre toutes les lignes au-dessus de celle(s) supprimée(s)
    if lig is not []:
        for nbr in range(len(lig)):
            for i in range(lig[nbr], 2, -1):
                for j in range(1, len(grille[1])):
                    if grille[i][j] == "1" and grille[i-1][j] == "2":
                        grille[i][j] = grille[i-1][j]
                        grille[i-1][j] = "1"
                    elif grille[i][j] == "0" and grille[i-1][j] == "2":
                        grille[i-1][j] = "1"
    return grille


########################### Vérification des colonnes du plateau  ########################################
'''
    Fonction booléen qui permet de vérifier si une ligne est remplie ou pas.
    Retourne la liste Col de toutes les colonnes remplies
'''


def etat_col(grille):
    # Changement de tous les 2 de la colonne en 1 pour supprimer les pions
    etatcol = True
    col = []
    for i in range(1, len(grille[1])-1):
        for y in range(1, len(grille)-1):
            if grille[y][i] == "1":
                etatcol = False
        if etatcol is True and i not in col:
            col.append(i)  # Liste qui contient toutes les colonnes qui ne comportent pas de "1"
        etatcol = True

    return col

########################### Suppression des colonnes du plateau  ########################################


'''
    Fonction qui nettoie la grille dans le cas où une colonne est remplie 
    et accorde un score par rapport au nombre de case "éliminé"

    Argument : La liste Col qui contient toutes les colonnes à supprimer
'''

# Fonction qui nettoie la grille dans le cas où une colonne est remplie et accorde un score par rapport au nombre de case(s) "annulée(s)"


def effacer_col(col, grille):
    for i in range(1, len(grille)-1):
        for j in col:
            if grille[i][j] == "2":
                grille[i][j] = "1"
                mise_a_jour_score("score")
    return grille

#########################################################################