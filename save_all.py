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
        Fonction qui regarde si la case sélectionnée par le joueurs est une des cases sur lesquelles le pion peut se déplacer
        """
        # Vérifie si la case est sur le plateau

        if self._x - 2 >= 0 and self._y - 1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x - 2][self._y - 1] == 0:
                # Mise des coordonnées en tuple pour pas qu'elles soient modifiées
                self._possible.append((self._x - 2, self._y - 1))

        if self._x - 2 >= 0 and self._y + 1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x - 2][self._y + 1] == 0:
                self._possible.append((self._x - 2, self._y + 1))

        if self._x + 2 < len(plateau) and self._y - 1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x + 2][self._y - 1] == 0:
                self._possible.append((self._x + 2, self._y - 1))

        if self._x + 2 < len(plateau) and self._y + 1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x + 2][self._y - 1] == 0:
                self._possible.append((self._x + 2, self._y + 1))

        if self._x - 1 >= 0 and self._y - 2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x - 1][self._y - 2] == 0:
                self._possible.append((self._x - 1, self._y - 2))

        if self._x + 1 < len(plateau) and self._y - 2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x + 1][self._y - 2] == 0:
                self._possible.append((self._x + 1, self._y - 2))

        if self._x - 1 >= 0 and self._y + 2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x - 1][self._y + 2] == 0:
                self._possible.append((self._x - 1, self._y + 2))

        if self._x + 1 < len(plateau) and self._y + 2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x + 1][self._y + 2] == 0 or plateau[self._x - 2][self._y - 1] == 3 or plateau[self._x - 2][self._y - 1] == 4:
                self._possible.append((self._x + 1, self._y + 2))

    def deplacement_possible(self, plateau, x, y):
        """
        Fonction qui renvoit si la case est disponible ou non.
        """
        _ = False
        for i in range(len(plateau)):
            for j in range(len(plateau)):
                if plateau[i][j] == 3 or plateau[i][j] == 4:
                    _ = True

        if _:
            self.cases_possibles(plateau)
            return (x, y) in self._possible
        else:
            return True


# ///////////////////////////////////////////////

class Jeu:
    def __init__(self, nb_pions=4):
        self._board = []
        self._nb_pions = nb_pions
        self._board_size = None
        self.set_board_size()
        self.set_board()
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

    def placement_pion(self, plateau, x, y):
        """
        Permet de placer un pion selon le joueur et si le déplaceent est possible au vu des règles du jeu sur la case sélectionnée.
        """
        joueur = self._pion.get_joueur()
        print(self._pion.deplacement_possible(plateau, x, y))
        if self._pion.deplacement_possible(plateau, x, y) is True:
            if joueur == 1:
                plateau[x][y] = 1
            elif joueur == 2:
                plateau[x][y] = 2

    def placement_croix(self, plateau):
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                if plateau[i][j] == 1:
                    plateau[i][j] = 4
                elif plateau[i][j] == 2:
                    plateau[i][j] = 5

    def verif_alignement(self):
        """
        Verifie si 5 pions sont aignés.
        """
        gagner1 = False
        gagner2 = False
        for i in range(self._board_size):
            for j in range(self._board_size):

                # Pions du joueur 1
                if self._board[i][j] == 4:

                    # Coin Haut Gauche
                    if i == 0:
                        if j == 0:
                            # Droite
                            if self._board[i + 1][j] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Bas
                            elif self._board[i][j + 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j + 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Diagonale Bas Droite
                            elif self._board[i + 1][j + 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j + 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Coin Haut Doite
                    if i == self._board_size:
                        if j == 0:
                            # Gauche
                            if self._board[self._board_size - 1][j] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Bas
                            elif self._board[self._board_size][j + 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j + 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Diagonale Bas Gauche
                            elif self._board[self._board_size - 1][j + 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j + 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Coin Bas Gauche
                    if i == 0:
                        if j == self._board_size:

                            # Droite
                            if self._board[i + 1][self._board_size] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Haut
                            elif self._board[i][self._board_size - 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j - 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True


                            # Diagonale Haut Droite
                            elif self._board[i + 1][self._board_size - 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j - 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Coin Bas Doite
                    if i == self._board_size:
                        if j == self._board_size:

                            # Gauche
                            if self._board[self._board_size - 1][self._board_size] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j] == 4:
                                        alignement += 1
                                    else:
                                        break
                                    if alignement >= self.get_nombre_de_pions_a_aligner():
                                        gagner1 = True

                            # Haut
                            elif self._board[self._board_size][self._board_size - 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j + 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                    if alignement >= self.get_nombre_de_pions_a_aligner():
                                        gagner1 = True

                            # Diagonale Haut Gauche
                            elif self._board[self._board_size - 1][self._board_size - 1] == 4:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j + 1] == 4:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Ligne Haut
                    if j == 0:

                        # Gauche
                        if self._board[i - 1][j] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Bas
                        elif self._board[i][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Droite
                        elif self._board[i + 1][j] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break

                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Bas Droite
                        elif self._board[i + 1][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True


                        # Diagonale Bas Gauche
                        elif self._board[i - 1][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Ligne Gauche
                    if i == 0:
                        # Bas
                        if self._board[i][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Haut
                        elif self._board[i][self._board_size - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Droite
                        elif self._board[i + 1][j] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Bas Droite
                        elif self._board[i + 1][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Haut Droite
                        elif self._board[i + 1][j - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Ligne Bas
                    if j == self._board_size:
                        # Haut
                        if self._board[i][self._board_size - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Droite
                        elif self._board[i + 1][self._board_size] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True


                        # Gauche
                        elif self._board[i - 1][self._board_size] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Haut Droite
                        elif self._board[i + 1][self._board_size - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Haut Gauche
                        elif self._board[i - 1][self._board_size - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Ligne Droite
                    if i == self._board_size:
                        # Haut
                        if self._board[self._board_size][j - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Gauche
                        elif self._board[self._board_size - 1][j] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Bas
                        elif self._board[self._board_size][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Bas Gauche
                        elif self._board[self._board_size - 1][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Haut Gauche
                        elif self._board[self._board_size - 1][j - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Global
                    # Gauche
                    if self._board[i - 1][j] == 4:
                        if self._board[i + 1][j] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j] == 4:
                                    alignement += 1
                                elif self._board[i - 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Droite
                    if self._board[i + 1][j] == 4:
                        if self._board[i - 1][j] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j] == 4:
                                    alignement += 1
                                elif self._board[i - 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Bas
                    if self._board[i][j - 1] == 4:
                        if self._board[i][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 4:
                                    alignement += 1
                                elif self._board[i][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Haut
                    if self._board[i][j + 1] == 4:
                        if self._board[i][j - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 4:
                                    alignement += 1
                                elif self._board[i][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Diag Haut Gauche
                    if self._board[i - 1][j - 1] == 4:
                        if self._board[i + 1][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j - 1] == 4:
                                    alignement += 1
                                elif self._board[i + 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Diag Haut Droite
                    if self._board[i + 1][j - 1] == 4:
                        if self._board[i - 1][j + 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 4:
                                    alignement += 1
                                elif self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Diag Bas Gauche
                    if self._board[i - 1][j + 1] == 4:
                        if self._board[i + 1][j - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                elif self._board[i + 1][j - 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Diag Bas Droite
                    if self._board[i + 1][j + 1] == 4:
                        if self._board[i - 1][j - 1] == 4:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j - 1] == 4:
                                    alignement += 1
                                elif self._board[i + 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j + 1] == 4:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                # Pions du joueur 2
                if self._board[i][j] == 5:

                    # Coin Haut Gauche
                    if i == 0:
                        if j == 0:
                            # Droite
                            if self._board[i + 1][j] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Bas
                            elif self._board[i][j + 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j + 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Diagonale Bas Droite
                            elif self._board[i + 1][j + 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j + 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Coin Haut Doite
                    if i == self._board_size:
                        if j == 0:
                            # Gauche
                            if self._board[self._board_size - 1][j] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Bas
                            elif self._board[self._board_size][j + 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j + 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Diagonale Bas Gauche
                            elif self._board[self._board_size - 1][j + 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j + 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Coin Bas Gauche
                    if i == 0:
                        if j == self._board_size:

                            # Droite
                            if self._board[i + 1][self._board_size] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                            # Haut
                            elif self._board[i][self._board_size - 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j - 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True


                            # Diagonale Haut Droite
                            elif self._board[i + 1][self._board_size - 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i + 1][j - 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Coin Bas Doite
                    if i == self._board_size:
                        if j == self._board_size:

                            # Gauche
                            if self._board[self._board_size - 1][self._board_size] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j] == 5:
                                        alignement += 1
                                    else:
                                        break
                                    if alignement >= self.get_nombre_de_pions_a_aligner():
                                        gagner1 = True

                            # Haut
                            elif self._board[self._board_size][self._board_size - 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i][j + 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                    if alignement >= self.get_nombre_de_pions_a_aligner():
                                        gagner1 = True

                            # Diagonale Haut Gauche
                            elif self._board[self._board_size - 1][self._board_size - 1] == 5:
                                alignement = 1
                                while alignement != self.get_nombre_de_pions_a_aligner():
                                    if self._board[i - 1][j + 1] == 5:
                                        alignement += 1
                                    else:
                                        break
                                if alignement >= self.get_nombre_de_pions_a_aligner():
                                    gagner1 = True

                    # Ligne Haut
                    if j == 0:

                        # Gauche
                        if self._board[i - 1][j] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Bas
                        elif self._board[i][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Droite
                        elif self._board[i + 1][j] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break

                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Bas Droite
                        elif self._board[i + 1][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True


                        # Diagonale Bas Gauche
                        elif self._board[i - 1][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                    # Ligne Gauche
                    if i == 0:
                        # Bas
                        if self._board[i][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Haut
                        elif self._board[i][self._board_size - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Droite
                        elif self._board[i + 1][j] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Bas Droite
                        elif self._board[i + 1][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner1 = True

                        # Diagonale Haut Droite
                        elif self._board[i + 1][j - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Ligne Bas
                    if j == self._board_size:
                        # Haut
                        if self._board[i][self._board_size - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Droite
                        elif self._board[i + 1][self._board_size] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True


                        # Gauche
                        elif self._board[i - 1][self._board_size] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Diagonale Haut Droite
                        elif self._board[i + 1][self._board_size - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Diagonale Haut Gauche
                        elif self._board[i - 1][self._board_size - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Ligne Droite
                    if i == self._board_size:
                        # Haut
                        if self._board[self._board_size][j - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Gauche
                        elif self._board[self._board_size - 1][j] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Bas
                        elif self._board[self._board_size][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Diagonale Bas Gauche
                        elif self._board[self._board_size - 1][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                        # Diagonale Haut Gauche
                        elif self._board[self._board_size - 1][j - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Global
                    # Gauche
                    if self._board[i - 1][j] == 5:
                        if self._board[i + 1][j] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j] == 5:
                                    alignement += 1
                                elif self._board[i - 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Droite
                    if self._board[i + 1][j] == 5:
                        if self._board[i - 1][j] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j] == 5:
                                    alignement += 1
                                elif self._board[i - 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Bas
                    if self._board[i][j - 1] == 5:
                        if self._board[i][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 5:
                                    alignement += 1
                                elif self._board[i][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Haut
                    if self._board[i][j + 1] == 5:
                        if self._board[i][j - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 5:
                                    alignement += 1
                                elif self._board[i][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Diag Haut Gauche
                    if self._board[i - 1][j - 1] == 5:
                        if self._board[i + 1][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j - 1] == 5:
                                    alignement += 1
                                elif self._board[i + 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Diag Haut Droite
                    if self._board[i + 1][j - 1] == 5:
                        if self._board[i - 1][j + 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 5:
                                    alignement += 1
                                elif self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Diag Bas Gauche
                    if self._board[i - 1][j + 1] == 5:
                        if self._board[i + 1][j - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                elif self._board[i + 1][j - 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

                    # Diag Bas Droite
                    if self._board[i + 1][j + 1] == 5:
                        if self._board[i - 1][j - 1] == 5:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i - 1][j - 1] == 5:
                                    alignement += 1
                                elif self._board[i + 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True
                        else:
                            alignement = 1
                            while alignement != self.get_nombre_de_pions_a_aligner():
                                if self._board[i + 1][j + 1] == 5:
                                    alignement += 1
                                else:
                                    break
                            if alignement >= self.get_nombre_de_pions_a_aligner():
                                gagner2 = True

            return gagner1, gagner2

    def end_of_game(self, x, y):
        """
        Permet de vérifier les conditions d'arrêt
        """
        # Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases disponibles) alors, la partie se termine.
        if not self._pion.deplacement_possible(self._board, x, y):
            return True
        elif self.verif_alignement() is True:
            return True


# ///////////////////////////////////

class Gui(Jeu, Pion):
    def __init__(self, width=500, height=500, nb_pions=4):
        self._root = Tk()
        self._root.title("La puissance du cavalier")
        Jeu.__init__(self)
        self.nb_pion = nb_pions
        self._taille_case = 500 // self.get_board_size()
        self._plateau = self.get_board()
        self._tour = 0
        self._joueur_en_cours = 0

        # Définit la taille de la fenêtre
        self._canvas = Canvas(self._root, width=width, height=height)

        # Affiche le plateau
        plateau_size = self.get_board_size()
        for i in range(plateau_size):
            for j in range(plateau_size):
                self._canvas.create_rectangle(i * self._taille_case + 2, j * self._taille_case + 2,
                                              i * self._taille_case + self._taille_case + 2,
                                              j * self._taille_case + self._taille_case + 2)

        # Récupère les cliques de l'utilisateur

        self._canvas.bind("<Button-1>", self.set_pions)

        self.boucle_jeu()

        # Lance le GUI
        self._canvas.pack()
        self._root.mainloop()

    def set_pions(self, event):
        """
        Fonction qui place les pions aux coordonnées du click sur le plateau.
        """
        print(self._plateau)
        coord_x = (event.x - 50) // self._taille_case
        coord_y = (event.y - 50) // self._taille_case
        self._joueur_en_cours = self._joueur
        print("en cours", self._joueur_en_cours)
        self.placement_pion(self._plateau, coord_x, coord_y)

        if self._tour % 2 == 0 and self._pion.deplacement_possible(self._plateau, coord_x, coord_y) is True:
            self._plateau[coord_x][coord_y] = 4
            self._canvas.create_oval((coord_x + 1) * self._taille_case + 2 + 3,
                                     (coord_y + 1) * self._taille_case + 2 + 3,
                                     (coord_x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (coord_y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="blue")
            self._tour += 1
            return coord_x, coord_y, self._joueur_en_cours
        elif self._tour % 2 != 0 and self._pion.deplacement_possible(self._plateau, coord_x, coord_y) is True:
            self._plateau[coord_x][coord_y] = 5
            self._canvas.create_oval((coord_x + 1) * self._taille_case + 2 + 3,
                                     (coord_y + 1) * self._taille_case + 2 + 3,
                                     (coord_x + 1) * self._taille_case + self._taille_case + 2 - 3,
                                     (coord_y + 1) * self._taille_case + self._taille_case + 2 - 3, fill="red")
            self._tour += 1
            return coord_x, coord_y, self._joueur_en_cours

    def set_croix(self):
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                if self._plateau[i][j] == 4:
                    self._canvas.create_line(self._taille_case + 5, self._taille_case + 5, self._taille_case + 63,
                                             self._taille_case + 63, fill="blue", width=5)
                    self._canvas.create_line(self._taille_case + 63, self._taille_case + 5, self._taille_case + 5,
                                             self._taille_case + 63, fill="blue", width=5)
                elif self._plateau[i][j] == 5:
                    self._canvas.create_line(self._taille_case + 5, self._taille_case + 5, self._taille_case + 63,
                                             self._taille_case + 63, fill="red", width=5)
                    self._canvas.create_line(self._taille_case + 63, self._taille_case + 5, self._taille_case + 5,
                                             self._taille_case + 63, fill="red", width=5)

    def boucle_jeu(self):
        """
        Fonction qui permet au jeu de fonctionner selon les règles, le déroulement du jeu.
        """
        self.set_board_size()
        self.set_nombre_de_pions_a_aligner()
        self.get_nombre_de_pions_a_aligner()
        self._x = 0
        self._y = 0
        self._joueur = 0
        self._tour = 0

        truc = self.end_of_game(self._x, self._y)

        if truc is False or truc is None:
            self.set_croix()
            print("joueur", self._joueur)
            print("voir", self._tour % 2)
            if self._tour % 2 == 0:
                self._joueur = 1

                print("tour", self._tour, "joueur en cours",self._joueur_en_cours)
            else:
                self._joueur = 2

                print(self._tour)
            print("Je passe ici")
            return self._joueur, self._tour

        else:
            return self.end_of_game(self._x, self._y)

Gui(500, 500)