###################################
# UNIDAD 5 - Ejercicio 1          #
# Interfaz gráfica (ESQUEMA)      #
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


#Definición de la clase ----------------------------------------------
class Aplicacion(tk.Frame):      
    
    def __init__(self, master):
        super().__init__(master) #Llamamos al constructor de Frame

        #Inicialización del objeto Aplicacion
        self.master = master
        master.geometry('600x650+50+50') #anchoxalto+x+y
        master.config(bd=20)

        #Disposición del objeto Aplicacion
        self.pack() 

        #Llamamos al método que crea los elementos
        self.crear_widgets()

    def crear_widgets(self):
        #Contenedores ---------------------------------------------------
        fr_arriba = tk.Frame(self.master, bd=10)
        fr_arriba.config(background ='yellow')
        fr_arriba.pack(fill='x', side='top')
        
        fr_centro_arb = tk.Frame(self.master, bd=10)
        fr_centro_arb.config(background ='blue')
        fr_centro_arb.pack(fill='x', side='top')
        
        fr_centro_abj = tk.Frame(self.master, bd=10)
        fr_centro_abj.config(background ='pink')
        fr_centro_abj.pack(fill='x', side='top')
        
        fr_abajo = tk.Frame(self.master, bd=10)
        fr_abajo.config(background ='green')
        fr_abajo.pack(fill='x', side='top')
        
        #Título ---------------------------------------------------------
        titulo_label = ttk.Label(fr_arriba, text="Título:")
        titulo_label.pack()

        self.titulo_entry = ttk.Entry(fr_arriba )
        
        self.titulo_entry.pack()
        self.titulo_entry.focus()
        #Imagen ---------------------------------------------------------
        self.imagen = tk.PhotoImage(file='imagen_no_disponible.png')
        ttk.Label(fr_centro_arb, image=self.imagen).pack()

        #Botón CARGAR----------------------------------------------------
        btn_cargar = ttk.Button(fr_centro_arb, text="Cargar imagen", command=self.cargar).pack()
        
        #Descripcion --------------------------------------------------------
        self.descipcion_text = tk.Text(fr_centro_abj)
        self.descipcion_text.config(width=30, height=5, font=("Courier New", 12), padx=15, pady=15, selectbackground="grey")
        self.descipcion_text.pack(side='left')
        
        #Derechos de autor --------------------------------------------------------
        lf = ttk.LabelFrame(fr_centro_abj, text='Derechos de autor')
        lf.pack(fill='x', side='right')    

        self.opcion_selec = tk.IntVar()
        opciones = [["Creative Commons", 1],["Comercial o licencia", 2]]
        for opc in opciones:
            r = ttk.Radiobutton(lf, text=opc[0], value=opc[1], variable=self.opcion_selec).pack(fill='x', padx=30, pady=5)
        self.opcion_selec.set(1) #valor por defecto
        
        #Botones ------------------------------------------------------------------        
        btn_nuevo = ttk.Button(fr_abajo, text="Nuevo", command=self.nuevo).pack(side='left')
        btn_abrir = ttk.Button(fr_abajo, text="Abrir", command=self.abrir).pack(side='left')
        btn_guardar = ttk.Button(fr_abajo, text="Guardar", command=self.guardar).pack(side='left')
        
        #Creación del menú ========================================================
        self.menubar = tk.Menu(self.master)   #Creamos el objeto Menu
        self.master.config(menu=self.menubar) #Indicamos que es el menú principal

        #Creamos los submenús --------------------------------------------
        self.archivo_menu = tk.Menu(self.menubar, tearoff=False)
        self.ayuda_menu = tk.Menu(self.menubar, tearoff=False)

        #Añadimos opciones al submenú "Archivo" --------------------------
        self.archivo_menu.add_command(label="Nuevo", command=self.nuevo)
        self.archivo_menu.add_command(label="Abrir", command=self.abrir)
        self.archivo_menu.add_command(label="Guardar", command=self.guardar)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.master.destroy)
        
        #Añadimos opciones al submenú "Ayuda" --------------------------
        self.ayuda_menu.add_command(label="Acerca de...", command=self.acerca_de)
        
        #Asignamos los submenús al menú principal -------------------------
        self.menubar.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.menubar.add_cascade(label="Ayuda", menu=self.ayuda_menu)      
        
        
    def cargar(self):
        '''Cargamos una imagen del disco duro'''
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
