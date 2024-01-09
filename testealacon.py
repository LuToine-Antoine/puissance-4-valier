import tkinter as tk

class Pion:
    def __init__(self, joueur):
        self.joueur = joueur
        self.position = None

class Jeu:
    def __init__(self, dimension=10, pions_a_aligner=5):
        self.dimension = dimension
        self.pions_a_aligner = pions_a_aligner
        self.plateau = [[None for _ in range(dimension)] for _ in range(dimension)]
        self.joueur_courant = 1
        self.pions = [Pion(1), Pion(2)]
        self.fin_de_partie = False

    def placer_pion(self, pion, ligne, colonne):
        pion.position = (ligne, colonne)
        self.plateau[ligne][colonne] = pion

    def deplacer_pion(self, pion, ligne, colonne):
        ancienne_ligne, ancienne_colonne = pion.position
        self.plateau[ancienne_ligne][ancienne_colonne] = None
        self.plateau[ligne][colonne] = pion
        pion.position = (ligne, colonne)

    def verifier_victoire(self):
        # Implémenter la logique de vérification de victoire
        pass

    def verifier_blocage(self):
        # Implémenter la logique de vérification de blocage
        pass

class PlateauGUI:
    def __init__(self, master, jeu):
        self.master = master
        self.jeu = jeu
        self.creer_interface()

    def creer_interface(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.gestion_clic_case)
        self.afficher_plateau()

    def afficher_plateau(self):
        self.canvas.delete("all")
        taille_case = 400 // self.jeu.dimension

        for i in range(self.jeu.dimension):
            for j in range(self.jeu.dimension):
                x1, y1 = j * taille_case, i * taille_case
                x2, y2 = x1 + taille_case, y1 + taille_case

                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                pion = self.jeu.plateau[i][j]
                if pion:
                    couleur = "red" if pion.joueur == 1 else "blue"
                    self.canvas.create_oval(x1, y1, x2, y2, fill=couleur)

    def gestion_clic_case(self, event):
        # Implémenter la gestion du clic sur une case
        pass

# Pour tester le code
if __name__ == "__main__":
    dimension = 10
    pions_a_aligner = 5

    jeu = Jeu(dimension, pions_a_aligner)

    root = tk.Tk()
    plateau_gui = PlateauGUI(root, jeu)
    root.mainloop()
