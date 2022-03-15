#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------
# JUEGO DE LA SERPIENTE
#----------------------------

from pygame.locals import *
from random import randint
import pygame
import time


class Orange: #-------------------------------------------------------
    x = 0
    y = 0
    pasos = 44
 

    def __init__(self,param_x,param_y):
        self.x = param_x * self.pasos
        self.y = param_y * self.pasos
 
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 

 
class Apple: #-------------------------------------------------------
    x = 0
    y = 0
    pasos = 44
 

    def __init__(self,param_x,param_y):
        self.x = param_x * self.pasos
        self.y = param_y * self.pasos
 
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Snake: #-------------------------------------------------------
    x = [0]     # posición x de todos los bloques de la serpiente
    y = [0]     # posición y de todos los bloques de la serpiente
    pasos = 44
    direccion = 0   # 0:este/derecha 1:oeste/izquierda 2:norte/arriba 3:sur/abajo
    longitud = 3    # inicialmente el cuerpo está formado por tres bloques
  

    def __init__(self, longitud):
       self.longitud = longitud

       # inicializa la posición de todas las partes del cuerpo de la serpiente
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # posición inicial de la serpiente sin colision
       self.x[1] = 1 * self.pasos
       self.x[2] = 2 * self.pasos
 

    def update(self, windowWidth, windowHeight):
        # actualiza la posición de los cuadrados del cuerpo de la serpiente
        for i in range(self.longitud-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # actualiza la posición de la cabeza de la serpiente
        if self.direccion == 0: # dirección este/derecha
            self.x[0] = (self.x[0] + self.pasos) % windowWidth
        if self.direccion == 1: # dirección oeste/izquierda
            self.x[0] = (self.x[0] - self.pasos) % windowWidth
        if self.direccion == 2: # dirección norte/arriba
            self.y[0] = (self.y[0] - self.pasos) % windowHeight
        if self.direccion == 3: # dirección sur/abajo
            self.y[0] = (self.y[0] + self.pasos) % windowHeight

 
    def moveRight(self):
        self.direccion = 0
 
    def moveLeft(self):
        self.direccion = 1
 
    def moveUp(self):
        self.direccion = 2
 
    def moveDown(self):
        self.direccion = 3 
 
    def draw(self, surface, image_head, image):
        surface.blit(image_head, (self.x[0],self.y[0]))

        # dibuja cada cuadrado del cuerpo de la serpiente
        for i in range(1,self.longitud):
            surface.blit(image,(self.x[i],self.y[i]))  

 
class App: #-------------------------------------------------------
 
    windowWidth = 792 
    windowHeight = 660 
    x = 0
    y = 0    
    snake = 0 # objeto serpiente
    apple = 0 # objeto manzana
    orange = 0 # objeto caracol
 
    def __init__(self):
        self._running = True
        self._display_surf = None   # Surface (superficie) que mostrara las imagenes
        
        self._image_surf = None     # imagen de fondo, aún sin asignar
        self._snake_head_surf = None # imagen de la cabeza de la serpiente, aún sin asignar        
        self._snake_surf = None     # imagen de la serpiente, aún sin asignar
        self._apple_surf = None     # imagen de la manzana, aún sin asignar
        self._orange_surf = None		# imagen del caracol, aún sin asignar
        
        self.snake = Snake(3)       # creamos un objeto de la clase Snake
        self.apple = Apple(5,5)     # creamos un objeto de la clase Apple
        self.orange = Orange(10,10)	# creamos un objeto de la clase Orange
 
    def on_init(self):
        pygame.init()
        self._running = True        
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        #Cargamos las imagenes en pantalla
        self._image_surf = pygame.image.load("cesped.jpg").convert()
        self._snake_head_surf = pygame.image.load("cabeza.jpg").convert()        
        self._snake_surf = pygame.image.load("cuadrado.jpg").convert()
        self._apple_surf = pygame.image.load("manzana.png").convert_alpha()
        self._orange_surf = pygame.image.load("naranja.png").convert_alpha()
 
    def on_event(self, event):    
        if event.type == QUIT:
            self._running = False

        # comprueba si se ha pulsado una tecla y actua en consecuencia
        keys = pygame.key.get_pressed()  
        if (keys[K_RIGHT]):
            self.snake.moveRight()
 
        if (keys[K_LEFT]):
            self.snake.moveLeft()
 
        if (keys[K_UP]):
            self.snake.moveUp()
 
        if (keys[K_DOWN]):
            self.snake.moveDown()
 
        if (keys[K_ESCAPE]):
            self._running = False            

    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
     
    def on_loop(self):
        self.snake.update(self.windowWidth, self.windowHeight) # actualiza la posición de la serpiente
 
        # comprueba si la serpiente se ha comido una manzana
        for i in range(0,self.snake.longitud):
            if self.isCollision(self.apple.x,self.apple.y,self.snake.x[i],self.snake.y[i],self.snake.pasos):
                self.apple.x = randint(2,9) * self.apple.pasos
                self.apple.y = randint(2,9) * self.apple.pasos
                self.snake.longitud = self.snake.longitud + 1

		# comprueba si la serpiente se ha comido un caracol
        for i in range(0,self.snake.longitud):
            if self.isCollision(self.orange.x,self.orange.y,self.snake.x[i], self.snake.y[i],self.snake.pasos):
                self.orange.x = randint(2,9) * self.orange.pasos
                self.orange.y = randint(2,9) * self.orange.pasos
                self.snake.longitud = self.snake.longitud + 1                
 
        # comprueba si la serpiente ha chocado consigo misma
        for i in range(2,self.snake.longitud):
            if self.isCollision(self.snake.x[0],self.snake.y[0],self.snake.x[i], self.snake.y[i],40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.snake.x[0]) + "," + str(self.snake.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.snake.x[i]) + "," + str(self.snake.y[i]) + ")")
                exit(0)
 
 
    def on_render(self):
        self._display_surf.blit(self._image_surf,(self.x,self.y))
        self.snake.draw(self._display_surf, self._snake_head_surf, self._snake_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.orange.draw(self._display_surf, self._orange_surf)
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
