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
                  
        ttk.Label(fr_arriba, text="Título:").pack(side="left")

        self.texto_concepto = tk.StringVar() 
        concepto_entry = ttk.Entry(fr_arriba, textvariable = self.texto_concepto)        
        concepto_entry.pack(side="left")
        concepto_entry.focus()

        #Descripción --------------------------------------------------------
        self.descipcion_text = tk.Text(fr_centro_arb)
        self.descipcion_text.config(width=23, height=8, font=("Courier New", 12), padx=15, pady=15, selectbackground="grey")
        self.descipcion_text.pack(side='left')
        
        #Palabras clave -----------------------------------------------------
        lf = ttk.LabelFrame(fr_centro_arb, text='Palabras clave')
        lf.pack(fill='x', side='right')    

        self.opcion_selec = tk.IntVar()
        opciones = [["Programación", 1],["Bases de datos", 2],["Robótica", 3],["Inteligencia articifial", 4]]
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
        
        
    def reset(self):
        self.descipcion_text.delete('1.0', 'end')
        self.texto_concepto.set('')
        self.opcion_selec.set(1)                  
        
        
    def nuevo(self):
        '''Limpiamos el formulario'''
        respuesta = tmb.askquestion("Consulta", 
        "Se borrarán los datos del formulario. ¿Estás seguro/a?")
        if respuesta == "yes": #valor "no" para el otro botón
            self.reset()    


    def abrir(self):
        '''Cargamos los datos de un fichero'''
        respuesta = tmb.askquestion("Consulta", 
        "Se borrarán los datos del formulario. ¿Estás seguro/a?")
        if respuesta == "yes": #valor "no" para el otro botón
        
            dir_actual = os.getcwd() #recuperamos el directorio actual.
            nom_fichero = tfd.askopenfilename(title='Seleccionar un fichero', initialdir=dir_actual,
                                            filetypes= (('Fichero TXT', '*.txt'),
                                                        ('Todos los ficheros', '*.*')))
            print(nom_fichero)
            if nom_fichero != None:
                try:
                    with open(nom_fichero, "r", encoding="utf-8") as fich:
                        linea = fich.read()                        
                        cadena = linea.rstrip('\n')
                        #concepto|descripción|materia
                        lista_campos = cadena.split('|')  #Separamos los campos del registro.
                    
                        self.texto_concepto .set(lista_campos[0]) #nombre
                        self.descipcion_text.delete('1.0', 'end')
                        self.descipcion_text.insert('1.0', lista_campos[1])
                        self.opcion_selec.set(lista_campos[2])

                except:
                    tmb.showerror("Error","El fichero no se ha podido abrir.")
    
    
    def guardar(self):
        dlg_save = tfd.asksaveasfilename(
        title="Guardar un fichero", defaultextension=".txt")
        
        if dlg_save != '':        
            titulo = self.texto_concepto.get()
            desc = self.descipcion_text.get('1.0', 'end').rstrip('\n')
            opcion = str(self.opcion_selec.get())     
            cadena = titulo  + '|' + desc + '|' + opcion + '\n'
         
            try:  
                fichero = open(dlg_save, 'w', encoding='utf-8')
                fichero.write(cadena)              
                fichero.close()
            except:
                tmb.showerror("Error","El fichero no se ha podido guardar.")
            else:
                tmb.showinfo("Información", "Datos guardados en el fichero correctamente.")

    def acerca_de(self):
        '''Mostramos información del/de la autor/a'''
        tmb.showinfo("Acerca", "Esta aplicación ha sido creada por Víctor Ponz.") # título, mensaje

#Programa principal ----------------------------------------------
root = tk.Tk() #Creamos la raíz
app = Aplicacion(root)  #Creamos el objeto Aplicacion
app.mainloop() #Lanzamos a ejecución el objeto Aplicacion
