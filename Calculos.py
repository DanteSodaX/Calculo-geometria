class Calculos:
    def __init__(self,a,b,c):
        self.a= a
        self.b= b
        self.c= c
    def menu(self):
        print("-------------------")  
        print("¡¡¡¡Bienvenido!!!!!")
        print("-------------------")  
        print("¿Que deseas hacer?")   
        print("1.-Calcular area de un triangulo")
        print("2.-Calcular area de un rectangulo")
        print("3.-Calcular el perimetro de una circuferencia")
        print("4.-Salir")
        
        d=int(input())
        if d==1:
            base = self.a
            altura = self.b
            self.area_de_triangulo(base,altura)

        elif d==2:
            base = self.a
            altura = self.b
            self.area_rectangulo(base,altura)
        elif d==3:
            radio = self.c
            self.perimetros_circuferencia(radio)
        elif d==4:
            pass    
        else:
            print("Incorrecto")
            self.menu()    
    def area_de_triangulo(self,a,b): 
        total1 = self.a*self.b
        total2 = total1/2
        return print(total2) 
    def area_rectangulo(self,a,b):
        total = self.a*self.b
        return print(total)
        
    def perimetros_circuferencia(self,c):
        total = self.a*3.14*2
        return print(total)
        
base = int(input("Introdusca un numero que usara como base: "))
altura = int(input("Introdusca un numero que usara como altura: "))
radio = int(input("Introdusca un numero que usara como radio: "))
calc = Calculos(base,altura,radio)
while True:
    calc.menu()
           
    






