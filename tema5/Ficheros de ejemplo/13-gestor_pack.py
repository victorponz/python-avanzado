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
root.config(bd=20)
root.geometry('400x150+500+300')

#Configuración de los botones básicos ---------------------------
boton1 = ttk.Button(root, text="Uno", command=sumar)
boton1.pack()

boton2 = ttk.Button(root, text="Dos", command=sumar)
boton2.pack()

#Probamos los parámetros <fill> y <expand> ----------------------
#boton1.pack(fill='x')
#boton2.pack(fill='both', expand=True)

#Probamos los parámetros <ipadx> e <ipady> ----------------------
#boton1.pack(ipadx=40, ipady=20)

#Probamos side='left' -------------------------------------------
#boton1.pack(side='left')
#boton2.pack(side='left')

#Probamos side='right' -------------------------------------------
#boton1.pack(side='right')
#boton2.pack(side='right')

#Probamos side='bottom' -------------------------------------------
#boton1.pack(side='bottom')
#boton2.pack(side='bottom')


# Bucle de la aplicación
root.mainloop()

