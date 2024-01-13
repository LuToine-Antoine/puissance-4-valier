from tkinter import *


class Pion:
    def __init__(self, x, y, joueur):
        self.__x = x
        self.__y = y
        self.__joueur = joueur
        self.__possible = []

    def set_pion_game(self, x, y):
        """
        Permet de placer le pion durant la partie en fonction des case possibles
        """
        self.__x = x
        self.__y = y
        return self.__x, self.__y

    def cases_possibles(self, plateau):
        """
        Fonction qui regarde si la case sélectionnée par le joueurs est une des cases sur lesquelles le pion peut se déplacer
        """
        # Vérifie si la case est sur le plateau
        if self.__x-2 >= 0 and self.__y-1 >= 0:
            # Vérifie si la case est vide
            if plateau[self.__x-2][self.__y-1] == 0:
                self.__possible.append(self.__x-2)
                self.__possible.append(self.__y-1)


        if self.__x-2 >= 0 and self.__y-1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self.__x-2][self.__y-1] == 0:
                self.__possible.append(self.__x-2)
                self.__possible.append(self.__y-1)


        if self.__x-2 >= 0 and self.__y+1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self.__x-2][self.__y+1] == 0:
                self.__possible.append(self.__x-2)
                self.__possible.append((self.__y+1))


        if self.__x+2 < len(plateau) and self.__y-1 >= 0:
            # Vérifie si la case est disponible
            if plateau[self.__x+2][self.__y-1] == 0:
                self.__possible.append(self.__x+2)
                self.__possible.append(self.__y-1)


        if self.__x+2 < len(plateau) and self.__y+1 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self.__x+2][self.__y-1] == 0:
                self.__possible.append(self.__x+2)
                self.__possible.append((self.__y+1))


        if self.__x-1 >= 0 and self.__y-2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self.__x-1][self.__y-2] == 0:
                self.__possible.append(self.__x - 1)
                self.__possible.append((self.__y - 2))


        if self.__x+1 < len(plateau) and self.__y-2 >= 0:
            # Vérifie si la case est disponible
            if plateau[self.__x+1][self.__y-2] is None:
                self.__possible.append(self.__x + 1)
                self.__possible.append((self.__y - 2))


        if self.__x-1 >= 0 and self.__y+2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self.__x-1][self.__y+2] == 0:
                self.__possible.append(self.__x - 1)
                self.__possible.append((self.__y + 2))


        if self.__x+1 < len(plateau) and self.__y+2 < len(plateau):
            # Vérifie si la case est disponible
            if plateau[self.__x+1][self.__y+2] == 0:
                self.__possible.append(self.__x + 1)
                self.__possible.append((self.__y + 2))


    def deplacement_possible(self):
        """
        Fonction qui, si la fontion "cases_possibles" retourne True, vérifie si la case est libre
        """
        if self.cases_possibles(self.__x, self.__y):
            return True
        else:
            return False


# ///////////////////////////////////////////////

class Jeu:
    def __init__(self, board=[], board_size=8, nb_pions=4, x = 1, y = 1, joueur = 1):
        self.__board = board
        self.__nb_pions = nb_pions
        self.__board_size = board_size
        Pion.__init__(self, x, y, joueur)

    def set_board_size(self):
        """
        Fonction qui permet de selectionner la taille du plateau entre 8 et 12.
        """
        self.__board_size = int(input("Choisissez une taille de plateau comprise entre 8 et 12 : "))
        while (8 > self.__board_size) or (self.__board_size > 12):
            self.__board_size = int(
                input("Taille non prise en charge, veuillez re-saisir une taille de plateau comprise entre 8 et 12 : "))
        return self.__board_size

    def get_board_size(self):
        """
        Permet d'avoir la taille du plateau.
        """
        return self.__board_size

    def set_board(self):
        """
        Permet d'initialiser le plateau en fonction de la taille entrée.
        """
        self.__board = []
        for i in range(self.__board_size):
            ligne = []
            self.__board.append(ligne)
            for j in range(self.__board_size):
                ligne.append(0)
        return self.__board

    def get_board(self):
        """
        Permet de retourner le tableau.
        """
        return self.__board

    def set_nombre_de_pions_a_aligner(self):
        """
        Permet de définir le nombre de pions à aligner pour gagner.
        """
        self.__nb_pions = int(input("Nombre de pion à aligner entre 4 et 6 : "))

    def get_nombre_de_pions_a_aligner(self):
        """
        Permet de retourner le nombre de pions nécessaire à aligner pour gagner.
        """
        return self.__nb_pions

    def end_of_game(self):
        """
        Permet de vérifier les conditions d'arrêt
        """
        # Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases dispo) alors fin de la partie = vrai
        if not self.deplacement_possible():
            return True
        # elif :


# ///////////////////////////////////

class Gui(Jeu):
    def __init__(self, width=500, height=500, nb_pions=4):
        self.__root = Tk()
        self.__root.title("La puissance du cavalier")
        Jeu.__init__(self)
        self.nb_pion = nb_pions
        self.__color_dict = {0: "white", 1: "bleu", 2: "red"}
        self.__taille_case = 50

        # Définit la taille de la fenêtre
        self.__canvas = Canvas(self.__root, width=width, height=height)

        # Affiche le plateau
        plateau_size = self.get_board_size()
        for i in range(plateau_size):
            for j in range(plateau_size):
                self.__canvas.create_rectangle(i * self.__taille_case + 50, j * self.__taille_case + 50,
                                               i * self.__taille_case + self.__taille_case + 50,
                                               j * self.__taille_case + self.__taille_case + 50)

        # self.__canvas.bind("<Button-1>", self.set_pions())

        # Lance le GUI
        self.__canvas.pack()
        self.__root.mainloop()

    def set_pions(self, event):
        # A ajuster pour faire en sorte d'ajouter un pion quand on clique
        coord_x = event.x // self.__size_x
        coord_y = event.y // self.__size_y


    def boucle_jeu(self):
        pass


game = Jeu(8)
game.set_board_size(8)
game.set_board()
b = game.get_board()
print(b, sep="\n")

Gui(500, 500, 12)
