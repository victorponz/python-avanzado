try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()
root.geometry("300x300+50+50")

#Creamos el menú principal --------------------------------------------
menubar = tk.Menu(root)   #Creamos el objeto Menu
root.config(menu=menubar) #Indicamos que es el menú principal

#Creamos los submenús --------------------------------------------
archivo_menu = tk.Menu(menubar, tearoff=False)
editar_menu = tk.Menu(menubar, tearoff=False)
ayuda_menu = tk.Menu(menubar, tearoff=False)

#Añadimos opciones al submenú "Archivo" --------------------------
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Cerrar")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.destroy)

#Añadimos opciones al submenú "Editar" ----------------------------
editar_menu.add_command(label="Cortar")
editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Pegar")

#Añadimos opciones al submenú "Ayuda" -----------------------------
ayuda_menu.add_command(label="Ayuda")
ayuda_menu.add_separator()
ayuda_menu.add_command(label="Acerca de...")

#Asignamos los submenús al menú principal -------------------------
menubar.add_cascade(label="Archivo", menu=archivo_menu)
menubar.add_cascade(label="Editar", menu=editar_menu)
menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

#Añadimos un submenú al menú "Archivo" ----------------------------
editar_menu.add_separator()
mas_menu = tk.Menu(editar_menu, tearoff=False)
mas_menu.add_command(label="Importar")
mas_menu.add_command(label="Exportar")
editar_menu.add_cascade(label="Más opciones", menu=mas_menu)

# Bucle de la aplicación
root.mainloop()