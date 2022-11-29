import pygame as pg
class BolasLocas():
    def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=20):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.vy = 0
        self.vx = 0


    def velocidad(self,vx,vy):
        self.vx = vx
        self.vy = vy



    def movimiento(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy
               
        if self.pos_x >= (xmax-self.w) or self.pos_x <= 0:
            self.vx *= -1 
        if self.pos_y >= (ymax-self.h) or self.pos_y <= 0:
            self.vy = self.vy * -1
        
        #return mov
    
class bolillas:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_radio = radio
        self.pos_x = pos_x
        
  
