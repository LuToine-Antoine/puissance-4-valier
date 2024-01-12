from tkinter import * 

class Pion : 
    def __init__(self, x, y, joueur):
        self.__x = x
        self.__y = y 
        self.__joueur = joueur


    def set_pion_game(self,x, y):
        '''
        Permet de placer le pion durant la partie en fonction des case possibles
        '''
        self.__x = x
        self.__y = y
        return self.__x, self.__y


    def cases_possibles(self,i,j):
        '''
        Fonction qui regarde si la case sélectionnée par le joueurs est une des cases sur lesquelles le pion peut se déplacer
        '''

        # Les 0
        poscases_zero_hautg = {1 :[i+2, j+1] , 5 : [i+1, j+2]}
        poscases_zero_basg = {1 :[i+2, j+1] , 5 : [i+1, j+2]}
        return self[i][j] in poscases_zero_basg.values()
        poscases_zero_basd = {4 : [i-2, j-1], 8 : [i-1, j-2]}
        return self[i][j] in poscases_zero_basd.values()
        poscases_zero_hautd = {2 : [i-2, j+1], 6 : [i-1, j+2]}
        
        # Les lignes
        poscases_lignes ={1 :[i+2, j+1] , 3 : [i+2, j-1], 5 : [i+1, j+2],  7 : [i+1, j-2]}
        poscases_lignes ={1 :[i+2, j+1] , 2 : [i-2, j+1], 5 : [i+1, j+2], 6 : [i-1, j+2]}
        poscases_lignes ={1 :[i+2, j+1] , 4 : [i-2, j-1],  6 : [i-1, j+2],  8 : [i-1, j-2]}
        poscases_lignes ={1 :[i+2, j+1] , 2 : [i-2, j+1], 5 : [i+1, j+2], 6 : [i-1, j+2]}

        # Les 0 + 1
        poscases_un_hautgd = {1 :[i+2, j+1] , 5 : [i+1, j+2], 6 : [i-1, j+2]}
        poscases_un_hautgg = {1 :[i+2, j+1] , 3 : [i+2, j-1], 5 : [i+1, j+2]}
    
        poscases_un_basgd = {3 : [i+2, j-1], 7 : [i+1, j-2], 8 : [i-1, j-2]}
        poscases_un_basgg = {1 :[i+2, j+1] , 3 : [i+2, j-1], 7 : [i+1, j-2]}

        poscases_un_basdg = {4 : [i-2, j-1], 7 : [i+1, j-2], 8 : [i-1, j-2]}
        poscases_un_basdd = {2 : [i-2, j+1], 4 : [i-2, j-1], 8 : [i-1, j-2]}

        poscases_un_hautdg ={2 : [i-2, j+1], 4 : [i-2, j-1], 6 : [i-1, j+2]}
        poscases_un_hautdd ={2 : [i-2, j+1], 4 : [i-2, j-1],6 : [i-1, j+2]}

        # Haut
            #Gauche
        if i == 0 :
            if j == 0 :
                return self[i][j] in poscases_zero_hautg.values()
            elif j == 1 :
                return self[i][j] in poscases_un_hautgd.values()

        if i == 1 :
            if j == 1 :
                return self[i][j] in poscases_un_hautgg.values()
            

            #Droite
        if i == self.board_size():
            if j == 0 :
                return self[i][j] in poscases_zero_hautd.values()
            elif j == 1 :
                return self[i][j] in poscases_un_hautdd()
                pass

        if i == self.board_size()-1 :
            if j == 1 :
                return self[i][j] in poscases_un_hautdd.values()
            
            


        #Bas
        
            #Gauche
            #Droite
                pass
        poscases_milieu = {1 :[i+2, j+1] , 2 : [i-2, j+1], 3 : [i+2, j-1], 4 : [i-2, j-1], 5 : [i+1, j+2], 6 : [i-1, j+2], 7 : [i+1, j-2], 8 : [i-1, j-2]}
        # Vérifie si l'élément choisi correspond a l'une des case de déplacement possible (répertoriés dans le dictionnaire)
        return self[i][j] in poscases_milieu.values()


    def deplacement_possible(self, i,j):
        '''
        Fonction qui, si la fontion "cases_possibles" retourne True, vérifie si la case est libre
        '''
        if self.cases_possibles() == True and self[i][j] == 3 :
            return True
        else :
            return False
        

