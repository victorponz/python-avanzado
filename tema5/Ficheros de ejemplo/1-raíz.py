try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    
    
#Creamos la raíz "root"
root = tk.Tk()

#Configuramos la raíz "root"
root.title("Bienvenid@s") #título de la ventana
root.geometry('500x150+250+250') #anchoxalto+x+y

#Bucle de la aplicación
root.mainloop()

