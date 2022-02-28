try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    
def sumar():
    pass

# Configuración de la raíz
root = tk.Tk()
root.config(bd=15)

#Botón con texto

boton1 = ttk.Button(root, text="Sumar", command=sumar)
boton1.pack()

#boton1['state'] = tk.NORMAL
#boton1['state'] = tk.DISABLED

#Botón con una imagen
'''
imagen = tk.PhotoImage(file="suma.png")
boton1 = ttk.Button(root, image=imagen, command=sumar)
boton1.pack()
'''

#Botón con una imagen y un texto
'''
imagen = tk.PhotoImage(file="suma.png")
boton1 = ttk.Button(root, text="suma ", image=imagen, compound="right", command=sumar)
boton1.pack()
'''

# Finalmente bucle de la aplicación
root.mainloop()

