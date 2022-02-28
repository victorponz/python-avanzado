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


#DEFINICIÓN DE FUNCIONES =================================================
        
def reset():
    '''Limpiamos los valores de los campos del formulario'''
    texto_nombre.set('')
    opcion_selec.set(-1)
    zumba_valor.set(False)
    latino_valor.set(False)
    regio_valor.set(False)
    
def nuevo():
    '''Empezamos de nuevo'''
    respuesta = tmb.askquestion("Consulta", 
    "Se borrarán los datos del formulario. ¿Estás seguro/a?")
    if respuesta == "yes": #valor "no" para el otro botón
        reset()


def abrir():
    '''Cargamos los datos de un fichero'''
    respuesta = tmb.askquestion("Consulta", 
    "Se borrarán los datos del formulario. ¿Estás seguro/a?")
    if respuesta == "yes": #valor "no" para el otro botón
        try:
            with open("14-datos_ficha.txt", 'r', encoding='utf-8') as fichero:
                for linea in fichero:
                    cadena = linea.rstrip('\n')
                    lista_campos = cadena.split('-')  #Separamos los campos del registro.
                    
                    texto_nombre.set(lista_campos[0]) #nombre
                    opcion_selec.set(lista_campos[1]) #horario
                    zumba_valor.set(lista_campos[2])  #zumba
                    latino_valor.set(lista_campos[3]) #bailes latinos
                    regio_valor.set(lista_campos[4])  #bailes regionales
        except:
            tmb.showerror("Error","El fichero no se ha podido abrir.")

def guardar():
    '''Guardamos los datos en un fichero'''
    respuesta = tmb.askquestion("Consulta", 
    "Se modificarán los datos del fichero. ¿Estás seguro/a?")
    if respuesta == "yes": #valor "no" para el otro botón            
        nombre = texto_nombre.get()
        horario = str(opcion_selec.get())
        zumba = str(zumba_valor.get())
        latinos = str(latino_valor.get())
        regionales = str(regio_valor.get())        
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

#PROGRAMA PRINCIPAL ======================================================
root = tk.Tk() #Creamos la raíz
root.geometry('450x330+50+50') #anchoxalto+x+y
root.config(bd=20)


#WIDGETS =================================================================
#Contenedores ---------------------------------------------------
fr_arriba = tk.Frame(root, bd=10)
#fr_arriba.config(background ='yellow')
fr_arriba.pack(fill='x', side='top')

fr_centro = tk.Frame(root, bd=10)
#fr_centro.config(background ='pink')
fr_centro.pack(fill='x', side='top')

fr_abajo = tk.Frame(root, bd=10)
#fr_abajo.config(background ='green')
fr_abajo.pack(fill='x', side='top')

#Nombre ---------------------------------------------------------                
ttk.Label(fr_arriba, text="Nombre: ").pack(side='left')
texto_nombre = tk.StringVar() 
nombre_entry = ttk.Entry(fr_arriba, textvariable = texto_nombre)
nombre_entry.focus()
nombre_entry.pack(side='left')

#Horario --------------------------------------------------------
lf1 = ttk.LabelFrame(fr_centro, text=' Horario: ')
lf1.pack(fill='x', side='left')        

opcion_selec = tk.IntVar()
opciones = [["Mañana", 1],["Tarde", 2],["Noche", 3]]
for opc in opciones:
    r = ttk.Radiobutton(lf1, text=opc[0], value=opc[1], variable=opcion_selec).pack(fill='x', padx=30, pady=5)        

#Actividad ------------------------------------------------------
lf2 = ttk.LabelFrame(fr_centro, text=' Actividad: ')
lf2.pack(fill='x', side='right')        

zumba_valor = tk.BooleanVar()
chk_zumba = ttk.Checkbutton(lf2, text="Zumba", variable=zumba_valor, onvalue=True, offvalue=False)
chk_zumba.pack(fill='x', padx=30, pady=5)
zumba_valor.set(False)

latino_valor = tk.BooleanVar()
chk_latino = ttk.Checkbutton(lf2, text="Bailes latinos", variable=latino_valor, onvalue=True, offvalue=False)
chk_latino.pack(fill='x', padx=30, pady=5)
latino_valor.set(False)

regio_valor = tk.BooleanVar()
chk_regio = ttk.Checkbutton(lf2, text="Bailes regionales", variable=regio_valor, onvalue=True, offvalue=False)
chk_regio.pack(fill='x', padx=30, pady=5)
regio_valor.set(False)

#Botones ------------------------------------------------------------------        
btn_reset = ttk.Button(fr_abajo, text="Reset", command=reset).pack(side='left')

#Creación del menú ========================================================
menubar = tk.Menu(root)   #Creamos el objeto Menu
root.config(menu=menubar) #Indicamos que es el menú principal

#Creamos los submenús --------------------------------------------
archivo_menu = tk.Menu(menubar, tearoff=False)

#Añadimos opciones al submenú "Archivo" --------------------------
archivo_menu.add_command(label="Nuevo", command=nuevo)
archivo_menu.add_command(label="Abrir", command=abrir)
archivo_menu.add_command(label="Guardar", command=guardar)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.destroy)

#Asignamos los submenús al menú principal -------------------------
menubar.add_cascade(label="Archivo", menu=archivo_menu)        


root.mainloop() #Lanzamos a ejecución el objeto Application
