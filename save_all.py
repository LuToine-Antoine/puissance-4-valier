from tkinter import *


class Pion:
    def __init__(self, x, y, joueur):
        self._x = x
        self._y = y
        self._joueur = joueur

    def set_coordonee(self, x, y):
        self._x = x
        self._y = y

    def get_coordonnee(self):
        return self._x, self._y

    def get_joueur(self):
        """
        Retourne le joueur actuel.
        """
        return self._joueur


class Jeu:
    def __init__(self):
        self._nb_pions = None
        self._board = []
        self._board_size = None
        self.set_board_size()
        self.set_board()
        self._tour = 0
        self._x = 0
        self._y = 0
        self._joueur = 1
        self._possible = []
        # Pour combinaison
        self._pion = Pion(None, None, 1)
        self._pion2 = Pion(None, None, 2)

    def get_board_size(self):
        """
        Permet d'avoir la taille du plateau.
        """
        return self._board_size

    def set_board_size(self):
        """
        Permet de selectionner la taille du plateau entre 8 et 12.
        """
        self._board_size = int(input("Choisissez une taille de plateau comprise entre 8 et 12 : "))
        while (8 > self._board_size) or (self._board_size > 12):
            self._board_size = int(
                input("Taille non prise en charge, veuillez re-saisir une taille de plateau comprise entre 8 et 12 : "))

    def set_board(self):
        """
        Permet d'initialiser le plateau en fonction de la taille entrée.
        """
        self._board = []
        for i in range(self.get_board_size()):
            ligne = []
            self._board.append(ligne)
            for j in range(self.get_board_size()):
                ligne.append(0)
        return self._board

    def get_board(self):
        """
        Permet de retourner le tableau.
        """
        return self._board

    def get_nombre_de_pions_a_aligner(self):
        """
        Permet de retourner le nombre de pions nécessaire à aligner pour gagner.
        """
        return self._nb_pions

    def set_nombre_de_pions_a_aligner(self):
        """
        Permet de définir le nombre de pions à aligner pour gagner.
        """
        self._nb_pions = int(input("Nombre de pion à aligner entre 4 et 6 : "))
        while (4 > self._nb_pions) or (self._nb_pions > 6):
            self._nb_pions = int(
                input("Valeur non prise en charge, veuillez re-saisir un nombre de pion à aligner entre 4 et 6 :  "))

    def placement_pion(self, plateau, x, y, ancien):
        """
        Permet de placer un pion selon le joueur et si le déplaceent est possible au vu des règles du jeu sur la case sélectionnée.
        """
        #print("Peut se placer : ", self._pion.deplacement_possible(plateau, self._x, self._y, self._tour))
        if self._case_possibles(plateau,x,y) is True:
            plateau[self._y][self._x] = 1

        elif self._case_possibles(plateau,x,y) is True:
            plateau[self._y][self._x] = 2

    def placement_croix(self, plateau):
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                if plateau[i][j] == 1:
                    plateau[i][j] = 3
                elif plateau[i][j] == 2:
                    plateau[i][j] = 4

    def verif_haut(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i][j - 1] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_bas(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i][j + 1] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_gauche(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j] == pion_du_joueur:
                    alignement += 1
                else:
                    break
                if alignement >= self.get_nombre_de_pions_a_aligner():
                    return True

    def verif_droite(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diaghautdroit(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j - 1] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diaghautgauche(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j - 1] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diagbasdroit(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j + 1] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diagbasgauche(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j + 1] == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_alignement(self):
        """
        Verifie si le nombre de pions a aligner le sont.
        """
        pion_du_joueur = 0
        if self._tour % 2 == 0:
            pion_du_joueur = 3
        else:
            pion_du_joueur = 4
        for i in range(self._board_size):
            for j in range(self._board_size):

                # Coin Haut Gauche
                if i == 0:
                    if j == 0:
                        # Droite
                        self.verif_droite(i, j, pion_du_joueur)
                        # Bas
                        self.verif_bas(i, j, pion_du_joueur)
                        # Diagonale Bas Droite
                        self.verif_diagbasdroit(i, j, pion_du_joueur)

                # Coin Haut Doite
                if i == self._board_size:
                    if j == 0:
                        # Gauche
                        self.verif_diaghautdroit(i, j, pion_du_joueur)
                        # Bas
                        self.verif_bas(i, j, pion_du_joueur)
                        # Diagonale Bas Gauche
                        self.verif_diagbasgauche(i, j, pion_du_joueur)

                # Coin Bas Gauche
                if i == 0:
                    if j == self._board_size:
                        # Droite
                        self.verif_droite(i, j, pion_du_joueur)
                        # Haut
                        self.verif_haut(i, j, pion_du_joueur)
                        # Diagonale Haut Droite
                        self.verif_diaghautdroit(i, j, pion_du_joueur)

                # Coin Bas Doite
                if i == self._board_size:
                    if j == self._board_size:
                        # Gauche
                        self.verif_gauche(i, j, pion_du_joueur)
                        # Haut
                        self.verif_haut(i, j, pion_du_joueur)
                        # Diagonale Haut Gauche
                        self.verif_diaghautgauche(i, j, pion_du_joueur)

                # Ligne Haut
                if j == 0:
                    # Gauche
                    self.verif_gauche(i, j, pion_du_joueur)
                    # Bas
                    self.verif_bas(i, j, pion_du_joueur)
                    # Droite
                    self.verif_droite(i, j, pion_du_joueur)
                    # Diagonale Bas Droite
                    self.verif_diagbasdroit(i, j, pion_du_joueur)
                    # Diagonale Bas Gauche
                    self.verif_diagbasgauche(i, j, pion_du_joueur)

                # Ligne Gauche
                if i == 0:
                    # Bas
                    self.verif_bas(i, j, pion_du_joueur)
                    # Haut
                    self.verif_haut(i, j, pion_du_joueur)
                    # Droite
                    self.verif_droite(i, j, pion_du_joueur)
                    # Diagonale Bas Droite
                    self.verif_diagbasdroit(i, j, pion_du_joueur)
                    # Diagonale Haut Droite
                    self.verif_diaghautdroit(i, j, pion_du_joueur)

                # Ligne Bas
                if j == self._board_size:
                    # Haut
                    self.verif_haut(i, j, pion_du_joueur)
                    # Droite
                    self.verif_droite(i, j, pion_du_joueur)
                    # Gauche
                    self.verif_gauche(i, j, pion_du_joueur)
                    # Diagonale Haut Droite
                    self.verif_diaghautdroit(i, j, pion_du_joueur)
                    # Diagonale Haut Gauche
                    self.verif_diaghautgauche(i, j, pion_du_joueur)

                # Ligne Droite
                if i == self._board_size:
                    # Haut
                    self.verif_haut(i, j, pion_du_joueur)
                    # Gauche
                    self.verif_gauche(i, j, pion_du_joueur)
                    # Bas
                    self.verif_bas(i, j, pion_du_joueur)
                    # Diagonale Bas Gauche
                    self.verif_diagbasgauche(i, j, pion_du_joueur)
                    # Diagonale Haut Gauche
                    self.verif_diaghautgauche(i, j, pion_du_joueur)

                # Global
                # Gauche
                else:
                    self.verif_gauche(i, j, pion_du_joueur)
                    self.verif_droite(i, j, pion_du_joueur)
                    self.verif_haut(i, j, pion_du_joueur)
                    self.verif_bas(i, j, pion_du_joueur)
                    self.verif_diagbasdroit(i, j, pion_du_joueur)
                    self.verif_diagbasgauche(i, j, pion_du_joueur)
                    self.verif_diaghautdroit(i, j, pion_du_joueur)
                    self.verif_diagbasgauche(i, j, pion_du_joueur)

    def end_of_game(self, x, y, tour):
        """
        Permet de vérifier les conditions d'arrêt
        """
        # Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases disponibles) alors, la partie se termine.
        if not self.cases_possibles(self._board, x, y):
            return True
        elif not self.cases_possibles(self._board, x, y):
            return True
        elif self.verif_alignement() is True and tour > 1:
            return True
        else:
            return False

    def cases_possibles(self, plateau, x, y):
        """
        Fonction qui regarde si la case sélectionnée par le joueur est une des cases sur lesquelles le pion peut se déplacer
        """
        self._x = x
        self._y = y
        self._possible = []

        # Vérifie si la case est sur le plateau pour éviter le out of range.
        # x Haut gauche
        if (self._x - 2) >= 0 and (self._y - 1) >= 0:
            # Vérifie si la case est vide
            if plateau[self._x - 2][self._y - 1] == 0:
                return True
            else:
                return False

        # x Bas gauche
        if (self._x - 2) >= 0 and (self._y + 1) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x - 2][self._y + 1] == 0:
                return True
            else:
                return False

        # x Haut droite
        if (self._x + 2) < len(plateau) and (self._y - 1) >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x + 2][self._y - 1] == 0:
                return True
            else:
                return False

        # x Bas droite
        if (self._x + 2) < len(plateau) and (self._y + 1) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x + 2][self._y + 1] == 0:
                return True
            else:
                return False

        # y Haut gauche
        if (self._x - 1) >= 0 and (self._y - 2) >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x - 1][self._y - 2] == 0:
                return True
            else:
                return False

        # y Bas gauche
        if (self._x - 1) >= 0 and (self._y + 2) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x - 1][self._y + 2] == 0:
                return True
            else:
                return False

        # y Haut droite
        if (self._x + 1) < len(plateau) and (self._y - 2) >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x + 1][self._y - 2] == 0:
                return True
            else:
                return False

        # y Bas droite

        if (self._x + 1) < len(plateau) and (self._y + 2) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x + 1][self._y + 2] == 0:
                return True
            else:
                return False

        print("ici", self._possible)


