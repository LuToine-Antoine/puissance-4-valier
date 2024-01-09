from tkinter import * 

class Pion : 
    def __init__(self, position, joueur):
        self.__position = position
        self.__joueur = joueur
        

class Jeu:
    def __init__(self, board = [], board_size = 8, nb_pions = 4):
        self.__board = board
        self.__nb_pions = nb_pions
        self.__board_size = board_size


    def set_board_size(self, board_size):
        ''' Fonction qui permet de selectionner la taille du plateau entre 8 et 12'''

        self.__board_size = int(input("Choisissez une taille de plateau comprise entre 8 et 12 : "))
        while (8 > self.__board_size) or (self.__board_size > 12):
            self.__board_size = int(input("Taille non prise en charge, veuillez re-saisir une taille de plateau comprise entre 8 et 12 : "))
        return self.__board_size

    def get_board_size(self):
        return self.__board_size


    #Permet de définir le plateau en fonction de la taille sélectionnée 
    def set_board(self):
        self.__board = []
        for i in range(self.__board_size) :
            ligne = []
            self.__board.append(ligne)
            for i in range(self.__board_size):
                ligne.append(0)
        return self.__board


    # Permet d'afficher le tableau
    def get_board(self):
        for i in range(len(self.__board)):
            print(*self.__board[i])


    def set_nombre_de_pions(self, x):
        self.__nb_pions = int(input("Nombre de pion a aligner entre 4 et 6 : "))


    def get_nombre_de_pions(self):
        return self.__nb_pions


    # Fonction qui définit les différents status possibles pour une case (cf "note.txt")

    def statut_cases(self,i):
        if self[i] == 0 :
            print(".")
        if self[i] == 1 :
            print("O")
        if self[i] == 2 :
            print("P")
        if self[i] == 3 :
            print("X")


    # Fonction qui regarde si la case sélectionnée par le joueurs est une des cases sur lesquelles le pion peut se déplacer
    
    def cases_possibles(self,i,j):
        poscases = {1 :[i+2][j+1] , 2 : [i-2][j+1], 3 : [i+2][j-1], 4 : [i-2][j-1], 5 : [i+1][j+2], 6 : [i-1][j+2], 7 : [i+1][j-2], 8 : [i-1][j-2]} ## ELLE N'Y SONT PAS TOUTES ! A RAJOUTER
        num = 1 
        while num != 8:
            # Case choisie = cases de déplacement et correspond a une case possible
            if self[i][j] == self[poscases] and self[i][j] == 2:
                return True
            elif num+1 == 8:
                return "Plus de cases dispos"
            else :
                None 
            num +=1


    # Fonction qui, si la fontion "cases_possibles" retourne True, vérifie si la case est libre

    def deplacement_possible(self, i,j):
        pass


class Gui(Jeu) :
        def __init__(self, width, height, nb_pions):
            self.__root = Tk()
            self.__root.title("La puissance du cavalier")
            self.__plateau = Jeu()
            self.__size = self.__plateau.get_board_size()
            self.__color_dict = {0:"white", 1:"bleu", 2:"red"}

            self.__canvas = Canvas(self.__root, width=width, height=height)
            self.__rectangles = []
            for i in range(self.__plateau.get_board()):
                self.__rectangles.append([])
                for j in range(self.__):
                    color = self.__color_dict[self.__forest.get_tree_in_grid(i,j).get_state()]
                    rectangle = self.__canvas.create_rectangle(i * self.__size_x, j * self.__size_y,
                                                            i * self.__size_x + self.__size_x, j * self.__size_y + self.__size_y,
                                                            fill=color)
                    self.__rectangles[i].append(rectangle)


            self.__canvas.bind("<Button-1>", self.update_on_clic)
            self.__canvas.bind("<Button-2>", self.start_auto_fire)
            self.__canvas.bind("<Button-3>", self.fire_on_clic)


            self.__canvas.pack()

            self.__root.mainloop()
        pass

game = Jeu(8)
game.set_board_size(8)
game.set_board()
game.get_board()

Gui(20,20,4)