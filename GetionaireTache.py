from tkinter import *
from tkinter import messagebox

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Gestionnaire de tâches")
fenetre.geometry("400x300")

# Liste des tâches
taches = []

# Fonction pour ajouter une tâche
def ajouter_tache():
    tache = entree_tache.get()
    if tache:
        taches.append(tache)
        messagebox.showinfo("Succès", "Tâche ajoutée avec succès !")
        entree_tache.delete(0, END)
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer une tâche.")

# Fonction pour afficher les tâches
def afficher_taches():
    if taches:
        messagebox.showinfo("Tâches", "\n".join(taches))
    else:
        messagebox.showinfo("Tâches", "Aucune tâche.")

# Éléments de l'interface utilisateur
label_tache = Label(fenetre, text="Tâche :")
label_tache.pack()

entree_tache = Entry(fenetre, width=30)
entree_tache.pack()

btn_ajouter = Button(fenetre, text="Ajouter", command=ajouter_tache)
btn_ajouter.pack()

btn_afficher = Button(fenetre, text="Afficher les tâches", command=afficher_taches)
btn_afficher.pack()

# Boucle principale
fenetre.mainloop()