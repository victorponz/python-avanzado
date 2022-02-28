try:
    import Tkinter as tk
    from Tkinter import ttk
    import Tkinter.messagebox as tmb
    import Tkinter.filedialog as tfd
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    import tkinter.messagebox as tmb
    import tkinter.filedialog as tfd

#
# DEFINICIÓN DE FUNCIONES -------------------------------------------
#
def informacion():
    tmb.showinfo("Información", "Bienvenid@ al mundo de Python.") # título, mensaje

def atencion():
    tmb.showwarning("Atención", "Puede haber hackers en esta habitación.") # título, mensaje

def error():
    tmb.showerror("Error", "El fichero no existe.") # título, mensaje


def pregunta():
    respuesta = tmb.askquestion("Consulta", 
        "¿Te gusta hacer deporte?")

    if respuesta == "yes": #valor "no" para el otro botón
        pass  #instrucciones para el "sí"
    else:
        pass #instrucciones para el "no"
    
#
# PROGRAMA PRINCIPAL -------------------------------------------------
#

# Configuración de la raíz
root = tk.Tk()
root.config(bd=20)

ttk.Button(root, text="Información", command=informacion).pack()
ttk.Button(root, text="Atención", command=atencion).pack()
ttk.Button(root, text="Error", command=error).pack()
ttk.Button(root, text="Pregunta", command=pregunta).pack()

# Bucle de la aplicación
root.mainloop()