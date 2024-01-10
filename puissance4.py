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
        ''' Fonction qui permet de selectionner la taille du plateau entre 8 et 12.'''

        self.__board_size = int(input("Choisissez une taille de plateau comprise entre 8 et 12 : "))
        while (8 > self.__board_size) or (self.__board_size > 12):
            self.__board_size = int(input("Taille non prise en charge, veuillez re-saisir une taille de plateau comprise entre 8 et 12 : "))
        return self.__board_size

    def get_board_size(self):
        '''Permet d'avoir la taille du plateau.'''
        return self.__board_size


    def set_board(self):
        '''Permet d'initialiser le plateau en fonction de la taille entrée.'''
        self.__board = []
        for i in range(self.__board_size) :
            ligne = []
            self.__board.append(ligne)
            for i in range(self.__board_size):
                ligne.append(0)
        return self.__board


    def get_board(self):
        '''Permet de retourner le tableau.'''
        return self.__board


    def set_nombre_de_pions_a_aligner(self, x):
        '''Permet de définir le nombre de pions à aligner pour gagner.'''
        self.__nb_pions = int(input("Nombre de pion à aligner entre 4 et 6 : "))


    def get_nombre_de_pions_a_aligner(self):
        '''Permet de retourner le nombre de pions nécessaire à aligner pour gagner'''
        return self.__nb_pions

    
    def cases_possibles(self,i,j):
        '''
        Fonction qui regarde si la case sélectionnée par le joueurs est une des cases sur lesquelles le pion peut se déplacer
        '''
        poscases = {1 :[i+2][j+1] , 2 : [i-2][j+1], 3 : [i+2][j-1], 4 : [i-2][j-1], 5 : [i+1][j+2], 6 : [i-1][j+2], 7 : [i+1][j-2], 8 : [i-1][j-2]}
        num = 1 
        while num != 8:
            # Case choisie = cases de déplacement et correspond a une case possible
            if self[i][j] == self[poscases] and self[i][j] == 2:
                return True
            else :
                None 
            num +=1


    def deplacement_possible(self, i,j):
        '''Fonction qui, si la fontion "cases_possibles" retourne True, vérifie si la case est libre'''
        pass


class Gui(Jeu) :
        def __init__(self, width, height, nb_pions):
            self.__root = Tk()
            self.__root.title("La puissance du cavalier")
            self.__plateau = Jeu()
            self.__size = self.__plateau.get_board_size()
            self.__color_dict = {0:"white", 1:"bleu", 2:"red"}
            self.__taille_case = 40

            # Définit la taille de la fenêtre
            self.__canvas = Canvas(self.__root, width=width, height=height)
            

            #Affiche le plateau
            plateau = self.__plateau.get_board_size()
            for i in range(plateau):
                for j in range(plateau):
                    self.__canvas.create_rectangle(i * self.__taille_case, j * self.__taille_case, i *self.__taille_case + self.__taille_case, j * self.__taille_case + self.__taille_case)
                    


            #self.__canvas.bind("<Button-1>", self.update_on_clic)
            #self.__canvas.bind("<Button-2>", self.start_auto_fire)
            #self.__canvas.bind("<Button-3>", self.fire_on_clic)
            
            #Lance le GUI
            self.__canvas.pack()
            self.__root.mainloop()
            

game = Jeu(8)
game.set_board_size(8)
game.set_board()
b = game.get_board()
print(b , sep="\n")

Gui(1000, 800, 8)