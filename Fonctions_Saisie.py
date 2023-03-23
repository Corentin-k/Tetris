###########################################################
#####            Projet Tetris                     ########
##### Auteur : Corentin KERVAGORET et Jonathan REN ########
#####            Version : 2                       ########
###########################################################
### Toutes les fonctions demandant une saisie de l'utilisateur###
###                Notifiés par un s                          ###
### Fonctions : s_choix_plateau, liste_bloc, s_mode,s_choix_bloc,###
###                 s_positions                              ###

from Bloc import *



'''
    Sélection de la forme du tableau et génération d'une matrice associé à la forme choisi
    Retourne la matrice associé au plateau grille et le plateau choisie sous forme de chaine de caractère
'''


def s_choix_plateau():
    print()
    plateau = ""
    while plateau != "triangle" and plateau != "cercle" and plateau != "losange" :
        plateau = input('Avec quel plateau voulez vous jouer : "triangle", "cercle" ou "losange" : ')
    print()
    # Saisi sécurisé pour ne pas répéter le programme si l'utilisateur se trompe

    print("Voici le plateau de jeu:\n")
    print(" ###########################################\n")
    # Ouverture du fichier en lecture et sauvegarde du plateau dans la variable grille
    grille = [[]]  # sauvegarde du plateau
    fichier = plateau + ".txt"
    with open(fichier, "r") as fichier:
        # Ajout de Coordonnées en haut du tableau (lettres minuscules)
        for i in range(21):
            lettre = chr(ord('a') + i)
            grille[0].append(lettre)
        grille.append([])
        i = 1
        for ligne in fichier:
            # Ajout de coordonnées sur la gauche du tableau (lettres majuscules)
            grille[i].append(chr(ord('A') + i - 1))
            for car in ligne:
                if car != '\n' and car != ' ':
                    grille[i].append(car)
            # Ajout de coordonnées sur la droite du tableau (lettres majuscules)
            grille[i].append(chr(ord('A') + i - 1))
            grille.append([])
            i = i + 1
    # Ajout de Coordonnées en bas du tableau (lettres minuscules)
    for i in range(len(grille[1]) - 2):
        lettre = chr(ord('a') + i)
        grille[-1].append(lettre)
    liste_bloc(plateau)

    return grille, plateau


'''
    Fonction qui permet la création d'une liste qui contiendra l'ensemble des blocs du plateau associée
    Prend en argument "plateau" qui contient la forme du plateau
    Et retourne une matrice contenant la liste de tous les blocs possible pour le plateau
'''


def liste_bloc(plateau):
    # Création d'une liste qui contiendra l'ensemble des blocs du plateau associé
    liste = []
    if plateau == "triangle":
        liste = bloc_triangle()
    if plateau == "losange":
        liste = bloc_losange()
    if plateau == "cercle":
        liste = bloc_cercle()
    return liste


'''
    Fonction qui demande a l'utilisateur le mode de jeu
    Retourne le mode de jeu choisi par l'utilisateur dans une chaîne de caractère  
'''

def s_mode():
    print("Quel module voulez vous choisir ?\n")
    print("1) Afficher à chaque tour de jeu l’ensemble des blocs disponibles et vous en sélectionnez un. \n")
    print("2) Afficher uniquement 3 blocs sélectionnés aléatoirement. \n")
    mode = 0
    # Saisi sécurisé pour éviter de relancer le jeu si l'utilisateur se trompe
    # Le mode doit être un nombre soit 1, soit 2
    while mode != "1" and mode != "2":
        mode = input("En attente de la sélection du mode de jeu.... ")
    print("Ok votre demande a bien été enregistrée")
    return mode

