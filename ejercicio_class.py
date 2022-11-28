'''
from clase_bolas import BolasLocas
import pygame as pg

#inicializar todos los modulos de pygame
#pantallas,sonidos,teclados,etc
pg.init()

#creamos una pantalla o surface
pantalla_principal = pg.display.set_mode( (800,600) )# ventana y tamaño de ventana
pg.display.set_caption("Bolillas rebotando")# titulo de la ventana




'''
x = 400
y = 300
vx = 1
vy = 1
'''
game_over = False
contador = 0
x = 400
y = 300
vx = 1
vy = 1
bola1 = BolasLocas(400,300,20,20)
while not game_over:#bucle para ejecutar los fotogramas para el repintado de la pantalla

    for eventos in pg.event.get():# captura todos los eventos de pygame en forma de lista
        #print(eventos)
        if eventos.type == pg.QUIT:#controlar que pare el bucle
            game_over = True

    pantalla_principal.fill( (73, 162, 240) )

  
    x += vx
    y += vy
    if x >= 800 or x == 0:#llegue a los limites
        vx = vx * -1 
    if y >= 600 or y == 0:
        vy = vy * -1
    #x = 400
    #y = 300
    
    #print(bola1)
    pg.draw.rect(pantalla_principal,(250, 248, 55),bola1)
    '''
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x +50,y+40,20,20))
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x-100,-200,20,20))
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x-200,y-300,20,20))
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x-400,y-250,20,20))
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x-50,y-150,20,20))
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x+100,y+200,20,20))
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x+200,y+200,20,20))
    '''
    #bola1 = BolasLocas(self,100,50,20,20)
    pg.display.flip()#para activar el color que le hemos asignado con rgb

    contador += 1




pg.quit
'''