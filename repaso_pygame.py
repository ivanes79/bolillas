import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Bolillas Robando")

x=390
y=290
vx=1
vy=1

x2=300
y2=400
vx2=1
vy2=1



game_over=False
contador = 0
while not game_over:
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = True
    contador+=1
    print("fotograma :",contador) 

    pantalla_principal.fill((52,152,219))

    x += vx
    y += vy

    x2 += vx2
    y2 += vy2

    if x >= 800 or x <=0:#limite en x
        vx *= -1
    if y >= 600 or y <=0:#limite en y
        vy *= -1 

    if x2 >= 800 or x2 <=0:#limite en x
        vx2 *= -1
    if y2 >= 600 or y2 <=0:#limite en y
        vy2 *= -1    

    pg.draw.rect(pantalla_principal,(255,255,255),(x,y,20,20) )

    pg.draw.rect(pantalla_principal,(0,255,0),(x2,y2,20,20) )

    pg.display.flip()

pg.quit()

