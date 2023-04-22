#Definiton of the class
class operaciones:
  #Initialization of the class
    def __init__(self,numero,numero2):
        self.numero=numero
        self.numero2=numero2
    def suma(self):
        return "El resultado de la suma es {}".format(self.numero+self.numero2)
    def resta(self):
        return "El resultado de la resta es {}".format(self.numero-self.numero2)
    def multiplicacion(self):
        return "El resultado de la multiplicacion es {}".format(self.numero*self.numero2)
    def division(self):
        return "El resultado de la division es {}".format(self.numero/self.numero2)
op=operaciones(10,20)
#Suma/Addition
print(op.suma())
#Resta/subtraction
print(op.resta())
#Multiplicacion/Multiplication
print(op.multiplicacion())
#Division/Division
print(op.division())
