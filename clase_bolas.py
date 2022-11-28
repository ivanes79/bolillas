'''
class BolasLocas():
    def __init__(self,x,y,ancho,largo):
        self.x = int(x)
        self.y = int(y)
        self.ancho = ancho
        self.largo = largo
       
   
    def movimiento(self):
        self.vx = 1
        self.vy = 1
        self.x += vx
        self.y += vy
        if self.x >= 800 or self.x == 0:
            vx = vx * -1 
        if self.y >= 600 or self.y == 0:
            vy = vy * -1
        
        #return mov
    
       
bola1 = BolasLocas(300,400,20,20)
bola2 = BolasLocas(200,300,20,20)
bola3 = BolasLocas(150,400,20,20)
bola4 = BolasLocas(50,200,20,20)
bola5 = BolasLocas(250,50,20,20)
bola6 = BolasLocas(300,100,20,20)  

print(bola5.x)
print(bola6.y)
print(bola3.ancho)
print(bola2.largo)   
''' 