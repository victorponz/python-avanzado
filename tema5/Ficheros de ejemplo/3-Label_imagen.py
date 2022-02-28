try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk


# Configuración de la raíz
root = tk.Tk()

# Solo foto con texto ------------------------------------------------
'''
imagen = tk.PhotoImage(file="winter.png")
ttk.Label(root, image=imagen).pack()
'''

# Foto con texto -----------------------------------------------------
imagen = tk.PhotoImage(file="polaroid.png")
ttk.Label(root, text="Polaroid",
         font= ("Verdana",24),
         foreground= "white",
         background= "grey",
         image=imagen,
         compound="top").pack()


# Bucle de la aplicación
root.mainloop()

