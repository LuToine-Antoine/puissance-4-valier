from tkinter import *


class Pion:
    def __init__(self, x, y, joueur=1):
        self._x = x
        self._y = y
        self._joueur = joueur
        self._possible = []

    def get_joueur(self):
        """
        Retourne le joueur actuel.
        """
        return self._joueur

    def cases_possibles(self, plateau):
        """
        Fonction qui regarde si la case sélectionnée par le joueur est une des cases sur lesquelles le pion peut se déplacer
        """
        # Vérifie si la case est sur le plateau pour éviter le out of range.
        # i Haut gauche
        if self._x - 2 >= 0 and self._y - 1 >= 0:
            # Vérifie si la case est vide
            if plateau[self._x - 2][self._y - 1] == 0:
                # Mise des coordonnées en tuple pour pas qu'elles soient modifiées.
                self._possible.append((self._x - 2, self._y - 1))

        # i Bas gauche
        if self._x - 2 >= 0 and self._y + 1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x - 2][self._y + 1] == 0:
                self._possible.append((self._x - 2, self._y + 1))

        # i Haut droite
        if self._x + 2 < len(plateau) and self._y - 1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x + 2][self._y - 1] == 0:
                self._possible.append((self._x + 2, self._y - 1))

        # i Bas droite
        if self._x + 2 < len(plateau) and self._y + 1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x + 2][self._y + 1] == 0:
                self._possible.append((self._x + 2, self._y + 1))

        # j Haut gauche
        if self._x - 1 >= 0 and self._y - 2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x - 1][self._y - 2] == 0:
                self._possible.append((self._x - 1, self._y - 2))

        # j Bas gauche PROBLEME
        if self._x - 1 >= 0 and self._y + 2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x - 1][self._y + 2] == 0:
                self._possible.append((self._x - 1, self._y + 2))

        # j Haut droite
        if self._x + 1 < len(plateau) and self._y - 2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x + 1][self._y - 2] == 0:
                self._possible.append((self._x + 1, self._y - 2))

        # j Bas droite PROBLEME
        if self._x + 1 < len(plateau) and self._y + 2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x + 1][self._y + 2] == 0:
                self._possible.append((self._x + 1, self._y + 2))

    def deplacement_possible(self, plateau, x, y, tour):
        """
        Fonction qui renvoit si la case est disponible ou non, si oui renvoit ses coordonnées.
        """
        if tour < 3:
            if plateau[x][y] == '0':
                return True
            return False

        self.cases_possibles(plateau)
        # print("coordonnées possibes : ", self._possible)
        return (x, y) in self._possible


