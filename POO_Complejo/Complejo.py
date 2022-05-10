#Practica 1 POO python
#Numeros Complejos
#SSPEDII Seccion: D11
#Corona Yanez Mariana Elizabeth


class Ncomplex :
    #atributos de la clase
    Preal = 0
    Pima = 0

    #constructor
    def __init__(self,real,ima):
        self.Preal = real
        self.Pima = ima

    #metodos de la clase
    #Setters
    def CambioReal (self,real):
        self.Preal = real
    def CambioIma(self,ima):
        self.Pima = ima

    #getter
    def RegresaReal (self):
        return self.Preal
    def RegresaIma (self):
        return self.Pima

    # Suma de complejos
    def __add__(self, n):
        return Ncomplex(self.Preal + n.Preal, self.Pima + n.Pima)

    #Resta de complejos
    def __sub__(self, n):
        return Ncomplex(self.Preal - n.Preal, self.Pima - n.Pima)

    #Multiplicacion de complejos
    def __mul__(self, n):
        real = (self.Preal * n.Preal) - (self.Pima * n.Pima)
        ima = (self.Preal * n.Pima) + (self.Pima * n.Preal)
        return Ncomplex(real,ima)

    #Imprimir complejo
    def Imprimir (self):
        if self.Pima < 0 :
            print(self.Preal," ",self.Pima,"i")
        else:
            print(self.Preal," +",self.Pima,"i")


numero1 = Ncomplex(3,7)
numero2 = Ncomplex(10,-6)

num3 = (numero1 + numero2)
num4 = (numero1 - numero2)
num5 = (numero1 * numero2)

print("Complejo 1")
numero1.Imprimir()
print("\nComplejo 2")
numero2.Imprimir()

print("\nSuma: ")
num3.Imprimir()
print("\nResta: ")
num4.Imprimir()
print("\nMultiplicacion: ")
num5.Imprimir()

print("\nCambios")
numero1.CambioReal(5)
numero2.CambioIma(8)

numero1.Imprimir()
numero2.Imprimir()

a = numero1.RegresaReal()
print(a)

