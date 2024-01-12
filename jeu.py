from tkinter import * 
from gui import *
from pion import *

class Jeu:
    def __init__(self, board = [], board_size = 8, nb_pions = 4):
        self.__board = board
        self.__nb_pions = nb_pions
        self.__board_size = board_size


    def set_board_size(self):
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

    def update_board(self, i, j, joueur):
        '''
        Permet de mettre à jour le plateau en fonction des coups joués.
        '''
        print(i,j)
        self.__board[i][j] = joueur
        return self.__board

    def get_board(self):
        '''
        Permet de retourner le tableau.
        '''
        return self.__board


    def set_nombre_de_pions_a_aligner(self, x):
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
        pass
        
    def boucle_jeu(self):
        self.set_board_size()
        self.set_board()
        while self.end_of_game == False : 
            self.get_board
            #self.__pion.self.set_pion_au_depart()