class Jeu:
    def __init__(self):
        self._nb_pions = None
        self._board = []
        self._board_size = None
        self.set_board_size()
        self.set_board()
        self._tour = 0
        # Pour combinaison
        self._pion = Pion(1, 1, 1)
        self._pion2 = Pion(1, 1, 2)

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

    def get_board(self):
        """
        Permet de retourner le tableau.
        """
        return self._board

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

    def placement_pion(self, plateau, x, y):
        """
        Permet de placer un pion selon le joueur et si le déplaceent est possible au vu des règles du jeu sur la case sélectionnée.
        """
        joueur = self._pion.get_joueur()
        print("Peut se placer : ", self._pion.deplacement_possible(plateau, x, y, self._tour))
        if self._pion.deplacement_possible(plateau, x, y, self._tour) is True:
            if joueur == 1:
                plateau[x][y] = 1
            elif joueur == 2:
                plateau[x][y] = 2
        else:
            print("False test peut pas placer pion")

    def placement_croix(self, plateau):
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                if plateau[i][j] == 1:
                    plateau[i][j] = 3
                elif plateau[i][j] == 2:
                    plateau[i][j] = 4

    def verif_haut(self, i, j, alignement):
        alignement = 1
        while alignement != self.get_nombre_de_pions_a_aligner():
            if self._board[i][j - 1] == 3 or self._board[i][j - 1] == 4:
                alignement += 1
            else:
                break
        if alignement >= self.get_nombre_de_pions_a_aligner():
            if self._board[i][j - 1] == 3:
                gagner1 = True
            elif self._board[i][j - 1] == 4:
                gagner2 = True

    def verif_bas(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i][j + 1] == 3 or self._board[i][j + 1] == 4:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                if self._board[i][j + 1] == 3:
                    gagner1 = True
                elif self._board[i][j + 1] == 4:
                    gagner2 = True

    def verif_gauche(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j] == 3 or self._board[i - 1][j] == 3:
                    alignement += 1
                else:
                    break
                if alignement >= self.get_nombre_de_pions_a_aligner():
                    if self._board[i - 1][j] == 3:
                        gagner1 = True
                    elif self._board[i - 1][j] == 4:
                        gagner2 = True

    def verif_droite(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j] == 3 or self._board[i + 1][j + 1] == 4:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j] == 3:
                    gagner1 = True
                elif self._board[i + 1][j] == 4:
                    gagner2 = True

    def verif_diaghautdroit(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j - 1] == 3 or self._board[i + 1][j - 1] == 4:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j - 1] == 3:
                    gagner1 = True
                elif self._board[i + 1][j - 1] == 4:
                    gagner2 = True

    def verif_diaghautgauche(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j - 1] == 3 or self._board[i - 1][j - 1] == 4:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j - 1] == 3:
                    gagner1 = True
                elif self._board[i - 1][j - 1] == 4:
                    gagner2 = True

    def verif_diagbasdroit(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j + 1] == 3 or self._board[i + 1][j + 1] == 4:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                if self._board[i + 1][j + 1] == 3:
                    gagner1 = True
                elif self._board[i + 1][j + 1] == 4:
                    gagner2 = True

    def verif_diagbasgauche(self, i, j, alignement):
        alignement = 1
        if self._board[i][j] == 3 or self._board[i][j] == 4:
            while alignement != self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j + 1] == 3 or self._board[i - 1][j + 1] == 4:
                    alignement += 1
                else:
                    break
            if alignement >= self.get_nombre_de_pions_a_aligner():
                if self._board[i - 1][j + 1] == 3:
                    gagner1 = True
                elif self._board[i - 1][j + 1] == 4:
                    gagner2 = True

    def verif_alignement(self):
        """
        Verifie si le nombre de pions a alignÃ© le sont.
        """
        for i in range(self._board_size):
            for j in range(self._board_size):

                # Coin Haut Gauche
                if i == 0:
                    if j == 0:
                        # Droite
                        alignement = 1
                        self.verif_droite(i, j, alignement)
                        # Bas
                        self.verif_bas(i, j, alignement)
                        # Diagonale Bas Droite
                        self.verif_diagbasdroit(i, j, alignement)

                # Coin Haut Doite
                if i == self._board_size:
                    if j == 0:
                        # Gauche
                        alignement = 1
                        self.verif_diaghautdroit(i, j, alignement)
                        # Bas
                        self.verif_bas(i, j, alignement)
                        # Diagonale Bas Gauche
                        self.verif_diagbasgauche(i, j, alignement)

                # Coin Bas Gauche
                if i == 0:
                    if j == self._board_size:
                        # Droite
                        alignement = 1
                        self.verif_droite(i, j, alignement)
                        # Haut
                        self.verif_haut(i, j, alignement)
                        # Diagonale Haut Droite
                        self.verif_diaghautdroit(i, j, alignement)

                # Coin Bas Doite
                if i == self._board_size:
                    if j == self._board_size:
                        # Gauche
                        alignement = 1
                        self.verif_gauche(i, j, alignement)
                        # Haut
                        self.verif_haut(i, j, alignement)
                        # Diagonale Haut Gauche
                        self.verif_diaghautgauche(i, j, alignement)

                # Ligne Haut
                if j == 0:
                    # Gauche
                    alignement = 1
                    self.verif_gauche(i, j, alignement)
                    # Bas
                    self.verif_bas(i, j, alignement)
                    # Droite
                    self.verif_droite(i, j, alignement)
                    # Diagonale Bas Droite
                    self.verif_diagbasdroit(i, j, alignement)
                    # Diagonale Bas Gauche
                    self.verif_diagbasgauche(i, j, alignement)

                # Ligne Gauche
                if i == 0:
                    # Bas
                    alignement = 1
                    self.verif_bas(i, j, alignement)
                    # Haut
                    self.verif_haut(i, j, alignement)
                    # Droite
                    self.verif_droite(i, j, alignement)
                    # Diagonale Bas Droite
                    self.verif_diagbasdroit(i, j, alignement)
                    # Diagonale Haut Droite
                    self.verif_diaghautdroit(i, j, alignement)

                # Ligne Bas
                if j == self._board_size:
                    # Haut
                    alignement = 1
                    self.verif_haut(i, j, alignement)
                    # Droite
                    self.verif_droite(i, j, alignement)
                    # Gauche
                    self.verif_gauche(i, j, alignement)
                    # Diagonale Haut Droite
                    self.verif_diaghautdroit(i, j, alignement)
                    # Diagonale Haut Gauche
                    self.verif_diaghautgauche(i, j, alignement)

                # Ligne Droite
                if i == self._board_size:
                    # Haut
                    alignement = 1
                    self.verif_haut(i, j, alignement)
                    # Gauche
                    self.verif_gauche(i, j, alignement)
                    # Bas
                    self.verif_bas(i, j, alignement)
                    # Diagonale Bas Gauche
                    self.verif_diagbasgauche(i, j, alignement)
                    # Diagonale Haut Gauche
                    self.verif_diaghautgauche(i, j, alignement)

                # Global
                # Gauche
                else:
                    alignement = 1
                    self.verif_gauche()
                    self.verif_droite()
                    self.verif_haut()
                    self.verif_bas()
                    self.verif_diagbasdroit()
                    self.verif_diagbasgauche()
                    self.verif_diaghautdroit()
                    self.verif_diagbasgauche()

    def end_of_game(self, x, y, tour):
        """
        Permet de vérifier les conditions d'arrêt
        """
        # Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases disponibles) alors, la partie se termine.
        if not self._pion.deplacement_possible(self._board, x, y, self._tour):
            return True
        elif self.verif_alignement() is True and tour > 1:
            return True
        else:
            return False


