from tkinter import * 

class Pion : 
    def __init__(self, position, joueur):
        self.__position = position
        self.__joueur = joueur
        

class Jeu:
    def __init__(self, board = 8, nb_pions = 4):
      self.__board = board
      self.__nb_pions = nb_pions

    def set_board(self):
        taille = int(input("Choisissez une taille de plateau comprise entre 8 et 12 : "))
        self.__board = []
        if 8 <= taille <= 12:
            for i in range(taille) :
                ligne = []
                self.__board.append(ligne)
                for i in range(taille):
                    ligne.append(0)
        else :
            while (8 > taille) or (taille > 12):
                taille = int(input("Taille non prise en charge, veuillez re-saisir une taille de plateau comprise entre 8 et 12 : "))

    def get_board(self):
       return self.__board

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


game = Jeu()
Jeu.set_board()
a = game.get_board()
print(a)