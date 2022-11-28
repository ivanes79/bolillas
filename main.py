import pygame as pg

#inicializar todos los modulos de pygame
#pantallas,sonidos,teclados,etc
pg.init()

#creamos una pantalla o surface
pantalla_principal = pg.display.set_mode( (800,600) )# ventana y tamaño de ventana
pg.display.set_caption("Bolillas rebotando")# titulo de la ventana

#es una variable para controlar el bucle
game_over = False
contador = 0
x = 400
y = 300
vx = 1
vy = 1



while not game_over:#bucle para ejecutar los fotogramas para el repintado de la pantalla

    for eventos in pg.event.get():# captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:#controlar que pare el bucle
            game_over = True

    pantalla_principal.fill( (73, 162, 240) )#asigna un color a la pantalla
    #hay que poner lo que queramos antes del display.flip
    x += vx
    y += vy
    if x >= 800 or x == 0:#llegue a los limites
        vx = vx * -1 
    if y >= 600 or y == 0:
        vy = vy * -1




    ''' 
    if x != 780:
        x += 1
    if y != 580:
        y += 1
    '''



    #la surface o pantalla #color en rgb  #posicion(posicion(ancho y largo) y dimensiones(ancho y largo)
    pg.draw.rect(pantalla_principal,(250, 248, 55),(x,y,20,20))
  
    #metodo para definir un cuadrado

    pg.display.flip()#para activar el color que le hemos asignado con rgb

    contador += 1




pg.quit



     