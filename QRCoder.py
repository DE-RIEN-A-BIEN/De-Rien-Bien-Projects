import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


def create_qr_code():
    selected_option = options.get()
    content = entry_content.get()

    if selected_option == "Texte":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill="black", back_color="white")
    elif selected_option == "URL":
        content = "http://" + content  # Ajout du préfixe "http://" pour les URL
        qr_image = qrcode.make(content)
    # Ajouter d'autres options ici pour les coordonnées géographiques, les informations de contact, les événements calendrier, etc.

    preview_image = ImageTk.PhotoImage(qr_image)
    preview_label.configure(image=preview_image)
    preview_label.image = preview_image

    save_image_button.pack()
    save_pdf_button.pack()

def save_image():
    selected_option = options.get()
    content = entry_content.get()
    if selected_option == "Texte":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill="black", back_color="white")
    elif selected_option == "URL":
        qr_image = qrcode.make(content)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG Files", "*.png"),))
    if save_path:
        qr_image.save(save_path)

def save_pdf():
    selected_option = options.get()
    content = entry_content.get()
    if selected_option == "Texte":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill="black", back_color="white")
    elif selected_option == "URL":
        qr_image = qrcode.make(content)
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=(("PDF Files", "*.pdf"),))
    if save_path:
        qr_image.save(save_path, "PDF", resolution=100.0)

# Création de la fenêtre principale
root = Tk()
root.title("Générateur de codes QR")
root.geometry("400x450")
root.configure(bg="#BE398D")

# Création de la frame pour le contenu
content_frame = Frame(root, bg="#BE398D")
content_frame.place(relx=0.5, rely=0.2, anchor=CENTER)

# Label et Entry pour le contenu
label_content = Label(content_frame, text="Contenu :", bg="#BE398D")
label_content.grid(row=0, column=0, padx=10, pady=10)
entry_content = Entry(content_frame)
entry_content.grid(row=0, column=1, padx=10, pady=10)

# Options pour le type de contenu
options_label = Label(root, text="Type de contenu :", bg="#BE398D")
options_label.place(relx=0.5, rely=0.4, anchor=CENTER)
options = StringVar(root)
options.set("Texte")  # Valeur par défaut
content_options = OptionMenu(root, options, "Texte", "URL")  # Ajouter d'autres options ici
content_options.place(relx=0.5, rely=0.45, anchor=CENTER)

# Bouton pour créer le QR Code
create_button = Button(root, text="Créer QR Code", command=create_qr_code, bg="#BE398D")
create_button.place(relx=0.5, rely=0.55, anchor=CENTER)

# Label pour l'aperçu du code QR
preview_label = Label(root, bg="#BE398D")
preview_label.place(relx=0.5, rely=0.7, anchor=CENTER)

# Bouton pour enregistrer l'image
save_image_button = Button(root, text="Télécharger l'image", command=save_image, bg="#BE398D")
save_pdf_button = Button(root, text="Télécharger le PDF", command=save_pdf, bg="#BE398D")

# Boucle principale
root.mainloop()