from tkinter import *


class Pion:
    def __init__(self, x, y, joueur):
        self._x = x
        self._y = y
        self._joueur = joueur

    def set_coordoneex(self, x):
        self._x = x

    def get_coordonneex(self):
        return self._x

    def set_coordoneey(self, y):
        self._y = y

    def get_coordonneey(self):
        return self._y

    def get_joueur(self):
        """
        Retourne le joueur actuel.
        """
        return self._joueur


class Jeu:
    def __init__(self):
        self._nb_pions = 4
        self._board = []
        self._board_size = 8
        self.set_board_size()
        self.set_board()
        self._tour = 0
        self._x = 0
        self._y = 0
        self._possible = []
        self._joueur = 1
        # Pour combinaison
        self._pion1 = Pion(0, 0, 1)
        self._pion2 = Pion(0, 0, 2)

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

    def cases_possibles(self, plateau, x, y):
        """
        Fonction qui regarde si la case sélectionnée par le joueur est une des cases sur lesquelles le pion peut se déplacer
        """
        print("cases possibles ", x, y)

        possible = []
        # Vérifie si la case est sur le plateau pour éviter le out of range.
        # x Haut gauche
        if (x - 2) >= 0 and (y - 1) >= 0:
            # Vérifie si la case est vide
            if plateau[x - 2][y - 1] == 0:
                possible.append((x - 2, y - 1))

        # x Bas gauche
        if (x - 2) >= 0 and (y + 1) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[x - 2][y + 1] == 0:
                possible.append((x - 2, y + 1))

        # x Haut droite
        if (x + 2) < len(plateau) and (y - 1) >= 0:
            # Vérifie si la case est disponible
            if plateau[x + 2][y - 1] == 0:
                possible.append((x + 2, y - 1))

        # x Bas droite
        if (x + 2) < len(plateau) and (y + 1) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[x + 2][y + 1] == 0:
                possible.append((x + 2, y + 1))

        # y Haut gauche
        if (x + 1) < len(plateau) and (y + 2) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[x + 1][y + 2] == 0:
                possible.append((x + 1, y + 2))

        # y Bas gauche
        if (x + 1) < len(plateau) and (y - 2) >= 0:
            # Vérifie si la case est disponible
            if plateau[x + 1][y - 2] == 0:
                possible.append((x + 1, y - 2))

        # y Haut droite
        if (x - 1) >= 0 and (y + 2) < len(plateau):
            # Vérifie si la case est disponible
            if plateau[x - 1][y + 2] == 0:
                possible.append((x - 1, y + 2))

        # y Bas droite

        if (x - 1) >= 0 and (y - 2) >= 0:
            # Vérifie si la case est disponible
            if plateau[x - 1][y - 2] == 0:
                possible.append((x - 1, y - 2))

        return possible

    def placement_pion(self, plateau, x, y, joueur):
        """
        Permet de placer un pion selon le joueur et si le déplaceent est possible au vu des règles du jeu sur la case sélectionnée.
        """
        if self._tour <= 1:
            if joueur == 1:
                plateau[x][y] = 1
            elif joueur == 2:
                plateau[x][y] = 2
            return True
        else:
            self._possible = self.cases_possibles(plateau, x, y)
            if self._possible == []:
                print("Joueur ", self._joueur, " Win !!!")

            print(x, y)
            print(self._possible)

            if (self._x, self._y) in self._possible:
                print(self._possible)
                print(x, y)
                if joueur == 1:
                    plateau[x][y] = 1
                elif joueur == 2:
                    plateau[x][y] = 2
                return True
            return False

    def placement_croix(self, x, y, plateau):
        if plateau[x][y] == 1:
            plateau[x][y] = 3
        elif plateau[x][y] == 2:
            plateau[x][y] = 4

    def verif_haut(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i][j - 1] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_bas(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i][j + 1] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_gauche(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i - 1][j] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
                if alignement >= self.get_nombre_de_pions_a_aligner():
                    return True

    def verif_droite(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i + 1][j] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diaghautdroit(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i + 1][j - 1] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diaghautgauche(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i - 1][j - 1] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diagbasdroit(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i + 1][j + 1] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_diagbasgauche(self, i, j, pion_du_joueur):
        alignement = 1
        if self._board[i][j] == pion_du_joueur:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if 0 <= self._board[i - 1][j + 1] < self.get_board_size() == pion_du_joueur:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                return True

    def verif_alignement(self, x, y):
        """
        Verifie si le nombre de pions a aligner le sont.
        """
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
                elif i == self._board_size:
                    if j == 0:
                        # Gauche
                        self.verif_diaghautdroit(i, j, pion_du_joueur)
                        # Bas
                        self.verif_bas(i, j, pion_du_joueur)
                        # Diagonale Bas Gauche
                        self.verif_diagbasgauche(i, j, pion_du_joueur)

                # Coin Bas Gauche
                elif i == 0:
                    if j == self._board_size:
                        # Droite
                        self.verif_droite(i, j, pion_du_joueur)
                        # Haut
                        self.verif_haut(i, j, pion_du_joueur)
                        # Diagonale Haut Droite
                        self.verif_diaghautdroit(i, j, pion_du_joueur)

                # Coin Bas Doite
                elif i == self._board_size:
                    if j == self._board_size:
                        # Gauche
                        self.verif_gauche(i, j, pion_du_joueur)
                        # Haut
                        self.verif_haut(i, j, pion_du_joueur)
                        # Diagonale Haut Gauche
                        self.verif_diaghautgauche(i, j, pion_du_joueur)

                # Ligne Haut
                elif j == 0:
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
                elif i == 0:
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
                elif j == self._board_size:
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
                elif i == self._board_size:
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

    def end_of_game(self, tour):
        """
        Permet de vérifier les conditions d'arrêt
        """
        pion1x, pion1y = self._pion1.get_coordonneex(), self._pion1.get_coordonneey()
        pion2x, pion2y = self._pion2.get_coordonneex(), self._pion2.get_coordonneey()
        print("pion 1", pion1x, pion1y)
        print("pion 2", pion2x, pion2y)

        # Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases disponibles) alors, la partie se termine.
        if self.placement_pion(self._plateau, pion1x, pion1y, self._joueur) is False or self.placement_pion(
                self._plateau, pion2x, pion2y, self._joueur) is False:
            return True
        elif self.verif_alignement(pion1x, pion1y) is True or self.verif_alignement(pion2x,
                                                                                    pion2y) is True and tour > 1:
            return True
        else:
            return False


