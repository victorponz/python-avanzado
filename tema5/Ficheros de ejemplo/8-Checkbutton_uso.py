try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# DEFINICIÓN DE FUNCIONES --------------------------
# Muestra en la etiqueta "selec_texto" el valor seleccionado.
def queso_mod():
    selec_queso.set(queso.get())

def cebolla_mod():
    selec_cebolla.set(cebolla.get())

def guindilla_mod():
    selec_guindilla.set(guindilla.get())


# PROGRAMA PRINCIPAL -------------------------------
# Configuración de la raíz
root = tk.Tk()

#Ingredientes pizza
ingredientes = ttk.Label(root, text="INGREDIENTES PIZZA:")
ingredientes.pack(fill='x', padx=10, pady=5)

queso = tk.BooleanVar()
check1 = ttk.Checkbutton(root, text="Queso", command=queso_mod,
                         variable=queso, onvalue=True, offvalue=False)
check1.pack(fill='x', padx=30, pady=5)

cebolla = tk.BooleanVar()
check2 = ttk.Checkbutton(root, text="Cebolla", command=cebolla_mod,
                         variable=cebolla, onvalue=True, offvalue=False)
check2.pack(fill='x', padx=30, pady=5)

guindilla = tk.BooleanVar()
check3 = ttk.Checkbutton(root, text="Guindilla",command=guindilla_mod,
                         variable=guindilla, onvalue=True, offvalue=False)
check3.pack(fill='x', padx=30, pady=5)


# Etiquetas que muestran los valores seleccionados:
selec_queso = tk.StringVar()
selec_queso.set('')
tk.Label(root, textvariable = selec_queso).pack()

selec_cebolla = tk.StringVar()
selec_cebolla.set('')
tk.Label(root, textvariable = selec_cebolla).pack()

selec_guindilla = tk.StringVar()
selec_guindilla.set('')
tk.Label(root, textvariable = selec_guindilla).pack()


# Finalmente bucle de la aplicación
root.mainloop()