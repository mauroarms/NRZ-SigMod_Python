from customtkinter import *
from PIL import Image
# from modulacionporfunciones import modulacion
from modulacionporfunciones import modulacion
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def modular():
    secuencia = entryBits.get()
    if(secuencia == ""):
        error.configure(text="Por favor ingrese una secuencia...")
        error.pack(anchor="w", padx=(25,0))
    else:
        error.configure(text="")
        baudRate = int(br.get())
        tipoModulacion = tMod.get()
        print(secuencia, baudRate, tipoModulacion)
        modulacion(secuencia,baudRate,tipoModulacion)

def validate_binary_input(char, current_value):
    if char.isdigit() and (char == '0' or char == '1'):
        # Limitar la longitud de la cadena a 16 caracteres
        if len(current_value) <= 16:
            return True
    return False

# Configuraciones de Ventana
app = CTk()
app.geometry("1080x480")
app.resizable(0,0)
app.title("NRZ-SigMod")
app.iconbitmap("./img/NRZ-SigMod_Icon.ico")

#Declaración de diferentes imagenes
side_img_data = Image.open("./img/side-img2.png")
nrz_icon_data = Image.open("./img/wave.png")
nave_icon_data = Image.open("./img/nave.png")
signal_icon_data = Image.open("./img/signal.png")
main_icon_data = Image.open("./img/NRZ-SigMod.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(780, 480))
nrz_icon = CTkImage(dark_image=nrz_icon_data, light_image=nrz_icon_data, size=(20,20))
signal_icon = CTkImage(dark_image=signal_icon_data, light_image=signal_icon_data, size=(20,20))
nave_icon = CTkImage(dark_image=nave_icon_data, light_image=nave_icon_data, size=(20,20))
main_icon = CTkImage(dark_image=main_icon_data, light_image=main_icon_data, size=(30,25))


CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")
frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

# Textos

CTkLabel(master=frame, text="NRZ-SigMod", text_color="#031a53", anchor="w", justify="left", font=("Arial Bold", 24), image=main_icon, compound="left").pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Rellene los campos", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

# ENTRY Secuencia Bits
CTkLabel(master=frame, text="  Secuencia de Bits:", text_color="#031a53", anchor="w", justify="left", font=("Arial Bold", 14), image=nrz_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))

validation = frame.register(validate_binary_input) 
entryBits = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#031a53", border_width=1, text_color="#000000", validate="key", validatecommand=(validation, "%S", "%P"))
entryBits.pack(anchor="w", padx=(25, 0))

# COMBOBOX Baud-Rate
CTkLabel(master=frame, text="  Baud-Rate:", text_color="#031a53", anchor="w", justify="left", font=("Arial Bold", 14), image=nave_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))

combo_var = tk.StringVar()
br = CTkComboBox(master=frame, values=["1","2","3","4","5"], variable=combo_var, width=225, fg_color="#EEEEEE", border_color="#031a53", border_width=1, text_color="#000000", dropdown_fg_color="#EEEEEE", button_color="#031a53", dropdown_text_color="#031a53", dropdown_hover_color="#7E7E7E", button_hover_color="#7E7E7E", state="readonly" )
br.pack(anchor="w", padx=(25, 0))
combo_var.set("1")

# COMBOBOX Tipo De Modulacion
CTkLabel(master=frame, text="  Tipo de Modulación Digital:", text_color="#031a53", anchor="w", justify="left", font=("Arial Bold", 14), image=signal_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))

combo_var_mod = tk.StringVar()
tMod=CTkComboBox(master=frame, values=["ask","psk","fsk"], width=225, variable=combo_var_mod, fg_color="#EEEEEE", border_color="#031a53", border_width=1, text_color="#000000", dropdown_fg_color="#EEEEEE", button_color="#031a53", dropdown_text_color="#031a53", dropdown_hover_color="#7E7E7E", button_hover_color="#7E7E7E",state="readonly" )
tMod.pack(anchor="w", padx=(25, 0))
combo_var_mod.set("ask")


# Botón de Modulacion
CTkButton(master=frame, text="Modular", fg_color="#031a53", hover_color="#7E7E7E", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=modular).pack(anchor="w", pady=(40, 0), padx=(25, 0))
error = CTkLabel(master=frame, text_color="#7E7E7E", anchor="w", justify="center", font=("Arial Bold", 16))

app.mainloop()