try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()
root.geometry('300x200+50+50') #anchoxalto+x+y

# usuario
usuario_label = ttk.Label(root, text="Usuario:")
usuario_label.pack()

usuario_entry = ttk.Entry(root)
#usuario_entry = ttk.Entry(root, justify='right') #configuramos la alineación del texto
usuario_entry.pack()
usuario_entry.focus()
'''
texto_usuario = tk.StringVar() 
usuario_entry = ttk.Entry(root, textvariable = texto_usuario) #usamos un StringVar para el valor
'''

# contraseña
contra_label = ttk.Label(root, text="Contraseña:")
contra_label.pack()

contra_entry = ttk.Entry(root, show="*") #enmascaramos los caracteres
contra_entry.pack()

# otro
otro_label = ttk.Label(root, text="Otro:")
otro_label.pack()

otro_entry = ttk.Entry(root, state= 'disabled') #deshabilitamos este campo
otro_entry.pack()


# Finalmente bucle de la aplicación
root.mainloop()