###################################
# UNIDAD 5 - Ejercicio obligatorio#
# Glosario (ESQUEMA)              #
###################################
try:
    import Tkinter as tk
    from Tkinter import ttk
    import Tkinter.messagebox as tmb
    import Tkinter.filedialog as tfd
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    import tkinter.messagebox as tmb
    import tkinter.filedialog as tfd

import os


#Definición de la clase ----------------------------------------------
class Aplicacion(tk.Frame):    
    
    def __init__(self, master):
        super().__init__(master) #Llamamos al constructor de Frame

        #Inicialización del objeto Aplicacion
        self.master = master
        master.geometry('600x370+50+50') #anchoxalto+x+y
        master.config(bd=20)

        #Disposición del objeto Aplicacion
        self.pack() 

        #Llamamos al método que crea los elementos
        self.crear_widgets()

    def crear_widgets(self):
        #Contenedores ---------------------------------------------------
        fr_arriba = tk.Frame(self.master, bd=10)
        #fr_arriba.config(background ='yellow')
        fr_arriba.pack(fill='x', side='top')
        
        fr_centro_arb = tk.Frame(self.master, bd=10)
        #fr_centro_arb.config(background ='blue')
        fr_centro_arb.pack(fill='x', side='top')        
        
        fr_abajo = tk.Frame(self.master, bd=10)
        #fr_abajo.config(background ='green')
        fr_abajo.pack(fill='x', side='top')
        
        #Concepto ---------------------------------------------------------                
                  
        
        #Descripción --------------------------------------------------------
        
        
        #Palabras clave -----------------------------------------------------
        
        
        #Botones ------------------------------------------------------------------        
        
        
        #Creación del menú ========================================================
        self.menubar = tk.Menu(self.master)   #Creamos el objeto Menu
        self.master.config(menu=self.menubar) #Indicamos que es el menú principal

        #Creamos los submenús --------------------------------------------
        

        #Añadimos opciones al submenú "Archivo" --------------------------
        
        
        #Añadimos opciones al submenú "Ayuda" --------------------------
        
        
        #Asignamos los submenús al menú principal -------------------------
        
        
        
    def reset(self):
        pass              
        
        
    def nuevo(self):
        '''Limpiamos el formulario'''
        pass


    def abrir(self):
        '''Cargamos los datos de un fichero'''
        pass
    
    
    def guardar(self):
        '''Guardamos los datos en un fichero'''
        pass


    def acerca_de(self):
        '''Mostramos información del/de la autor/a'''
        pass

#Programa principal ----------------------------------------------
root = tk.Tk() #Creamos la raíz
app = Aplicacion(root)  #Creamos el objeto Aplicacion
app.mainloop() #Lanzamos a ejecución el objeto Aplicacion
