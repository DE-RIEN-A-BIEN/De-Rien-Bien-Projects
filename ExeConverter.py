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


def convert_to_exe():
    script_path = filedialog.askopenfilename(title="Choisir le script Python")

    if script_path:
        script_name = os.path.basename(script_path)
        script_dir = os.path.dirname(script_path)
        output_dir = os.path.join(script_dir, script_name + " EXE")

        os.makedirs(output_dir, exist_ok=True)

        icon_path = filedialog.askopenfilename(title="Choisir l'icône")

        if icon_path:
            icon_name = os.path.basename(icon_path)
            output_name = os.path.splitext(script_name)[0]
            output_path = os.path.join(output_dir, output_name)

            subprocess.call(['pyinstaller', '--onefile', '--icon=' + icon_path, script_path, '-n', output_name])

            os.rename(icon_path, os.path.join(output_dir, icon_name))

            messagebox.showinfo("Conversion terminée", f"Le fichier .exe a été créé avec succès dans :\n{output_dir}")
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une icône.")
    else:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un script Python.")


window = tk.Tk()
window.title("Convertir en .exe")
window.geometry("400x200")

canvas = GradientCanvas(window, width=400, height=200)
canvas.pack(fill="both", expand=True)

title_label = tk.Label(window, text="Convertir en .exe", font=("Arial", 16, "bold"), bg="#F0F0F0")
title_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

convert_button = tk.Button(window, text="Convertir en .exe", command=convert_to_exe, font=("Arial", 12, "bold"),
                           bg="#4CAF50", fg="white", relief=tk.RAISED)
convert_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

script_label = tk.Label(window, text="", font=("Arial", 10), bg="#F0F0F0")
script_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

icon_label = tk.Label(window, text="", font=("Arial", 10), bg="#F0F0F0")
icon_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

window.mainloop()