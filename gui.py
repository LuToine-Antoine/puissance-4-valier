from tkinter import * 
from pion import *
from jeu import *

class Gui(Jeu) :
        def __init__(self, width, height, nb_pions):
            self.__root = Tk()
            self.__root.title("La puissance du cavalier")
            self.__game = Jeu()
            self.__color_dict = {0:"white", 1:"bleu", 2:"red"}
            self.__taille_case = 40

            # Définit la taille de la fenêtre
            self.__canvas = Canvas(self.__root, width=width, height=height)
            

            #Affiche le plateau
            plateau_size = self.__game.get_board_size()
            for i in range(plateau_size ):
                for j in range(plateau_size ):
                    self.__canvas.create_rectangle(i * self.__taille_case, j * self.__taille_case, i *self.__taille_case + self.__taille_case, j * self.__taille_case + self.__taille_case)

                    
            #self.__canvas.bind("<Button-1>", self.set_pions())
            #self.__canvas.bind("<Button-2>", self.start_auto_fire)
            #self.__canvas.bind("<Button-3>", self.fire_on_clic)
            
            #Lance le GUI
            self.__canvas.pack(padx= 200, pady= 200)
            self.__root.mainloop()
            
        def set_pions(self, event):
            '''
            A ajuster pour faire en sorte d'ajouter un pion quand on clique
            '''
            coord_x = event.x//self.__size_x
            coord_y = event.y//self.__size_y
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