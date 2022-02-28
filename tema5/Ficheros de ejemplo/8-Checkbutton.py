try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()

#Ingredientes pizza
ingredientes = ttk.Label(root, text="INGREDIENTES PIZZA:")
ingredientes.pack(fill='x', padx=10, pady=5)

queso = tk.BooleanVar()
check1 = ttk.Checkbutton(root, text="Queso", variable=queso, onvalue=True, offvalue=False)
check1.pack(fill='x', padx=30, pady=5)

cebolla = tk.BooleanVar()
check2 = ttk.Checkbutton(root, text="Cebolla", variable=cebolla, onvalue=True, offvalue=False)
check2.pack(fill='x', padx=30, pady=5)

guindilla = tk.BooleanVar()
check3 = ttk.Checkbutton(root, text="Guindilla", variable=guindilla, onvalue=True, offvalue=False)
check3.pack(fill='x', padx=30, pady=5)

# Finalmente bucle de la aplicación
root.mainloop()