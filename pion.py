from tkinter import * 
from gui import *
from jeu import *

class Pion : 
    def __init__(self, x, y, joueur):
        self.__x = x
        self.__y = y 
        self.__joueur = joueur
        self.__game = Jeu()

    def set_pion_au_depart(self):
        '''
        Permet de placer le pion où l'on veut en début de partie
        '''
        board = self.__game.get_board()
        if self.__joueur == 1 :
            board[self.__x][self.__y] = 1
            return board
        elif self.__joueur == 2 :
            board[self.__x][self.__y] = 2
            return board


    def set_pion_game(self,):
        '''
        Permet de placer le pion durant la partie en fonction des case possibles
        '''
        pass


    def cases_possibles(self,i,j):
        '''
        Fonction qui regarde si la case sélectionnée par le joueurs est une des cases sur lesquelles le pion peut se déplacer
        '''
        poscases = {1 :[i+2][j+1] , 2 : [i-2][j+1], 3 : [i+2][j-1], 4 : [i-2][j-1], 5 : [i+1][j+2], 6 : [i-1][j+2], 7 : [i+1][j-2], 8 : [i-1][j-2]}
        num = 1 
        while num != 8:
            # Case choisie = cases de déplacement et correspond a une case possible
            if self[i][j] == self[poscases] :
                return True
            else :
                None 
            num +=1
        return False 


    def deplacement_possible(self, i,j):
        '''
        Fonction qui, si la fontion "cases_possibles" retourne True, vérifie si la case est libre
        '''
        if self.cases_possibles() == True and self[i][j] == 3 :
            return True
        else :
            return False