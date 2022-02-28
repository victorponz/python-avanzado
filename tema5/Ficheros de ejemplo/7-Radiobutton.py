try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()

#Colores
colores = ttk.Label(root, text="COLORES:")
colores.pack(fill='x', padx=10, pady=5)

opcion = tk.IntVar()
ttk.Radiobutton(root, text="Rojo", value=1, variable=opcion).pack(fill='x', padx=30, pady=5)
ttk.Radiobutton(root, text="Verde", value=2, variable=opcion).pack(fill='x', padx=30, pady=5)
ttk.Radiobutton(root, text="Azul", value=3, variable=opcion).pack(fill='x', padx=30, pady=5)


# Finalmente bucle de la aplicación
root.mainloop()