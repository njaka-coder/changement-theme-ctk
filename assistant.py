import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Changement de mode")
app.geometry("500x400")

#label d'instructions

label = ctk.CTkLabel(app,text="Cliquer pour changer le mode", font=("Helvetica",16))
label.pack(pady=30)

# Fonctions pour changer le mode
def set_mode_sombre():
    ctk.set_appearance_mode("dark")

def set_mode_clair():
    ctk.set_appearance_mode("light")

#Bouton pour activer la reconnaissance vocale

sombre_boutton=ctk.CTkButton(app, text="Mode Sombre",font=("helvetica",14),height=50,width=200,command=set_mode_sombre)
sombre_boutton.pack(pady=20)

claire_boutton=ctk.CTkButton(app, text="Mode claire",font=("helvetica",14),height=50,width=200,fg_color="red",command=set_mode_clair)
claire_boutton.pack(pady=20)
app.mainloop()