# ///////////////////////////////////

class Gui(Jeu, Pion):
    def __init__(self, width=600, height=600):
        self._root = Tk()
        self._root.title("La puissance du cavalier")
        Jeu.__init__(self)
        self._taille_case = 500 // self.get_board_size() - 1
        self._plateau = self.get_board()
        self.set_nombre_de_pions_a_aligner()
        self.get_nombre_de_pions_a_aligner()
        self._joueur = 1
        self._x = 0
        self._y = 0

        # Définit la taille de la fenêtre
        self._canvas = Canvas(self._root, width=width, height=height)

        # Affiche le plateau
        plateau_size = self.get_board_size()
        for i in range(plateau_size):
            for j in range(plateau_size):
                self._canvas.create_rectangle((i + 1) * self._taille_case + 2, (j + 1) * self._taille_case + 2,
                                              (i + 1) * self._taille_case + self._taille_case + 2,
                                              (j + 1) * self._taille_case + self._taille_case + 2)

        # Récupère les cliques de l'utilisateur

        self._canvas.bind("<Button-1>", self.set_pions)

        # Lance le GUI
        self._canvas.pack()
        self._root.mainloop()

    def set_pions(self, event):
        """
        Fonction qui place les pions aux coordonnées du click sur le plateau.
        """
        print(self._plateau)
        self._x = (event.x - 50) // self._taille_case
        self._y = (event.y - 50) // self._taille_case
        if self._tour >= 2:
            if 0 <= self._x < self.get_board_size() and 0 <= self._y < self.get_board_size() and self.deplacement_possible(self._plateau, self._x, self._y, self._tour) != False:
                self.placement_pion(self._plateau, self._x, self._y)
                print(self._x, self._y)
                self.affichage_rond(self._x, self._y, self._tour)
        elif 0 <= self._tour < 2:
            self.placement_pion(self._plateau, self._x, self._y)
            print(self._x, self._y)
            self.affichage_rond(self._x, self._y, self._tour)

    def affichage_rond(self, x, y, tour):
        """
        Affiche les pions.
        """
        self._x = x
        self._y = y
        self._tour = tour
        if self._tour % 2 == 0 and self._plateau[self._x][self._y] == 0:
            self._canvas.create_oval((self._x + 1) * self._taille_case + 2 + 3,
                                     (self._y + 1) * self._taille_case + 2 + 3,
                                     (self._x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (self._y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="blue")
            self._tour += 1
            self._plateau[self._x][self._y] = 1
            self.boucle_jeu(self._x, self._y)
            return self._plateau[self._x][self._y], self._tour

        elif self._tour % 2 != 0 and self._plateau[self._x][self._y] == 0:
            self._canvas.create_oval((self._x + 1) * self._taille_case + 2 + 3,
                                     (self._y + 1) * self._taille_case + 2 + 3,
                                     (self._x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (self._y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="red")
            self._tour += 1
            self._plateau[self._x][self._y] = 2
            self.boucle_jeu(self._x, self._y)
            return self._plateau[self._x][self._y], self._tour

    def set_croix(self, x, y):
        self._x = x
        self._y = y
        size = self.get_board_size()
        if self.placement_pion(self._x, self._y):
            for i in range(size):
                for j in range(size):
                    if self._plateau[i][j] == 1:
                        self._plateau[self._x][self._y] = 3
                    elif self._plateau[i][j] == 2:
                        self._plateau[self._x][self._y] = 4
        self.affichage_croix()

    def affichage_croix(self):
        if self._plateau[self._x][self._y] == 3:
            self._canvas.create_line((self._x + 1) * self._taille_case,
                                     (self._y + 1) * self._taille_case,
                                     (self._x + 1) * self._taille_case + self._taille_case,
                                     (self._y + 1) * self._taille_case + self._taille_case, fill="blue",
                                     width=5)
            self._canvas.create_line((self._x + 2) * self._taille_case - self._taille_case,
                                     (self._y + 1) * self._taille_case + self._taille_case,
                                     (self._x + 2) * self._taille_case,
                                     (self._y + 1) * self._taille_case, fill="blue", width=5)

            return self._plateau[self._x][self._y]
        if self._plateau[self._x][self._y] == 4:
            self._canvas.create_line((self._x + 1) * self._taille_case,
                                     (self._y + 1) * self._taille_case,
                                     (self._x + 1) * self._taille_case + self._taille_case,
                                     (self._y + 1) * self._taille_case + self._taille_case, fill="red",
                                     width=5)
            self._canvas.create_line((self._x + 2) * self._taille_case - self._taille_case,
                                     (self._y + 1) * self._taille_case + self._taille_case,
                                     (self._x + 2) * self._taille_case,
                                     (self._y + 1) * self._taille_case, fill="red", width=5)

            self._plateau[self._x][self._y] = 4
            return self._plateau[self._x][self._y]

    def boucle_jeu(self, x, y):
        """
        Fonction qui permet au jeu de fonctionner selon les règles, le déroulement du jeu.
        """
        self._x = x
        self._y = y
        if self.end_of_game(self._x, self._y, self._tour) is False or self._tour >= 1:
            print("Placement pion : ", self.deplacement_possible(self._plateau, self._x, self._y, self._tour))
            print("joueur", self._joueur)
            if self._tour % 2 == 0:
                self._joueur = 1
                print("tour", self._tour)
            else:
                self._joueur = 2
                print(self._tour)
            print("Je passe ici")
            return self._joueur, self._tour
        else:
            return self.end_of_game(self._x, self._y, self._tour)


Gui(600, 600)
