from os import system
import sys
sys.path.append(r"..\\Inmobiliaria")
from Clases.clasepropiedad import propiedad  # Esto es para importar la clase propiedad
from Conexion.conexionbd import conexion  # Esto es para importar la clase conexion
import time
conex = conexion()  # Sirve para crear un objeto de la clase conexion
prop = propiedad()  # Sirve para crear un objeto de la clase propiedad
salir = False # Esto es una variable para salir del programa
Encabezado = "Fecha  " + \
    time.strftime(
        "%x") + "                                          Hora  " + time.strftime("%X")
menu = ("""\

Base de Datos Inmobiliaria            


1. Conectarse a la Base de Datos                                  
2. Ingresar una nueva propiedad                                   
3. Modificar datos de propiedad existente                                  
4. Eliminar datos de propiedad existente                                   
5. Listar todas las propiedades de la Base de Datos                                  
6. Listar propiedades disponibles para la venta                   
7. Listar propiedades disponibles para alquiler                   
8. Listar propiedades vendidas                                    
9. Listar propiedades alquiladas                                                                                                    
0. Salir\
""")
while not salir:
    print(Encabezado)
    print(menu)
    try:
        opcion = int(input("Ingrese un número para operar: "))
        print()     
        system("cls")
        if opcion == 1:
            print('Conectando a la Base de Datos...')
            time.sleep(1)
            print()
            conex.conectar()
        elif not conex.conectado():
            print("Debe conectarse a la Base de Datos en la Opción Nº 1")
        else:
            if opcion == 2:                
                time.sleep(0.5)
                prop.insertarPropiedad()
            elif opcion == 3:                 
                print('Para poder modificar una propiedad, listaremos todas las propiedades disponibles')
                print()
                continua = input('    PRESIONE UNA TECLA PARA CONTINUAR...')
                prop.modificarPropiedad()                
            elif opcion == 4:                 
                print('Para poder eliminar una propiedad, listaremos todas las propiedades disponibles')
                print()
                continua = input('    PRESIONE UNA TECLA PARA CONTINUAR...')
                prop.eliminarPropiedad()
            elif opcion == 5:                 
                print('Listaremos todas las propiedades disponibles...')
                print()
                continua = input('    PRESIONE UNA TECLA PARA CONTINUAR...')
                prop.ListarPropiedades()
            elif opcion == 6:                 
                print('listaremos todas las propiedades disponibles para la venta')
                continua=input('    PRESIONE UNA TECLA PARA CONTINUAR...')
                print()
                prop.ListarPropiedadesDispVenta()
            elif opcion == 7:                 
                print('Listaremos todas las propiedades disponibles para alquilar')
                continua = input('    PRESIONE UNA TECLA PARA CONTINUAR...')
                print()
                prop.ListarPropiedadesDispAlquiler()
            elif opcion == 8:                 
                print('Listaremos todas las propiedades que fueron vendidas')
                continua = input('    PRESIONE UNA TECLA  PARA CONTINUAR...')
                print()
                prop.ListarPropiedadesVendidas()
            elif opcion == 9:                 
                print('Listaremos todas las propiedades que están alquiladas')
                continua = input('    PRESIONE UNA TECLA PARA CONTINUAR...')
                print()
                prop.ListarPropiedadesAlquiladas()
            elif opcion == 0:
                print('Exit...')
                time.sleep(1)
                conex.desconectar()
                salir = True
                time.sleep(2)
            else:
                print('El número ingresado es incorrecto')
        print()
        continua = input('    PRESIONE UNA TECLA PARA CONTINUAR...')
        system("cls")
    except Exception as e:
        print()
        print("    ¡¡ Opción inválida !! ", e)
        continua = input(' PRESIONE UNA TECLA PARA CONTINUAR...')
        time.sleep(1)
        system("cls")