'''
    Fonction qui demande a le nombre de point à atteindre pour gagnez le jeu
    Retourne donc la variable choix_score qui retourne le nombre de point à gagner
    Seul problème, nous n'avons pas réussis a faire une saisie sécurisé car le nombre choisi par l'utiliateur peut être infinis   
'''
def s_choix_score():
    print("En combien de point voulez-vous jouer ?\n")
    niveau=5
    while niveau not in ["1", "2", "3", "4"]:
        niveau = input("Voulez vous un niveau facile (1), moyen (2) ou compliqué (3) ou choisir votre score a atteindre (4) : ")
    if niveau == "1":
        choix_score = 10
    elif niveau == "2":
        choix_score = 40
    elif niveau == "3":
        choix_score = 100
    else:
        zero = 0
        while zero == 0:
            choix_score = int((input("Nouveau score à atteindre : ")))
            if choix_score == 0:
                print("le score ne peut pas être nul")
            else:
                zero = 1
    print()
    print("Le jeu va donc se jouer en", choix_score,"points\n")
    return choix_score

'''
    Fonction qui demande a l'utilisateur le mode de jeu
    Prend en argument la variable nbr qui contient le nombre de bloc que contient chaque plateau
    en fonction du mode de jeu choisi et le mode de jeu 'mode'
    Retourne le mode de jeu choisi par l'utilisateur dans une chaîne de caractère  
'''


def s_choix_bloc(nbr_bloc,mode):
    choix_bloc = "-1.5"
    # Saisie sécurisée pour que le choix du bloc soit compris entre 0 et la longueur de la liste de tous les blocs
    # Eviter que l'utilisateur tape : 'trois', '4,4', ...

    nbr_possible=[]
    # Créée une liste de tous les nombres possibles pour permettre de faire une saisie sécurisé
    for i in range(nbr_bloc+1):
        i = str(i)
        nbr_possible.append(i)
    while choix_bloc not in nbr_possible:
        choix_bloc = input("Quel bloc voulez vous choisir ?")
        if choix_bloc not in nbr_possible:
            print("Ce bloc n'existe pas \n")
        
    choix_bloc = int(choix_bloc)-1  # -1, car les blocs sont rangés dans une matrice

    '''
        if mode == "2":
            while choix_bloc <= "0" or choix_bloc > "3" or len(choix_bloc) >= 2:
                # Pour éviter que ce soit une lettre ou un nombre/lettre soit supérieur à 2 caractères
                choix_bloc = str(input("Quel bloc voulez vous choisir ?"))
                if choix_bloc <= "0" or choix_bloc > "3" or len(choix_bloc) >= 2:
                    print("Ce bloc n'existe pas \n")
        if mode == "1":
            while choix_bloc <= "0" or choix_bloc > str(nbr) or len(choix_bloc) >= 3:
                choix_bloc = str(input("Quel bloc voulez vous choisir ?"))
                if choix_bloc <= "0" or choix_bloc > str(nbr) or len(choix_bloc) >= 3:
                    if "4" <= choix_bloc <= "6" and len(choix_bloc)==1:
                        choix_bloc="0"+choix_bloc # Expliqué dans le rapport
                    else: print("Ce bloc n'existe pas \n")

        choix_bloc = int(choix_bloc) - 1  # -1, car les blocs sont rangés dans une matrice
        '''

    return choix_bloc


'''
    Fonction qui demande a l'utilisateur les positions du bloc
    Prend en argument la matrice grille pour pouvoir vérifié si les coordonnées choisies sont bonnes
    Retourne sous forme de tuple les coordonnées x,y du bloc choisies par l'utilisateur   
'''


# Les lettres minuscules correspondent à l'axe des colonnes et les lettres majuscules à l'axe des lignes
def s_positions(grille):
    position_x = "A"
    position_y = "a"

    # Vérification que la lettre donnée est bien compris dans la grille
    while ord(position_x) < ord(grille[0][0]) or ord(position_x) > ord(grille[0][-1]):
        position_x = "Aa"
        # Saisi sécurisée pour que l'utilisateur n'entre pas 2 lettres
        while len(position_x) >= 2 or len(position_x) == 0:
            position_x = input("Sur quelle colonne voulez vous placer le bloc ? (lettre minuscule) \n")

    while ord(position_y) < ord(grille[1][0]) or ord(position_y) > ord(grille[-2][0] or len(position_y) > 2):
        position_y = "aA"
        # Saisi sécurisée pour que l'utilisateur n'entre pas 2 lettres
        while len(position_y) >= 2 or len(position_y) == 0:
            position_y = input("Sur quelle colonne voulez vous placer le bloc ? (lettre majuscule) \n")

    return position_x, position_y