import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


def tracer_courbe():
    fonction = entree_fonction.get()
    try:
        x = np.linspace(-10, 10, 100)
        y = eval(fonction.replace("X", "x"))

        plt.figure(figsize=(8, 6))
        plt.plot(x, y)
        plt.title("Courbe de la fonction")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
    except:
        lbl_erreur.config(text="Erreur: Veuillez entrer une fonction valide.")


# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Traceur de courbes")
fenetre.geometry("300x200")

# Éléments de l'interface utilisateur
lbl_fonction = Label(fenetre, text="Fonction:")
lbl_fonction.pack()

entree_fonction = Entry(fenetre)
entree_fonction.pack()

btn_tracer = Button(fenetre, text="Tracer", command=tracer_courbe)
btn_tracer.pack()

lbl_erreur = Label(fenetre, text="")
lbl_erreur.pack()

# Boucle principale
fenetre.mainloop()