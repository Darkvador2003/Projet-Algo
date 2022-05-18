# -*- coding: utf-8 -*-
def test_victoire(grille_pos):
    """
    Parcours la grille de position donnée en entrée et vérifie s'il y a encore des bateaux en jeu.
    S'il n'y a plus de bateaux sur la grille. Alors un joueur a gagné.
    """
    presence_bateau = False
    for k in range (len(grille_pos)):
        for i in range (len(grille_pos)):
            if grille_pos[k][i] != 0:
                presence_bateau = True
    return presence_bateau  

def init_bateau():
    """
    Permet au(x) joueur(s) de sélectionner le nombre de bateaux et leurs taille avec lesquels ils jouent.
    Ces nombres ne peuvent être qu'entre 2 et 6 sinon message d'erreur.
    Retourne une liste de la forme [taille_bateau1, taille_bateau2, taille_bateau3, ...]
    """
    bateaux = []
    nb_bat = input("Combien de bateaux par joueur ? (2-6) :  ")
    while  len(nb_bat) != 1 or ord(nb_bat)<50 or ord(nb_bat)>54:
        print("Vous devez rentrer un nombre compris entre 2 et 6")
        nb_bat = input("Combien de bateaux par joueur ? (2-6) :  ")
    for loop in range(int(nb_bat)):
        taille_bateau = input(f"Quelle taille pour le bateau numéro {loop+1} (entre 2 et 5) :  ")
        while len(taille_bateau) != 1 or ord(taille_bateau)<50 or ord(taille_bateau)>53 :
            print("Veuillez rentrer un nombre compris entre 2 et 5")
            taille_bateau = input(f"Quelle taille pour le bateau numéro {loop+1} (entre 2 et 5) :  ")
        bateaux.append(int(taille_bateau))
    return (bateaux, bateaux)
    
def verif_placmnt_bateaux(c1, c2, n, grille_pos):
    """Fonction qui vérifie si les 2 coordonnées sont bien sur la même ligne ou même colonne, on ne peut
    pas placer de bateaux en diagonale.
    On ne peut pas non plus placer un bateau sur un bateau deja placé.
    c1 et c2 sont des coordonnées sous la forme [i,j] ou i est l'indice de la ligne et j l'indice de la colonne pour notre liste 2D. 
    n est la taille du bateau considéré.
    grille_pos est la grille des positions pour vérifier la validité des coordonnées.
    """
    if c2[0] > 10 or c2[1] > 10 :
        print("Vous essayez de placer un bateau trop près du bord.")
        res = False # Il n'y a pas la place pour faire rentrer un bateau 
    else:
        print(c1, c2)
        if c1[0] == c2[0] :#On est horizontal
            i = c1[1]
            while i < c2[1] and not grille_pos[c1[0]][i] :
                i += 1
            if i != c2[1] :
                print("Vous essayez de placer un bateau trop proche d'un autre bateau.")
                res = False
            else:
                res = True
        else: #Normalement on est forcément vertical
            i = c1[0]
            while i < c2[0] and not grille_pos[i][c1[1]] :
                i += 1 
            if i != c2[0] :
                print("Vous essayez de placer un bateau trop proche d'un autre bateau.")
                res = False
            else:
                res = True
        return res
            
        
def placement_bateaux(n,num_bat,grille_pos):
        """
        Permet au joueur de placer ses bateaux de taille n dans
        l'arène verticalement ou horizontalement (en modifiant les valeurs 
        de la liste contenant l'arène)
        num_bat est une variable qui continent le numéro du bateau que l'on doit placer.
        """
        a = input("coordonnée ligne entre 1 et 10 :  ") 
        if a != '10' : #10 est le seul cas où on ne peut pas utiliser la fonction ord car '10' fait 2 caractères donc on traite ce cas à part
            while len(a) != (1 or 2) or ord(a)<47 or ord(a)> 58 :
                print("Rentrez un chiffre entre 1 et 10 !")
                a = input("coordonnée ligne entre 1 et 10 :  ")
        a = int(a)
        b = (input("coordonnées colonne entre A et J :  "))
        while len(b) != 1 or ord(b)<65 or ord(b)> 74 :
            print("Rentrez une lettre majuscule entre A et J")
            b = (input("coordonnées colonne entre A et J :  "))
        b = ord(b) - 64
        c1 = [a,b] #Coordonnée du bateau en indices uniquement à titre indicatif
        vertical = input("vertical ou horizontal (tapez h ou v) :  ")
        while vertical not in "hv" or len(vertical) != 1 :
            vertical = input("vertical ou horizontal (tapez h ou v) :  ")
        if vertical == "v":
            vertical = True
        else:
            vertical = False

        if vertical:
            c2  = [a+n, b] #Coordonées du bateau en chiffres uniquement à titre indicatif
            if verif_placmnt_bateaux([a, b], [a+n, b], n, grille_pos):
                for i in range(a,a+n):
                    grille_pos[i][b] = num_bat
            else:
                placement_bateaux(n, num_bat, grille_pos)
        else:
            c2 = [a, b+n]#Coordonées du bateau en indice uniquement à titre indicatif
            if verif_placmnt_bateaux([a,b], [a, b+n] , n, grille_pos):
                for i in range(b,b+n):
                    grille_pos[a][i] = num_bat
            else:
                placement_bateaux(n, num_bat, grille_pos)

