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
        master.geometry('450x330+50+50') #anchoxalto+x+y
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
        
        fr_centro = tk.Frame(self.master, bd=10)
        #fr_centro.config(background ='pink')
        fr_centro.pack(fill='x', side='top')
        
        fr_abajo = tk.Frame(self.master, bd=10)
        #fr_abajo.config(background ='green')
        fr_abajo.pack(fill='x', side='top')
        
        #Nombre ---------------------------------------------------------                
        ttk.Label(fr_arriba, text="Nombre: ").pack(side='left')
        self.texto_nombre = tk.StringVar() 
        nombre_entry = ttk.Entry(fr_arriba, textvariable = self.texto_nombre)
        nombre_entry.focus()
        nombre_entry.pack(side='left')
        
        #Horario --------------------------------------------------------
        lf1 = ttk.LabelFrame(fr_centro, text=' Horario: ')
        lf1.pack(fill='x', side='left')        
        
        self.opcion_selec = tk.IntVar()
        opciones = [["Mañana", 1],["Tarde", 2],["Noche", 3]]
        for opc in opciones:
            r = ttk.Radiobutton(lf1, text=opc[0], value=opc[1], variable=self.opcion_selec).pack(fill='x', padx=30, pady=5)        
        
        #Actividad ------------------------------------------------------
        lf2 = ttk.LabelFrame(fr_centro, text=' Actividad: ')
        lf2.pack(fill='x', side='right')        

        self.zumba_valor = tk.BooleanVar()
        chk_zumba = ttk.Checkbutton(lf2, text="Zumba", variable=self.zumba_valor, onvalue=True, offvalue=False)
        chk_zumba.pack(fill='x', padx=30, pady=5)
        self.zumba_valor.set(False)

        self.latino_valor = tk.BooleanVar()
        chk_latino = ttk.Checkbutton(lf2, text="Bailes latinos", variable=self.latino_valor, onvalue=True, offvalue=False)
        chk_latino.pack(fill='x', padx=30, pady=5)
        self.latino_valor.set(False)

        self.regio_valor = tk.BooleanVar()
        chk_regio = ttk.Checkbutton(lf2, text="Bailes regionales", variable=self.regio_valor, onvalue=True, offvalue=False)
        chk_regio.pack(fill='x', padx=30, pady=5)
        self.regio_valor.set(False)
        
        #Botones ------------------------------------------------------------------        
        btn_reset = ttk.Button(fr_abajo, text="Reset", command=self.reset).pack(side='left')
        
        #Creación del menú ========================================================
        self.menubar = tk.Menu(self.master)   #Creamos el objeto Menu
        self.master.config(menu=self.menubar) #Indicamos que es el menú principal

        #Creamos los submenús --------------------------------------------
        self.archivo_menu = tk.Menu(self.menubar, tearoff=False)

        #Añadimos opciones al submenú "Archivo" --------------------------
        self.archivo_menu.add_command(label="Nuevo", command=self.nuevo)
        self.archivo_menu.add_command(label="Abrir", command=self.abrir)
        self.archivo_menu.add_command(label="Guardar", command=self.guardar)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.master.destroy)
        
        #Asignamos los submenús al menú principal -------------------------
        self.menubar.add_cascade(label="Archivo", menu=self.archivo_menu)        
        
    def reset(self):
        '''Limpiamos los valores de los campos del formulario'''
        self.texto_nombre.set('')
        self.opcion_selec.set(-1)
        self.zumba_valor.set(False)
        self.latino_valor.set(False)
        self.regio_valor.set(False)
        
    def nuevo(self):
        '''Empezamos de nuevo'''
        respuesta = tmb.askquestion("Consulta", 
        "Se borrarán los datos del formulario. ¿Estás seguro/a?")
        if respuesta == "yes": #valor "no" para el otro botón
            self.reset()


    def abrir(self):
        '''Cargamos los datos de un fichero'''
        respuesta = tmb.askquestion("Consulta", 
        "Se borrarán los datos del formulario. ¿Estás seguro/a?")
        if respuesta == "yes": #valor "no" para el otro botón
            try:
                with open("14-datos_ficha.txt", 'r', encoding='utf-8') as fichero:
                    for linea in fichero:
                        cadena = linea.rstrip('\n')
                        lista_campos = cadena.split('-')  #Separamos los campos del registro.
                        
                        self.texto_nombre.set(lista_campos[0]) #nombre
                        self.opcion_selec.set(lista_campos[1]) #horario
                        self.zumba_valor.set(lista_campos[2])  #zumba
                        self.latino_valor.set(lista_campos[3]) #bailes latinos
                        self.regio_valor.set(lista_campos[4])  #bailes regionales
            except:
                tmb.showerror("Error","El fichero no se ha podido abrir.")
    
    def guardar(self):
        '''Guardamos los datos en un fichero'''
        respuesta = tmb.askquestion("Consulta", 
        "Se modificarán los datos del fichero. ¿Estás seguro/a?")
        if respuesta == "yes": #valor "no" para el otro botón            
            nombre = self.texto_nombre.get()
            horario = str(self.opcion_selec.get())
            zumba = str(self.zumba_valor.get())
            latinos = str(self.latino_valor.get())
            regionales = str(self.regio_valor.get())        
            cadena = nombre + '-' + horario + '-' + zumba + '-' + latinos + '-' + regionales + '\n'
            #tmb.showinfo("Información", cadena)
            try:  
                fichero = open("14-datos_ficha.txt", 'w', encoding='utf-8')
                fichero.write(cadena)              
                fichero.close()
            except:
                tmb.showerror("Error","El fichero no se ha podido abrir.")
            else:
                tmb.showinfo("Información", "Datos guardados en el fichero correctamente.")

#Programa principal ----------------------------------------------
root = tk.Tk() #Creamos la raíz
app = Aplicacion(root)  #Creamos el objeto Aplicacion
app.mainloop() #Lanzamos a ejecución el objeto Aplicacion
