# El juego de la raqueta (ESQUEMA)  #
#####################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import *
from random import randint
import pygame
import time
 
class Pelota: #-------------------------------------------------------
    x = 100
    y = 100
    pasos = 44
    direccionX = 1 #1:oeste 2:este
    direccionY = 1 #1:norte 2:sur
    avance = 1 
    tamanyo = 40 

    def __init__(self):
       self.x = 100
       self.y = 100       
 
    def update(self, dirX, dirY):
        self.direccionX = dirX
        self.direccionY = dirY
        
        pass
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Raqueta: #-------------------------------------------------------
    x = [10]     # posición x de todos los bloques de la serpiente
    y = [0]     # posición y de todos los bloques de la serpiente
    pasos = 44
    direccion = 0   # 0:este/derecha 1:oeste/izquierda 2:norte/arriba 3:sur/abajo
    longitud = 3    # inicialmente el cuerpo está formado por tres bloques
  

    def __init__(self, longitud):
       self.longitud = longitud

       # inicializa la posición de todas las partes del cuerpo de la serpiente
       for i in range(0,3):
           self.x.append(10)
           self.y.append(0)
 
       # posición inicial de la serpiente sin colision
       self.x[1] = 1 * self.pasos
       self.x[2] = 2 * self.pasos
       self.x[3] = 3 * self.pasos

    def update(self, windowHeight):
        # actualiza la posición de los cuadrados del cuerpo de la serpiente
        for i in range(self.longitud-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # actualiza la posición de la cabeza de la serpiente
        if self.direccion == 0: # dirección norte/arriba
            self.y[0] = (self.y[0] - self.pasos) % windowHeight
        if self.direccion == 1: # dirección sur/abajo
            self.y[0] = (self.y[0] + self.pasos) % windowHeight

 
    def moveUp(self):
        self.direccion = 0
 
    def moveDown(self):
        self.direccion = 1     
    
    def draw(self, surface, image):
        # dibuja cada cuadrado del cuerpo de la raqueta
        for i in range(0,self.longitud):
            surface.blit(image,(self.x[i],self.y[i]))  
 
class App: #-------------------------------------------------------
 
    windowWidth = 792
    windowHeight = 660
    x = 0
    y = 0    
    raqueta = 0 # objeto raqueta
    pelota = 0 # objeto pelota
 
    def __init__(self):
        self._running = True
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        self._image_surf = None     # imagen de fondo, aun sin asignar
        self._raqueta_surf = None     # imagen de la raqueta, aun sin asignar
        self._pelota_surf = None     # imagen de la pelota, aun sin asignar
        
        self.raqueta = Raqueta(3)       # creamos un objeto de la clase Raqueta
        #CONTROL 
        #print("RAQUETA: (" + str(self.raqueta.x[1]) + " , " + str(self.raqueta.y[1]) + ")")
        self.pelota = Pelota()     # creamos un objeto de la clase Pelota
        #print("PELOTA: (" + str(self.pelota.x) + " , " + str(self.pelota.y) + ")")
 
    def on_init(self):
        pygame.init()
        self._running = True        
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        #Cargamos las imagenes en pantalla
        self._image_surf = pygame.image.load("cesped.jpg").convert()
        self._raqueta_surf = pygame.image.load("cuadrado.jpg").convert()     
        self._pelota_surf = pygame.image.load("pelota.png").convert()     

    def on_event(self, event):    
        if event.type == QUIT:
            self._running = False

        # comprueba si se ha pulsado una tecla y actúa en consecuencia
        keys = pygame.key.get_pressed()  

        if (keys[K_UP]):
            self.raqueta.moveUp()
 
        if (keys[K_DOWN]):
            self.raqueta.moveDown()
            
        if (keys[K_ESCAPE]):
            self._running = False            


    def isCollision(self,x1,y1,x2,y2,bsize):
        colision = False
        pass
        return colision
     
    def on_loop(self):
 
        # Comprueba si la pelota ha chocado con el borde superior
        #   - Si lleva dirección NE, rebotará hacia SE
        #   - Si lleva dirección NO, rebotará hacia SO
        pass
    
        # Comprueba si la pelota ha chocado con el borde inferior
        #   - Si lleva dirección SE, rebotará hacia NE
        #   - Si lleva dirección SO, rebotará hacia NO                
        pass      

        # Comprueba si la pelota ha chocado con el borde derecho
        #   - Si lleva dirección NE, rebotará hacia NO
        #   - Si lleva dirección SE, rebotará hacia SO        
        pass  
                
        # Comprueba si la pelota ha chocado con el borde izquierdo
        pass
            
        # Comprueba si la pelota ha chocado con la raqueta
        #   - Si lleva dirección NO, rebotará hacia NE
        #   - Si lleva dirección SO, rebotará hacia SE                
        pass
        
        self.raqueta.update(self.windowHeight) # actualiza la posición de la raqueta
        self.pelota.update(self.pelota.direccionX, self.pelota.direccionY) # actualiza la posición de la pelota 

 
    def on_render(self):
        self._display_surf.blit(self._image_surf,(self.x,self.y))
        self.raqueta.draw(self._display_surf, self._raqueta_surf)
        self.pelota.draw(self._display_surf, self._pelota_surf)
        pygame.display.flip()
 
    # cierra los recursos del programa
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init() 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)                         
            self.on_loop()
            self.on_render()
  
            time.sleep (150.0 / 1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
