try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()
root.config(bd=15) #tamaño del borde

# Multilíneas básico ------------------------------------------
texto = tk.Text(root)
texto.pack()

# Multilíneas personalizado ------------------------------------
'''
texto = tk.Text(root)
texto.config(width=30, height=10, font=("Courier New",12), 
             padx=15, pady=15, selectbackground="grey")
texto.pack()
'''

# Inicializamos el contenido ------------------------------------
texto.insert('1.0', 'Hola a tod@s')


# Finalmente bucle de la aplicación
root.mainloop()