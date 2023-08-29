import random
import tkinter as tk
from tkinter import messagebox

Alphabet_et_Nombre = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
Alphabet_Nombre_Caractères = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()[]{}<>\/|_-+=:;,.~`^éñç"

def generate_passwords():
    try:
        mot_de_passe = int(entry1.get())
        mot_de_passe2 = int(entry2.get())
        mot_de_passe3 = var.get()

        passwords = []

        for _ in range(mot_de_passe):
            cmdp = ""
            if mot_de_passe >=10 :
                print("Erreur")
            for _ in range(mot_de_passe2):
                if mot_de_passe3 == 1:
                    cmdp += random.choice(Alphabet_Nombre_Caractères)
                elif mot_de_passe3 == 0:
                    cmdp += random.choice(Alphabet_et_Nombre)
            passwords.append(cmdp)

        result_text.set("\n".join(passwords))
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

app = tk.Tk()
app.title("Générateur de mots de passe")

label1 = tk.Label(app, text="Combien de mots de passe souhaitez-vous générer ?")
label1.pack()

entry1 = tk.Entry(app)
entry1.pack()

label2 = tk.Label(app, text="Combien de caractères doit comporter chaque mot de passe ?")
label2.pack()

entry2 = tk.Entry(app)
entry2.pack()

label3 = tk.Label(app, text="Souhaitez-vous ajouter des caractères spéciaux ?")
label3.pack()

var = tk.IntVar()
checkbox = tk.Checkbutton(app, text="Oui", variable=var)
checkbox.pack()

generate_button = tk.Button(app, text="Générer", command=generate_passwords)
generate_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text)
result_label.pack()

app.mainloop()