def grille_pos(n,e):
    """
    génère une grille de n lignes et n colonnes
    e est l'élément contenu dans chaque cellule
    """
    grille = [list()]*n
    for k in range(len(grille)):
        grille[k] = [e]*n
    return grille

def grille_jeu():
    """
    Génère la grille de jeu:
    Une grille 11 par 11 ou la première ligne et colonne forment le repère des coordonnées.
    Retourne la grille sous forme de liste.
    """
    l1 = []
    l2 = ["   ", "A","B", "C", "D", "E", "F", "G", "H", "I", "J"]
    l1.append(l2)
    for y in range(1,11):
        l1.append([f"{y}  ",".",".",".",".",".",".",".",".",".","."])
    return(l1)

#grille_jeu = grille_jeu()

def afficher_grille(grille):
    """
    On veut afficher notre grille de la forme:
     ABCDEFGHIJ
    1..........
    2..X.......
    3.......O..
    4.......O..
    5...X......
    6..........
    7.....OOO..
    8..........
    9.....X....
   10..........
  
   Le paramètre grille est une liste 2D. On part du principe que la liste est déjà sous la bonne forme.
    """
    for ligne in grille:
        print("\n")
        for case in ligne:
            print(f"{case:4}", end="")
    print("\n")

def trad_coordonnees(coordonnees):
    """
    Convertit des coordonnées sous forme de chaîne de caractère donnés en paramètre en liste
    de la forme [chiffre_ligne, chiffre_colonne]
    """
    nouvelles_coordonnees = []
    nouvelles_coordonnees.append(int(coordonnees[1:])) #Position sur les lignes
    nouvelles_coordonnees.append(ord(coordonnees[0]) - 64) #Position sur les colonnes
    return nouvelles_coordonnees

def verif_coord(coord, grille_j):
    """
    Le paramètre coord correspond à la saisie de l'utilisateur qui doit être sous la forme A5 par exemple c'est à dire
    'colonne ligne'. Avec la lettre de la colonne en majuscules
    grille_j est la liste qui stocke tout les tirs déja effectués.
    Cette fonction retourne un booléen correspondant à la validité des coordonnées.
    """
    ex = "Un exemple de coordonnée valide serait :F2"
    if len(coord) <= 3:
        try:
            ligne = int(coord[1:])
            res = True
        except ValueError:
            print("La coordonnée correspondant à la ligne doit être un chiffre\n", ex)
            res = False
        if res:
            if ligne <= 10 and ligne > 0:
                if ord(coord[0]) >= 65 and ord(coord[0])<= 74:
                    coord = trad_coordonnees(coord)
                    print(coord)
                    if grille_j[coord[0]][coord[1]] == '.':
                        res = True
                    else:
                        print("Vous avez déjà tiré dans cette case. Sah vise mieux !")
                        res = False
                else:
                    print("La coordonnée correspondant à la colonne doit être en majuscule entre A et J (inclus).\n", ex)
                    res = False
            else:
                print("Vous avez rentré un numéro de ligne qui ne rentre pas dans le tableau.\n", ex)
                res = False
    else:
        print("Vous avez rentré des coordonnées trop longues !\n", ex)
        res = False
    return res

