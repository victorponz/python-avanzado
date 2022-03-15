#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------
# JUEGO DE LA SERPIENTE
#----------------------------

from pygame.locals import *
from random import randint
import pygame

class App:
    windowWidth = 1280
    windowHeight = 720
    x = 300
    y = 100
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
 
    def on_init(self):
        pygame.init()            
        self._running = True        
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        self._image_surf = pygame.image.load("otro_fondo.jpg").convert()
             
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False        
    
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.blit(self._image_surf,(self.x,self.y))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init()
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
