from os import system
class estado:
    Nombre = ""

    def __init__(self, nombre=''):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def __str__(self):
        return str(self.Nombre)

    def definirEstado(self):  # funcion para definir id de estado de propiedad
        correcto = False
        while not correcto:
            try:
                print("""Indique el estado de la propiedad de la siguiente lista:
                    1. Disponible
                    2. Alquilada
                    3. Vendida
                    4. Sin definir """)

                op = int(input("Ingrese una opcion numérica: "))
                if op in range(1, 5):
                    correcto = True
                    return op
                else:
                    print()
                    print("Error al ingresar la opción estado")
                    continua = input(' Presione una tecla para continuar...')
                    system("cls")

            except Exception as e:
                print()
                print("Error al ingresar la opción", e)
                continua = input(' Presione una tecla para continuar...')
                system("cls")
if __name__ == '__main__':
    print("Soy la Clase Estado")