def touche_ou_coule(grille_pos, tir_y, tir_x):
    """
    Modifie la liste des positions en mettant 0 à la coordonée qui a été atteinte.
    Ensuite on parcourt toute la liste des positions pour voir s'il reste encore des cellules avec des chiffres du bateaux.
    Si le numéro n'est plus représenté, afficher "touché, coulé".
    """
    coule = True
    bateau = grille_pos[tir_y][tir_x] 
    grille_pos[tir_y][tir_x] = 0 #On modifie la grille en retirant la case du bateau qui a été touchée
    for k in range (len(grille_pos)):
        for i in range (len(grille_pos)):
            if grille_pos[k][i] == bateau:
                coule = False
    if not coule:
        print("Touché !")
    else:
        print("Touché ! Coulé !")

def bateau_touche(coord, grille_pos, grille_jeu,joueur):
    """
    Cherche si les coordonnées renseignées en paramètre correspondent à la position d'un bâteau dans la grille de jeu de l'adversaire
    Si un bateau est touché, indiqué la touche sur la grille de jeu, réduire de 1 la vie du bâteau et la somme
    Retourne True si on a touché un bateau, False sinon.
    """
    if grille_pos[coord[0]][coord[1]]:  #Bateau touché
        grille_jeu[coord[0]][coord[1]] = "X"
        afficher_grille(grille_jeu)
        touche_ou_coule(grille_pos, coord[0], coord[1])
        res = True
    else:   #Tir dans l'eau
         grille_jeu[coord[0]][coord[1]] = "O"
         afficher_grille(grille_jeu)
         print("Plouf, c'est raté")
         print("C'est au tour de l'adversaire")
         res = False
    return res
         
def affichage_bateaux(grille_pos):
    grille_aff = grille_jeu()
    for i in range(len(grille_pos)):
        for j in range(len(grille_pos[i])):
            if grille_pos[i][j] :
                grille_aff[i][j] = 'B'
    afficher_grille(grille_aff)
         
#afficher_grille(grille_jeu)

#Définition des variables :
bateaux_1, bateaux_2 = init_bateau()
bateaux = [bateaux_1, bateaux_2]
tour = 0 #variable que l'on incremente à chaque fois qu'on change de joueur actif
grille_jeu_1 = grille_jeu()
grille_jeu_2 = grille_jeu()
grilles_jeux = [grille_jeu_1, grille_jeu_2]
grille_position_1 = grille_pos(11,0)    #Initialisation des grilles de position
grille_position_2 = grille_pos(11,0) 
grilles_pos = [grille_position_1, grille_position_2]

#Boucle Principale :

nombre_joueurs = 2 #nombre_joueurs()

  

if nombre_joueurs == 2:#Placement des bateaux ( optimisé)
    for i in range(2):
        print(f"Le joueur {i+1} va placer ses bateaux. Joueur {2-i} ne regardez pas !")
        for j in range(len(bateaux[i])):
            placement_bateaux(bateaux[i][j], j+1, grilles_pos[i])
        affichage_bateaux(grilles_pos[i])
    while test_victoire(grilles_pos[0]) and test_victoire(grilles_pos[1]): #On regarde dans les 2 grilles s'il reste encore des bateux à chasser.
        if tour %2 == 0:
            print("C'est au tour de joueur 1\n")
        else:
            print("C'est au tour de joueur 2\n")
        afficher_grille(grilles_jeux[tour%2])
        coordonnees_tir = input("Rentrez vos coordonnées de tir:  ")
        while not verif_coord(coordonnees_tir,grilles_jeux[tour%2]):
            coordonnees_tir = input("Rentrez vos coordonnées de tir:  ")
        print("C'est bon les coordonnées sont valide on va pouvoir tirer.")
        trad_coord = trad_coordonnees(coordonnees_tir)
        while bateau_touche(trad_coord,grilles_pos[(tour+1)%2],grilles_jeux[tour%2],f"joueur {tour%2 +1}") and test_victoire(grilles_pos[(tour+1)%2]) :
            print(f"Joueur {tour%2 +1} vous pouvez rejouer !")
            afficher_grille(grilles_jeux[tour%2])
            coordonnees_tir = input("Rentrez vos coordonnées de tir:  ")
            while not verif_coord(coordonnees_tir,grilles_jeux[tour%2]):
                coordonnees_tir = input("Rentrez vos coordonnées de tir:  ")
            print("C'est bon les coordonnées sont valide on va pouvoir tirer.")
            trad_coord = trad_coordonnees(coordonnees_tir)
        tour += 1
    print("FIN DE PARTIE")