class Gui(Jeu, Pion):
    def __init__(self, width=600, height=600):
        self._root = Tk()
        self._root.title("Puissance 4-valier")
        Jeu.__init__(self)
        Pion.__init__(self, 0, 0, 1)
        self._pion1 = Pion(0, 0, 1)
        self._pion2 = Pion(0, 0, 2)
        self._pion1x = 0
        self._pion1y = 0
        self._pion2x = 0
        self._pion2y = 0
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

    def affichage_rond(self, x, y):
        """
        Affiche les pions.
        """
        if self._joueur == 1:
            for item in self._canvas.find_withtag("pion1"):
                self._canvas.delete(item)
            self._canvas.create_oval((x + 1) * self._taille_case + 2 + 3,
                                     (y + 1) * self._taille_case + 2 + 3,
                                     (x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="blue", tags='pion1')
            self._plateau[x][y] = 1

        elif self._joueur == 2:
            for item in self._canvas.find_withtag("pion2"):
                self._canvas.delete(item)
            self._canvas.create_oval((x + 1) * self._taille_case + 2 + 3,
                                     (y + 1) * self._taille_case + 2 + 3,
                                     (x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="red", tags='pion2')
            self._plateau[x][y] = 2

    def affichage_croix(self, x, y):
        if self._plateau[x][y] == 3:
            self._canvas.create_line((x + 1) * self._taille_case,
                                     (y + 1) * self._taille_case,
                                     (x + 1) * self._taille_case + self._taille_case,
                                     (y + 1) * self._taille_case + self._taille_case, fill="blue",
                                     width=5)
            self._canvas.create_line((x + 2) * self._taille_case - self._taille_case,
                                     (y + 1) * self._taille_case + self._taille_case,
                                     (x + 2) * self._taille_case,
                                     (y + 1) * self._taille_case, fill="blue", width=5)

        elif self._plateau[x][y] == 4:
            self._canvas.create_line((x + 1) * self._taille_case,
                                     (y + 1) * self._taille_case,
                                     (x + 1) * self._taille_case + self._taille_case,
                                     (y + 1) * self._taille_case + self._taille_case, fill="red",
                                     width=5)
            self._canvas.create_line((x + 2) * self._taille_case - self._taille_case,
                                     (y + 1) * self._taille_case + self._taille_case,
                                     (x + 2) * self._taille_case,
                                     (y + 1) * self._taille_case, fill="red", width=5)

    def boucle_jeu(self, event):
        """
        Fonction qui permet au jeu de fonctionner selon les règles, le déroulement du jeu.
        """

        case = (((event.x - 50) // self._taille_case), ((event.y - 50) // self._taille_case))

        if self._tour % 2 == 0:
            self._joueur = 1
            anciennes_cos_x = self._pion1.get_coordonneex()
            anciennes_cos_y = self._pion1.get_coordonneey()
        else:
            self._joueur = 2
            anciennes_cos_x = self._pion2.get_coordonneex()
            anciennes_cos_y = self._pion2.get_coordonneey()

        self._x = case[0]
        self._y = case[1]

        print("joueur : ", self._joueur)
        if 0 <= self._x < self.get_board_size() and 0 <= self._y < self.get_board_size():
            print("new coord :", self._x, self._y)
            print("anciennes_cos_x :", anciennes_cos_x, anciennes_cos_y)
            if self._tour > 1:
                if self.placement_pion(self._plateau, anciennes_cos_x, anciennes_cos_y, self._joueur) is True:
                    self.affichage_rond(self._x, self._y)
                    self.placement_croix(anciennes_cos_x, anciennes_cos_y, self._plateau)
                    self.affichage_croix(anciennes_cos_x, anciennes_cos_y)

                    if self._joueur == 1:
                        self._pion1.set_coordoneex(self._x)
                        self._pion1.set_coordoneey(self._y)
                    elif self._joueur == 2:
                        self._pion2.set_coordoneex(self._x)
                        self._pion2.set_coordoneey(self._y)

                    print(*self._plateau, sep="\n")
                    self._tour += 1

            else:
                self.placement_pion(self._plateau, self._x, self._y, self._joueur)
                self.affichage_rond(self._x, self._y)

                if self._joueur == 1:
                    self._pion1.set_coordoneex(self._x)
                    self._pion1.set_coordoneey(self._y)
                elif self._joueur == 2:
                    self._pion2.set_coordoneex(self._x)
                    self._pion2.set_coordoneey(self._y)

                print(*self._plateau, sep="\n")
                self._tour += 1

        if self.end_of_game(self._tour) is True:
            return f"Joueur {self._joueur} a gagné !"


Gui(600, 600)
