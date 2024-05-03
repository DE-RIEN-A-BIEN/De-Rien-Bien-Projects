from tkinter import *


def convertir():
    unite_source = var_unite_source.get()
    unite_destination = var_unite_destination.get()
    valeur_source = float(entree_valeur.get())

    # Ajoutez ici les conversions pour chaque unité

    conversions = {
        "Celsius to Fahrenheit": (lambda x: (x * 9 / 5) + 32),
        "Fahrenheit to Celsius": (lambda x: (x - 32) * 5 / 9),
        "Kilomètres to Miles": (lambda x: x * 0.621371),
        "Miles to Kilomètres": (lambda x: x * 1.60934),
        # Ajoutez ici d'autres conversions d'unités
        "Kilograms to Pounds": (lambda x: x * 2.20462),
        "Pounds to Kilograms": (lambda x: x * 0.453592),
        "Liters to Gallons": (lambda x: x * 0.264172),
        "Gallons to Liters": (lambda x: x * 3.78541),
        "Inches to Centimeters": (lambda x: x * 2.54),
        "Centimeters to Inches": (lambda x: x * 0.393701),
        "Square Meters to Square Feet": (lambda x: x * 10.7639),
        "Square Feet to Square Meters": (lambda x: x * 0.092903),
        # Ajoutez ici d'autres conversions d'unités
    }

    conversion_key = unite_source + " to " + unite_destination

    if conversion_key in conversions:
        valeur_destination = conversions[conversion_key](valeur_source)
    else:
        valeur_destination = valeur_source

    lbl_resultat.config(text=str(valeur_destination))


# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Convertisseur d'unités")
fenetre.geometry("300x200")

# Variables de contrôle
var_unite_source = StringVar()
var_unite_destination = StringVar()

# Liste des unités disponibles
unites = [
    "Celsius", "Fahrenheit", "Kilomètres", "Miles",
    "Kilograms", "Pounds", "Liters", "Gallons",
    "Inches", "Centimeters", "Square Meters", "Square Feet",
    # Ajoutez ici d'autres unités
]

# Éléments de l'interface utilisateur
lbl_unite_source = Label(fenetre, text="Unité source:")
lbl_unite_source.pack()

menu_unite_source = OptionMenu(fenetre, var_unite_source, *unites)
menu_unite_source.pack()

lbl_unite_destination = Label(fenetre, text="Unité destination:")
lbl_unite_destination.pack()

menu_unite_destination = OptionMenu(fenetre, var_unite_destination, *unites)
menu_unite_destination.pack()

lbl_valeur = Label(fenetre, text="Valeur:")
lbl_valeur.pack()

entree_valeur = Entry(fenetre)
entree_valeur.pack()

btn_convertir = Button(fenetre, text="Convertir", command=convertir)
btn_convertir.pack()

lbl_resultat = Label(fenetre, text="")
lbl_resultat.pack()

# Boucle principale
fenetre.mainloop()