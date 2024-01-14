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

        if self._x-2 >= 0 and self._y-1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x-2][self._y-1] == 0:
                # Mise des coordonnées en tuple pour pas qu'elles soient modifiées
                self._possible.append((self._x-2, self._y-1))

        if self._x-2 >= 0 and self._y+1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x-2][self._y+1] == 0:
                self._possible.append((self._x-2, self._y+1))

        if self._x+2 < len(plateau) and self._y-1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x+2][self._y-1] == 0:
                self._possible.append((self._x+2, self._y-1))

        if self._x+2 < len(plateau) and self._y+1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x+2][self._y-1] == 0:
                self._possible.append((self._x+2, self._y+1))

        if self._x-1 >= 0 and self._y-2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x-1][self._y-2] == 0:
                self._possible.append((self._x - 1, self._y - 2))

        if self._x+1 < len(plateau) and self._y-2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self._x+1][self._y-2] == 0:
                self._possible.append((self._x + 1, self._y - 2))

        if self._x-1 >= 0 and self._y+2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x-1][self._y+2] == 0:
                self._possible.append((self._x - 1, self._y + 2))

        if self._x+1 < len(plateau) and self._y+2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self._x+1][self._y+2] == 0 or plateau[self._x-2][self._y-1] == 3 or plateau[self._x-2][self._y-1] == 4:
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
                self.placement_croix(plateau)
            elif joueur == 2:
                plateau[x][y] = 2
                self.placement_croix(plateau)

    def placement_croix(self, plateau):
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                if plateau[i][j] == 1:
                    plateau[i][j] = 4
                elif plateau[i][j] == 2:
                    plateau[i][j] = 5

    def end_of_game(self):
        """
        Permet de vérifier les conditions d'arrêt
        """
        # Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases disponibles) alors, la partie se termine.
        # if not self._pion.deplacement_possible(self._board, x, y):
        # return True
        # elif :


# ///////////////////////////////////

class Gui(Jeu, Pion):
    def __init__(self, width=500, height=500, nb_pions=4):
        self._root = Tk()
        self._root.title("La puissance du cavalier")
        Jeu.__init__(self)
        self.nb_pion = nb_pions
        # self._color_dict = {0: "white", 1: "bleu", 2: "red"}
        self._taille_case = 500 // self.get_board_size()
        self._plateau = self.get_board()

        # Définit la taille de la fenêtre
        self._canvas = Canvas(self._root, width=width, height=height)

        # Affiche le plateau
        plateau_size = self.get_board_size()
        for i in range(plateau_size):
            for j in range(plateau_size):
                self._canvas.create_rectangle(i * self._taille_case + 2, j * self._taille_case + 2, i * self._taille_case + self._taille_case + 2, j * self._taille_case + self._taille_case + 2)

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
        coord_x = (event.x - 50) // self._taille_case
        coord_y = (event.y - 50) // self._taille_case
        self.placement_pion(self._plateau, coord_x, coord_y)
        if self._pion.get_joueur() == 1 and self._pion.deplacement_possible(self._plateau, coord_x, coord_y) is True:
            self._canvas.create_oval((coord_x+1) * self._taille_case + 2 + 3, (coord_y+1) * self._taille_case + 2 + 3,
                                     (coord_x+1) * self._taille_case + self._taille_case + 2 - 3,
                                     (coord_y+1) * self._taille_case + self._taille_case + 2 - 3, fill="blue")
        elif self._pion2.get_joueur() == 2 and self._pion.deplacement_possible(self._plateau, coord_x, coord_y) is True:
            self._canvas.create_oval((coord_x+1) * self._taille_case + 2 + 3, (coord_y+1) * self._taille_case + 2 + 3,
                                     (coord_x+1) * self._taille_case + self._taille_case + 2 - 3,
                                     (coord_y+1) * self._taille_case + self._taille_case + 2 - 3, fill="red")

    def boucle_jeu(self):
        """
        Fonction qui permet au jeu de fonctionner selon les règles, le déroulement du jeu.
        """
        pass


Gui(500, 500, 12)