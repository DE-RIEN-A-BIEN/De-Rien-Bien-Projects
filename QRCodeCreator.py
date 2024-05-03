import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def create_qr_code():
    selected_option = options.get()
    content = entry_content.get()

    if selected_option == "Texte":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill="black", back_color="white")
    elif selected_option == "URL":
        content = "https://" + content  # Ajout du préfixe "http://" pour les URL
        qr_image = qrcode.make(content)
    # Ajouter d'autres options ici pour les coordonnées géographiques, les informations de contact, les événements calendrier, etc.

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG Files", "*.png"), ("PDF Files", "*.pdf")))
    if save_path:
        qr_image.save(save_path)

def show_qr_code_info():
    info_text = """Un code QR (Quick Response) est un type de code-barres bidimensionnel qui peut être scanné à l'aide d'un smartphone ou d'un lecteur de QR code. Il peut contenir différents types d'informations, tels que du texte, des URL, des coordonnées géographiques, des informations de contact, des événements calendrier, etc.

Cette application vous permet de créer des codes QR pour différentes utilisations. Sélectionnez le type de contenu que vous souhaitez inclure dans le code QR, entrez le contenu correspondant, puis cliquez sur le bouton 'Créer QR Code'. Vous pouvez ensuite enregistrer le code QR généré au format image (PNG) ou PDF dans le répertoire de votre choix."""

    info_window = Toplevel(root)
    info_window.title("À propos des codes QR")
    info_window.geometry("500x300")
    info_label = Label(info_window, text=info_text, wraplength=400, justify="left")
    info_label.pack(padx=20, pady=20)

# Création de la fenêtre principale
root = Tk()
root.title("Générateur de codes QR")
root.geometry("400x300")

# Création de la frame pour le contenu
content_frame = Frame(root)
content_frame.pack(pady=20)

# Label et Entry pour le contenu
label_content = Label(content_frame, text="Contenu :")
label_content.grid(row=0, column=0, padx=10, pady=10)
entry_content = Entry(content_frame)
entry_content.grid(row=0, column=1, padx=10, pady=10)

# Options pour le type de contenu
options_label = Label(root, text="Type de contenu :")
options_label.pack()
options = StringVar(root)
options.set("Texte")  # Valeur par défaut
content_options = OptionMenu(root, options, "Texte", "URL")  # Ajouter d'autres options ici
content_options.pack(pady=10)

# Bouton pour créer le QR Code
create_button = Button(root, text="Créer QR Code", command=create_qr_code)
create_button.pack(pady=10)

# Bouton pour afficher les informations sur les codes QR
info_button = Button(root, text="À propos des codes QR", command=show_qr_code_info)
info_button.pack(pady=10)

# Boucle principale
root.mainloop()