#///////////////////////////////////////////////

class Jeu:
    def __init__(self, board = [], board_size = 8, nb_pions = 4):
        self.__board = board
        self.__nb_pions = nb_pions
        self.__board_size = board_size


    def set_board_size(self, board_size):
        '''
        Fonction qui permet de selectionner la taille du plateau entre 8 et 12.
        '''
        self.__board_size = int(input("Choisissez une taille de plateau comprise entre 8 et 12 : "))
        while (8 > self.__board_size) or (self.__board_size > 12):
            self.__board_size = int(input("Taille non prise en charge, veuillez re-saisir une taille de plateau comprise entre 8 et 12 : "))
        return self.__board_size


    def get_board_size(self):
        '''
        Permet d'avoir la taille du plateau.
        '''
        return self.__board_size


    def set_board(self):
        '''
        Permet d'initialiser le plateau en fonction de la taille entrée.
        '''
        self.__board = []
        for i in range(self.__board_size) :
            ligne = []
            self.__board.append(ligne)
            for i in range(self.__board_size):
                ligne.append(0)
        return self.__board


    def get_board(self):
        '''
        Permet de retourner le tableau.
        '''
        return self.__board


    def set_nombre_de_pions_a_aligner(self):
        '''
        Permet de définir le nombre de pions à aligner pour gagner.
        '''
        self.__nb_pions = int(input("Nombre de pion à aligner entre 4 et 6 : "))


    def get_nombre_de_pions_a_aligner(self):
        '''
        Permet de retourner le nombre de pions nécessaire à aligner pour gagner.
        '''
        return self.__nb_pions



    def end_of_game(self):
        '''
        Permet de vérifier les conditions d'arrêt
        '''
        #Si la case choisie n'est pas une case où l'on peut mettre le pion (plus le cases dispo) alors fin de la partie = vrai
        if self.deplacement_possible(self) == False:
            return True
        #elif :
        


#///////////////////////////////////
    
class Gui(Jeu) :
        def __init__(self, width = 500, height = 500, nb_pions = 4):
            self.__root = Tk()
            self.__root.title("La puissance du cavalier")
            Jeu.__init__(self)
            self.nb_pion = nb_pions
            self.__color_dict = {0:"white", 1:"bleu", 2:"red"}
            self.__taille_case = 50

            # Définit la taille de la fenêtre
            self.__canvas = Canvas(self.__root, width=width, height=height)
            

            #Affiche le plateau
            plateau_size =self.get_board_size()
            for i in range(plateau_size ):
                for j in range(plateau_size ):
                    self.__canvas.create_rectangle(i * self.__taille_case+50, j * self.__taille_case+50, i *self.__taille_case + self.__taille_case+50, j * self.__taille_case + self.__taille_case+50)

                    
            #self.__canvas.bind("<Button-1>", self.set_pions())
            
            #Lance le GUI
            self.__canvas.pack()
            self.__root.mainloop()
            
        def set_pions(self, event):
            #A ajuster pour faire en sorte d'ajouter un pion quand on clique
            coord_x = event.x // self.__size_x
            coord_y = event.y // self.__size_y
            if self.__forest.get_tree_in_grid(coord_x, coord_y).get_state() == 1 :
                self.__forest.set_tree_state_in_grid(coord_x, coord_y, 2)
                self.update_grid()
            pions = []
            plateau = self.__game.get_board()
            for i in range(len(plateau)):
                for j in range(len(plateau)):
                    if plateau[i] == 1 :
                        oval = self.__canvas.create_oval(5 + self.__taille_case*i + 3 ,5 + 3, self.__taille_case*i +self.__taille_case+5 - 3,self.__taille_case+5 - 3, color = "blue")
                        pions.append(oval)
                    if plateau[i] == 2 :
                        oval = self.__canvas.create_oval(5 + self.__taille_case*i + 3 ,5 + 3, self.__taille_case*i +self.__taille_case+5 - 3,self.__taille_case+5 - 3, color = "red")
                        pions.append(oval)

        def boucle_jeu(self):
            pass
                    




game = Jeu(8)
game.set_board_size(8)
game.set_board()
b = game.get_board()
print(b , sep="\n")

Gui(500, 500, 12)