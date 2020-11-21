
class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Forma(Punto):
    def __init__(self,x, y, color, nombre):
        super().__init__(x, y)
        self.color=color
        self.nombre=nombre
    def print(self):
        print("Coordenadas x " + str(self.x) + " Coordenadas y " + str(self.y) + " Color -> " + self.color +" Nombre -> "+self.nombre)
    def obtener(self):
        return self.nombre,self.punto.x, self.punto.y
    def cambiarForma(self,x,y):
        self.x=x
        self.y=y

Forma1 = Forma( 4, 8,"Rojo","Triangulo")
Forma1.print()


class Rectangulo(Forma):
    def __init__(self, x, y, color, nombre, ladoMenor, ladoMayor):
        super().__init__(x, y, color,nombre)
        self.ladoMenor=ladoMenor
        self.ladoMayor=ladoMayor
    def Area(self):
        area=self.ladoMenor*self.ladoMayor
        print("El area es igual a: "+str(area))
    def perimetro(self):
        perimetro=2*self.ladoMenor+2*self.ladoMayor
        print("Perimetro: "+str(perimetro))

Rectangulo1=Rectangulo(2, 8, "Verde", "Rectangulo", 6, 5)
Rectangulo1.print()

class Elipse(Forma):
    def __init__(self, x, y, color, nombre, RMayor, RMenor):
        super().__init__(x,y,color,nombre)
        self.RMayor=RMayor
        self.RMenor=RMenor
    def areaElipse(self):
        area=math.pi*(self.RMayor*self.RMenor)
        print("Area de Elipse: "+str(area))

Elipse1=Elipse(3,7,"Amarillo","Elipse", 7,4)
Elipse1.print()


class Cuadrado(Rectangulo):
    def __init__(self,x,y,color,nombre,ladoMenor, ladoMayor):
        super().__init__(x,y, color, nombre, ladoMenor, ladoMayor)
    def print(self):
        super().print()

class Circulo(Elipse):
    def __init__(self, x, y, color, nombre, RMayor, RMenor):
        super().__init__(x,y, color,nombre,RMayor, RMenor)
    def print(self):
        super().print()

Rectangulo1=Rectangulo(9, 1, "Naranja", "Rectangulo", 1, 5)
Elipse1=Elipse(2,9,"Negro","Elipse", 7,8)
Cuadrado1=Cuadrado(0,7,"Morado","Cuadrado",5,2)
Circulo1=Circulo(2,3,"Rosa","Circulo",1,0)

tupla=(Rectangulo1,Elipse1,Cuadrado1,Circulo1)
for Forma in tupla:
    print(Forma.print())