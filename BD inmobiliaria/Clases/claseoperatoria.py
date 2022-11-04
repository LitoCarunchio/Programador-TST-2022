
from os import system
class operatoria:
    NombreOp = ""

    def __init__(self, nombre=''):
        self.NombreOp = nombre

    def getNombreOp(self):
        return self.NombreOp

    def setNombreOp(self, nombre):
        self.NombreOp = nombre

    def __str__(self):
        return str(self.NombreOp)
    
    def definirOperatoria(self):  # Esta funcion es para definir id de operatoria de propiedad
        correcto = False
        while not correcto:
            try:
                print("""Indique la operatoria de la propiedad de la siguiente lista:
                        1. Alquiler
                        2. Venta
                        3. Sin Definir
                        """)
                op = int(input("Ingrese una opcion numerica: "))
                if op in range(1, 4):
                    correcto = True
                    return op
                else:
                    print()
                    print("Error al ingresar la opción operatoria")
                    continua = input(' Presione una tecla para continuar...')
                    system("cls")

            except Exception as e:
                print()
                print("Error al ingresar la opcion", e)
                continua = input(' Presione una tecla para continuar...')
                system("cls")


        
if __name__ == '__main__':
    print("Soy la Clase Operatoria")
