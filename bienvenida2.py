import math

print("Bienvenid@ a IIC2233")
class Circulo:

    def __init__(self, radio, x, y):
        self.radio = radio
        self.x = x
        self.y = y

    def ObtenerPerimetro(self):
        perimetro = 2*self.radio* math.pi
        return perimetro

    def ObtenerArea(self):
        area = math.pi * (self.radio**2)
        return area

    def __str__(self):
        return "El area del circulo es " + str(self.ObtenerArea()) + " y su perimetro es "\
               + str(self.ObtenerPerimetro()) + " y su centro en el plano es (" + str(self.x) + "," + str(self.y) + ")"

class Rectangulo:

    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def ObtenerPerimetro(self):
        perimetro = 2 * self.lado1 + 2 * self.lado2
        return perimetro

    def ObtenerArea(self):
        area = self.lado1 * self.lado2
        return area

    def EsCuadrado(self):
        x = False
        if self.lado2 == self.lado1:
            x = True
        if x == True:
            return str("si")
        elif x == False:
            return str("no")

    def __str__(self):
        return "El perimetro de este rectangulo es "+ str(self.ObtenerPerimetro()) +\
               ", su area es " + str(self.ObtenerArea()) + " y el rectangulo " + self.EsCuadrado() + " es un cuadrado." +\
                " Ademas, sus vertices se ubican en los puntos "





x = Circulo(4,10,10)
print(x)

y = Rectangulo(3,3)
print(y)