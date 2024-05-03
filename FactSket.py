import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk


def factoriser():
    degre = int(entree_degre.get())
    coefficients = []
    for i in range(degre + 1):
        coeff = float(entries_coefficients[i].get())
        coefficients.append(coeff)

    # Construction de l'équation
    equation = ""
    for i in range(degre, 0, -1):
        equation += f"{coefficients[i]}*x^{i} + "
    equation += str(coefficients[0])

    # Factorisation de l'équation
    facteur = np.poly1d(coefficients)
    facteurs = facteur.r
    facteurs_str = " × ".join(f"(x - {f:.2f})" for f in facteurs)

    lbl_factorisation.config(text=f"Factorisation : {facteurs_str}")

    # Tracé de la courbe
    x = np.linspace(-10, 10, 100)
    y = facteur(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y)
    ax.set_title("Courbe de l'équation")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)

    plt.show()


def generer_cases():
    degre = int(entree_degre.get())

    for widget in frame_coefficients.winfo_children():
        widget.destroy()

    for i in range(degre + 1):
        lbl_coefficient = ttk.Label(frame_coefficients, text=f"Coefficient de degré {i}:")
        lbl_coefficient.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry_coefficient = ttk.Entry(frame_coefficients)
        entry_coefficient.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries_coefficients.append(entry_coefficient)

    btn_factoriser = ttk.Button(fenetre, text="Factoriser et Tracer", command=factoriser)
    btn_factoriser.grid(row=3, column=0, columnspan=2, pady=10)

    # Configurer l'expansion des cellules
    fenetre.grid_rowconfigure(2, weight=1)


# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Traceur d'équations")
fenetre.configure(background="#B747D6")

# Style de l'interface
style = ttk.Style()
style.configure('TFrame', background="#B747D6")
style.configure("TLabel", background="#ECECEC")
style.configure("TButton", background="#ACF2AF", foreground="#494CF2", padding=5, font=("Arial", 12))
style.configure("TEntry", padding=5, font=("Arial", 12))

# Cadre principal
main_frame = ttk.Frame(fenetre)
main_frame.grid(sticky="nsew")
main_frame.columnconfigure(1, weight=1)

# Éléments de l'interface utilisateur
lbl_degre = ttk.Label(main_frame, text="Degré de l'équation :")
lbl_degre.grid(row=0, column=0, padx=10, pady=5)

entree_degre = ttk.Entry(main_frame)
entree_degre.grid(row=0, column=1, padx=10, pady=5, sticky="we")

btn_generer = ttk.Button(main_frame, text="Générer", command=generer_cases)
btn_generer.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="we")

frame_coefficients = ttk.Frame(main_frame)
frame_coefficients.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

entries_coefficients = []

lbl_factorisation = ttk.Label(main_frame, text="")
lbl_factorisation.grid(row=3, column=0, columnspan=2, pady=10)

# Configurer l'expansion des cellules
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Boucle principale
fenetre.mainloop()