class Gui(Jeu, Pion):
    def __init__(self, width=600, height=600):
        self._root = Tk()
        self._root.title("La puissance du cavalier")
        Jeu.__init__(self)
        Pion.__init__(self, None, None, 1)
        self._pion1 = Pion(None, None, 1)
        self._pion2 = Pion(None, None, 2)
        self._taille_case = 500 // self.get_board_size() - 1
        self._plateau = self.get_board()
        self.set_nombre_de_pions_a_aligner()
        self.get_nombre_de_pions_a_aligner()

        # Définit la taille de la fenêtre
        self._canvas = Canvas(self._root, width=width, height=height)

        # Lance le GUI
        self._canvas.pack()

        # Affiche le plateau
        plateau_size = self.get_board_size()
        for i in range(plateau_size):
            for j in range(plateau_size):
                self._canvas.create_rectangle((i + 1) * self._taille_case + 2, (j + 1) * self._taille_case + 2,
                                              (i + 1) * self._taille_case + self._taille_case + 2,
                                              (j + 1) * self._taille_case + self._taille_case + 2)

        # Récupère les cliques de l'utilisateur
        self._canvas.bind("<Button-1>", self.boucle_jeu)
        # Lance le GUI
        self._root.mainloop()

    def put_pions(self, x, y, ancien):
        """
        Fonction qui place les pions aux coordonnées du click sur le plateau.
        """

        self._x = x
        self._y = y
        ancien_ = ancien
        if self._tour % 2 == 0:
            self._joueur = 1
        else:
            self._joueur = 2

        if 0 <= self._x < self.get_board_size() and 0 <= self._y < self.get_board_size():
            if 0 <= self._tour <= 2:

                if self._joueur == 1:
                    print(self._x, self._y)
                    self.placement_pion(self._plateau, self._x, self._y, ancien_)
                    self.affichage_rond(self._x, self._y, self._tour)
                    self._pion.get_coordonnee()
                    print(self._tour)
                    self._tour += 1

                if self._joueur == 2:
                    self.placement_pion(self._plateau, self._x, self._y, ancien_)
                    self.affichage_rond(self._x, self._y, self._tour)
                    self._pion2.get_coordonnee()
                    print(self._tour)
                    self._tour += 1

            if self._tour > 1:
                if self._joueur == 1:
                    if self.cases_possibles(self._plateau, self._x, self._y) is True:
                        self.placement_pion(self._plateau, self._x, self._y, ancien_)
                        self.affichage_rond(self._x, self._y, self._tour)
                        print(self._tour)
                        self._tour += 1

                elif self._joueur == 2:
                    if self.cases_possibles(self._plateau, self._x, self._y) is True:
                        self.placement_pion(self._plateau, self._x, self._y, ancien_)
                        self.affichage_rond(self._x, self._y, self._tour)
                        print(self._tour)
                        self._tour += 1


            print(*self._plateau, sep="\n")
            #print("hello 1 : ", self._pion.deplacement_possible(self._plateau, self._ancien_x, self._ancien_y, self._tour), "hello 2 : ", self._pion.deplacement_possible(self._plateau,self._ancien_x2, self._ancien_y2, self._tour), sep="\n")
            return self._x, self._y, self._tour, self._plateau

    def affichage_rond(self, x, y, tour):
        """
        Affiche les pions.
        """
        self._x = x
        self._y = y
        self._tour = tour

        if self._tour % 2 == 0 and self._plateau[self._x][self._y] == 0:
            for item in self._canvas.find_withtag("pion1"):
                self._canvas.delete(item)
            self._canvas.create_oval((self._x + 1) * self._taille_case + 2 + 3,
                                     (self._y + 1) * self._taille_case + 2 + 3,
                                     (self._x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (self._y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="blue", tags='pion1')
            self._tour += 1
            self._plateau[self._x][self._y] = 1
            return self._plateau[self._x][self._y], self._tour

        elif self._tour % 2 != 0 and self._plateau[self._x][self._y] == 0:
            for item in self._canvas.find_withtag("pion2"):
                self._canvas.delete(item)
            self._canvas.create_oval((self._x + 1) * self._taille_case + 2 + 3,
                                     (self._y + 1) * self._taille_case + 2 + 3,
                                     (self._x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (self._y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="red", tags='pion2')
            self._tour += 1
            self._plateau[self._x][self._y] = 2
            return self._plateau[self._x][self._y], self._tour

    def set_croix(self, x, y):
        self._x = x
        self._y = y
        size = self.get_board_size()
        if self._plateau[self._x][self._y] == 1:
            self._plateau[self._x][self._y] = 3
            self.affichage_croix()
        elif self._plateau[self._x][self._y] == 2:
            self._plateau[self._x][self._y] = 4
            self.affichage_croix()
        return self._plateau[self._x][self._y]

    def affichage_croix(self):
        if self._plateau[self._y][self._x] == 3:
            self._canvas.create_line((self._y + 1) * self._taille_case,
                                     (self._x + 1) * self._taille_case,
                                     (self._y + 1) * self._taille_case + self._taille_case,
                                     (self._x + 1) * self._taille_case + self._taille_case, fill="blue",
                                     width=5)
            self._canvas.create_line((self._y + 2) * self._taille_case - self._taille_case,
                                     (self._x + 1) * self._taille_case + self._taille_case,
                                     (self._y + 2) * self._taille_case,
                                     (self._x + 1) * self._taille_case, fill="blue", width=5)

            return self._plateau[self._y][self._x]
        if self._plateau[self._y][self._x] == 4:
            self._canvas.create_line((self._y + 1) * self._taille_case,
                                     (self._x + 1) * self._taille_case,
                                     (self._y + 1) * self._taille_case + self._taille_case,
                                     (self._x + 1) * self._taille_case + self._taille_case, fill="red",
                                     width=5)
            self._canvas.create_line((self._y + 2) * self._taille_case - self._taille_case,
                                     (self._x + 1) * self._taille_case + self._taille_case,
                                     (self._y + 2) * self._taille_case,
                                     (self._x + 1) * self._taille_case, fill="red", width=5)

            self._plateau[self._y][self._x] = 4
            return self._plateau[self._y][self._x]

    def boucle_jeu(self, event):
        """
        Fonction qui permet au jeu de fonctionner selon les règles, le déroulement du jeu.
        """
        self._x=0
        self._y =0
        case = (((event.x - 50) // self._taille_case),((event.y - 50) // self._taille_case))
        if self.end_of_game(self._x, self._y, self._tour) is False:
            if self._tour < 2:
                if self._joueur == 1:
                    self._pion.set_coordonee(self._x, self._y)
                    pion_1 = self._pion1.get_coordonnee()
                    ancien1 = pion_1
                    self.put_pions(self._x, self._y, ancien1)
                    self.affichage_rond()
                    self.affichage_croix()
                elif self._joueur == 2:
                    self._pion2.set_coordonee(self._x, self._y)
                    pion_2 = self._pion2.get_coordonnee()
                    ancien2 = pion_2
                    self.put_pions(self._x, self._y, ancien2)
                    self.affichage_rond()
                    self.affichage_croix()
            print("joueur", self._joueur)
            if self._tour % 2 == 0:
                self._joueur = 1
                pion_1 = self._pion1.get_coordonnee()
                ancien1 = pion_1
                self.placement_croix(self._plateau)
                print("tour", self._tour)
                self.affichage_rond()
                self.affichage_croix()
            elif self._tour % 2 == 1:
                self._joueur = 2
                self._pion2.set_coordonee(pion_2)
                pion_2 = self._pion2.get_coordonnee()
                ancien2 = pion_2
                self.put_pions(self._x, self._y, ancien2)
                self.placement_croix(self._plateau)
                print(self._tour)
                self.affichage_rond()
                self.affichage_croix()
        else:
            return f"Joueur {self._joueur} a gagné !"


Gui(600, 600)
