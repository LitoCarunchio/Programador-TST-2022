
from os import system

class tipo:
    Nombre = ""

    def __init__(self, nombre=''):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def __str__(self):
        return str(self.Nombre)

    def definirTipo(self):  # Funcion interna para definir el tipo de la propiedad
        correcto = False
        while not correcto:
            try:
                print("""Indique el tipo de propiedad de la siguiente lista:
                    1. Casa residencial
                    2. Casa en Country
                    3. Departamento
                    4. Terreno
                    5. Comercial
                    6. Quinta/Chacra/Campo
                    """)
                op = int(input("Ingrese una opción numérica: "))
                if op in range(1, 7):
                    correcto = True
                    return op
                else:
                    print()
                    print("Error al ingresar la opción tipo")
                    continua = input(' Presione una tecla para continuar...')
                    system("cls")

            except Exception as e:
                print()
                print("Error al ingresar la opción", e)
                continua = input(' Presione una tecla para continuar...')
                system("cls")
   
if __name__ == "__main__":
    print("Modulo de la clase tipo")
