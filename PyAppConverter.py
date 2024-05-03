import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess

class GradientCanvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.bind("<Configure>", self.draw)

    def draw(self, event=None):
        width = self.winfo_width()
        height = self.winfo_height()

        color1 = (0, 0, 255)  # Blue
        color2 = (138, 43, 226)  # Purple

        for y in range(height):
            r = int(color1[0] * (height - y) / height + color2[0] * y / height)
            g = int(color1[1] * (height - y) / height + color2[1] * y / height)
            b = int(color1[2] * (height - y) / height + color2[2] * y / height)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.create_line(0, y, width, y, fill=color)


# Fonction pour convertir en .exe
def convert_to_exe():
    # Sélectionner le script Python
    script_path = filedialog.askopenfilename(title="Choisir le script Python")

    if script_path:
        # Obtenir le nom du script et le répertoire de sortie
        script_name = os.path.basename(script_path)
        script_dir = os.path.dirname(script_path)
        output_dir = os.path.join(script_dir, script_name + " EXE")

        # Créer le répertoire de sortie s'il n'existe pas
        os.makedirs(output_dir, exist_ok=True)

        # Sélectionner l'icône
        icon_path = filedialog.askopenfilename(title="Choisir l'icône")

        if icon_path:
            # Obtenir le nom de l'icône et le chemin de sortie
            icon_name = os.path.basename(icon_path)
            output_name = os.path.splitext(script_name)[0]
            output_path = os.path.join(output_dir, output_name)

            # Convertir en .exe en utilisant PyInstaller
            subprocess.call(['pyinstaller', '--onefile', '--icon=' + icon_path, script_path, '-n', output_name])

            # Déplacer l'icône dans le répertoire de sortie
            os.rename(icon_path, os.path.join(output_dir, icon_name))

            # Afficher un message de conversion réussie
            messagebox.showinfo("Conversion terminée", f"Le fichier .exe a été créé avec succès dans :\n{output_dir}")
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une icône.")
    else:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un script Python.")


# Créer la fenêtre principale
window = tk.Tk()
window.title("Convertir en .exe")
window.geometry("400x200")

# Définir le style
canvas = GradientCanvas(window, width=400, height=200)
canvas.pack(fill="both", expand=True)
window.option_add("*Font", "Arial 10")

# Fonction pour ajuster l'interface lors du redimensionnement de la fenêtre
def on_window_resize(event):
    convert_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    script_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    icon_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

window.bind("<Configure>", on_window_resize)

# Ajouter un titre
title_label = tk.Label(window, text="Convertir en .exe", font=("Arial", 16, "bold"), bg="#F0F0F0")
title_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# Bouton pour convertir en .exe
convert_button = tk.Button(window, text="Convertir en .exe", command=convert_to_exe, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief=tk.RAISED)
convert_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Labels pour afficher le chemin d'accès du script et de l'icône
script_label = tk.Label(window, text="", font=("Arial", 10), bg="#F0F0F0")
script_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

icon_label = tk.Label(window, text="", font=("Arial", 10), bg="#F0F0F0")
icon_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Fonction pour mettre à jour les labels du chemin d'accès
def update_labels():
    # Sélectionner le script Python
    script_path = filedialog.askopenfilename(title="Choisir le script Python")

    # Obtenir le nom du script et le répertoire de sortie
    script_name = os.path.basename(script_path)
    script_dir = os.path.dirname(script_path)
    output_dir = os.path.join(script_dir, script_name + " EXE")

    script_label.config(text="Script sélectionné : " + os.path.basename(filedialog.askopenfilename(title="Choisir le script Python")))
    icon_label.config(text="Icône sélectionnée : " + os.path.join(output_dir, os.path.basename(filedialog.askopenfilename(title="Choisir l'icône"))))

# Lancement de la boucle principale
window.mainloop()