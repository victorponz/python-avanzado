try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk


# Configuración de la raíz
root = tk.Tk()

#Distintas formas de mostrar una etiqueta con texto -------------------------
#Forma 1:
etiqueta = ttk.Label(root, text="PAISAJE CAMPESTRE")
etiqueta.pack()

#Forma 2:
#etiqueta = ttk.Label(root, text="PAISAJE CAMPESTRE").pack()

#Forma 3:
#ttk.Label(root, text="PAISAJE CAMPESTRE").pack()


#Configuramos el aspecto del texto ------------------------------------------
'''
ttk.Label(root, text="PAISAJE CAMPESTRE",
         font= ("Verdana",24),
         foreground= "white",
         background= "grey"
         ).pack()
'''

#Si la etiqueta ya existe, podemos cambiar la configuración con config()
'''
etiqueta.config(font= ("Verdana",24),
                foreground= "white",
                background= "grey")
'''

# Bucle de la aplicación
root.mainloop()

