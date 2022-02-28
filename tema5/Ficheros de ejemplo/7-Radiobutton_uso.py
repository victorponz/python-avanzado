try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# DEFINICIÓN DE FUNCIONES --------------------------
# Muestra en la etiqueta "selec_texto" el valor seleccionado.
def selecciona():
    selec_texto.set(opcion_selec.get())


# PROGRAMA PRINCIPAL -------------------------------
# Configuración de la raíz
root = tk.Tk()

#Colores
colores = ttk.Label(root, text="COLORES:")
colores.pack(fill='x', padx=10, pady=5)

opcion_selec = tk.IntVar()
opciones = [["Rojo", 1],["Verde", 2],["Azul", 3]]
for opc in opciones:
    r = ttk.Radiobutton(root, text=opc[0], value=opc[1], variable=opcion_selec,
                command=selecciona).pack(fill='x', padx=30, pady=5)

# Etiqueta que muestra el valor seleccionado:
selec_texto = tk.StringVar()
selec_texto.set('')
etq_seleccionado = tk.Label(root, textvariable = selec_texto).pack()

# Finalmente bucle de la aplicación
root.mainloop()