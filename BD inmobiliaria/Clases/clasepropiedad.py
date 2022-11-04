import time
import sys
sys.path.append(r"..\\Inmobiliaria")
sys.path.append(r"..\\Inmobiliaria\\Clases")
from Conexion.conexionbd import conexion  # importar la clase conexion
from claseoperatoria import operatoria  # importar la clase operatoria
from claseestado import estado  # importar la clase estado
from clasetipo import tipo  # importamos la clase Tipo
from clasepropietario import propietario
from tabulate import tabulate
from os import system

class propiedad:   
    Ambientes = 0  # atributo de la clase Propiedad
    Direccion = " " # atributo de la clase Propiedad
    Localidad = ""  # ATRIBUTOS DE LA CLASE PROPIEDAD

    # Constructor de la clase Propiedad
    def __init__(self, ambientes=0, direccion='', localidad=""):
        self.Ambientes = ambientes
        self.Direccion = direccion
        self.Localidad = localidad

    def getAmbientes(self):  #los ambientes de la propiedad
        return self.Ambientes

    def getDireccion(self):  # la direccion de la propiedad
        return self.Direccion

    def getLocalidad(self):  # la localidad de la propiedad
        return self.Localidad

    def setAmbientes(self, ambientes):  #asignar los ambientes de la propiedad
        self.Ambientes = ambientes

    def setDireccion(self, direccion):  # asignar la direccion de la propiedad
        self.Direccion = direccion

    def setLocalidad(self, localidad):  #asignar la localidad de la propiedad
        self.Localidad = localidad

    def __str__(self):  # Este es un metodo para mostrar los datos de la propiedad
        return "Ambientes: " + str(self.Ambientes)+" Direccion: "+self.Direccion+" Localidad: "+str(self.Localidad)

    # Este es un metodo para pedir los datos de la propiedad
    def pedirDatosPropiedad(self, pro):
        try:
            pro.setDireccion(
                input("Ingrese la dirección de la propiedad: "))
            print()
            pro.setAmbientes(
                int(input("Ingrese la cantidad de ambientes de la propiedad: ")))
            print()
            pro.setLocalidad(
                input("Ingrese la localidad de la propiedad: "))
            print()
        except:
            print("Error al ingresar los datos de la propiedad")
    # ESte es un metodo interno para recuperar la lista de id de propiedades
    def RecuperarListaIdPropiedad(self):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad FROM Propiedad;")
                return cursor.fetchall()
            except Exception as e:
                print("Error al recuperar el lista id de propiedades: ", e)

    def ListarPropiedadID(self, id):  # Metodo para mostrar una propiedad por id dado
        cone = conexion()
        try:
            if cone.conectado():
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad, Ambientes, P.Direccion, Localidad, Nombre, Pro.Direccion, Contacto, Nombre_tipo, Nombre_Estado, Nombre_Operatoria_Comercial FROM Propiedad as P JOIN Propietario as Pro on P.Id_Propietario=Pro.Id_Propietario JOIN Tipo as T on P.Id_Tipo=T.Id_Tipo JOIN Estado as E on P.Id_Estado=E.Id_Estado JOIN OperatoriaComercial as O on P.Id_Operacion_Comercial=O.Id_Operatoria_Comercial WHERE Id_Propiedad='{}'".format(id))
                lista = cursor.fetchall()
                head = ['Id', 'Tipo', 'Estado', 'Operatoria', 'Ambientes', 'Direccion',
                        'Localidad', 'Dueño', 'Direccion', 'Contacto', ]
                tabla = []
                for x in lista:
                    tabla.append([x[0], x[7], x[8], x[9], x[1],
                                x[2], x[3], x[4], x[5], x[6]])
                print(tabulate(tabla, tablefmt="fancy_outline", headers=head))

        except Exception as e:
            print("Error al listar la propiedad: ", str(e))

    # Este es un metodo interno para recuperar el id del propietario
    def __RecuperarIdPropietario(self, id):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute(
                    "SELECT Id_Propietario FROM Propiedad WHERE Id_Propiedad = {}".format(id))
                return cursor.fetchall()
            except Exception as e:
                print("Error al recuperar el id del propietario: ", e)
    # Este es un metodo para insertar una propiedad en la base de datos (opcion 2 del menu)
    def insertarPropiedad(self):

        propie = propietario() 
        pro = propiedad()  
        cone = conexion()  
        tip = tipo()  
        est = estado()  
        ope = operatoria()  
        print("***** ESPACIO DE CARGA DE DATOS DE NUEVA PROPIEDAD *****")
        print()

        if cone.conectado():
            try:
                # funcion interna insertar por el usuario el propietario
                propie.insertarPropietario(propie)
                # # funcion interna recuperar id propietario
                recupIDpropie = propie.RecuperarUltimoIdPropietario()
                system("cls")
                time.sleep(0.5)
                # funcion interna para insertar por el usuario los campos No id de propiedad
                pro.pedirDatosPropiedad(pro)
                system("cls")
                time.sleep(0.5)
                # funcion interna para pedir al usuario el tipo de propiedad
                IDtipo = tip.definirTipo()
                print()
                system("cls")
                time.sleep(0.5)
                # funcion interna para pedir al usuario el estado de la propiedad
                IDestado = est.definirEstado()
                system("cls")
                time.sleep(0.5)
                print()
                IDopera = ope.definirOperatoria()
                system("cls")
                time.sleep(0.5)

                sql = "INSERT INTO Propiedad (Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario,Ambientes, Direccion, Localidad)  VALUES ('{}', '{}', '{}','{}','{}','{}','{}')".format(
                    IDtipo, IDestado, IDopera, recupIDpropie, pro.getAmbientes(), pro.getDireccion(), pro.getLocalidad())
                cursor = cone.conexion.cursor()
                cursor.execute(sql)
                cone.conexion.commit()
                print(cursor.rowcount, "PROPIEDAD INGRESADA CON EXITO.")
            except Exception as e:
                print("Error al cargar la propiedad: ", str(e))

    # Este es un metodo para modificar una propiedad en la base de datos (opcion 3 del menu)
    def modificarPropiedad(self):
        cone = conexion()
        prop = propiedad()  # instanciamos un objeto de la clase conexion
        tip = tipo()  # instanciamos un objeto de la clase tipo
        est = estado()  # instanciamos un objeto de la clase estado
        propie = propietario()  # instanciamos un objeto de la clase propietario
        ope = operatoria()  # instanciamos un objeto de la clase operatoria
        if cone.conectado():
            try:
                print("***** ESPACIO DE MODIFICACION DE DATOS DE PROPIEDAD *****")
                print()

                prop.ListarPropiedades()  # llamamos al metodo para listar las propiedades
                print()
                salir = False
                while not salir:
                    id = int(input('Ingrese el ID de la propiedad a modificar: '))
                    # obtenemos los id de la tabla propiedad
                    ListaId = prop.RecuperarListaIdPropiedad()
                    MiListaId = []  # creamos una lista vacia para guardar los id de la tabla propiedad como enteros
                    for x in ListaId:
                        MiListaId.append(int(x[0]))
                    if id in MiListaId:
                        salir = True
                        system("cls")
                        time.sleep(0.5)
                        print('La propiedad a modificar es:')
                        prop.ListarPropiedadID(id)
                        print("Ingrese los datos NUEVOS de la propiedad")
                        print()

                        # pedimos los nuevos datos de la propiedad
                        prop.pedirDatosPropiedad(prop)
                        time.sleep(0.5)

                        # funcion interna para pedir al usuario el tipo de propiedad
                        IDtipo = tip.definirTipo()
                        print()
                        time.sleep(0.5)

                        # funcion interna para pedir al usuario el estado de la propiedad
                        IDestado = est.definirEstado()
                        time.sleep(0.5)
                        print()
                        IDopera = ope.definirOperatoria()
                        time.sleep(0.5)
                        ListidPropie = prop.__RecuperarIdPropietario(id)
                        idPropie = ListidPropie[0][0]
                        modi = input(
                            "¿ Desea modificar el propietario? (s/n): ")
                        if modi == "s" or modi == "S":
                            system("cls")
                            print("El propietario a modificar es: ")
                            propie.MostrarPropietario(idPropie)
                            propie.modificarPropietario(idPropie)

                        sql = "UPDATE Propiedad SET Id_Tipo='{}', Id_Estado='{}', Id_Operacion_Comercial='{}',Id_Propietario='{}', Ambientes='{}', Direccion='{}', Localidad='{}' WHERE Id_Propiedad='{}'".format(
                            IDtipo, IDestado, IDopera, idPropie, prop.getAmbientes(), prop.getDireccion(), prop.getLocalidad(), id)
                        cursor = cone.conexion.cursor()
                        cursor.execute(sql)
                        cone.conexion.commit()
                        print()
                        print("HA MODIFICADO LA PROPIEDAD CON EXITO!")

                    else:
                        print("El ID ingresado no existe.")
                        print('Estas son las opciones que tiene disponibles: ', end=' ')
                        for i in MiListaId:
                            print(i, end=' ')
                        print()
            except Exception as e:
                print("Error para modificar la propiedad: ", str(e))

    # Este es un metodo para eliminar una propiedad(opcion 4 del menu)
    def eliminarPropiedad(self):
        cone = conexion()
        prop = propiedad()
        if cone.conectado:
            try:
                print("*****ESPACIO PARA ELIMINAR UNA PROPIEDAD*****")
                print()
                prop.ListarPropiedades() # llamamos al metodo para listar las propiedades
                print()
                salir = False
                while not salir:
                    cursor = cone.conexion.cursor()
                    cursor.execute("SELECT Id_Propiedad FROM Propiedad")
                    lista = cursor.fetchall()
                    MiListaId = []
                    for x in lista:
                        MiListaId.append(x[0])
                    MiListaId.sort()
                    id = int(
                        input("Ingrese el ID de la propiedad que desea eliminar: "))
                    if id in MiListaId:
                        sql = "DELETE FROM Propiedad WHERE Id_Propiedad='{}'".format(
                            id)
                        cursor = cone.conexion.cursor()
                        cursor.execute(sql)
                        cone.conexion.commit()
                        print()
                        print("PROPIEDAD ELIMINADA CON EXITO")
                        salir = True
                    else:
                        print("El ID ingresado no existe!")
                        print('Estas son las opciones que tiene disponibles: ', end=' ')
                        for i in MiListaId:
                            print(i, end=' ')
                        print()
            except Exception as e:
                print("Error para eliminar la propiedad")

    # Este es un metodo para listar las propiedades(opcion 5 del menu)
    def ListarPropiedades(self):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad, Ambientes, P.Direccion, Localidad, Nombre, Pro.Direccion, Contacto, Nombre_tipo, Nombre_Estado, Nombre_Operatoria_Comercial FROM Propiedad as P JOIN Propietario as Pro on P.Id_Propietario=Pro.Id_Propietario JOIN Tipo as T on P.Id_Tipo=T.Id_Tipo JOIN Estado as E on P.Id_Estado=E.Id_Estado JOIN OperatoriaComercial as O on P.Id_Operacion_Comercial=O.Id_Operatoria_Comercial")
                lista = cursor.fetchall()
                head = ['Id', 'Tipo', 'Estado', 'Operatoria', 'Ambientes', 'Direccion',
                        'Localidad', 'Dueño', 'Direccion', 'Contacto', ]
                tabla = []
                for x in lista:
                    tabla.append([x[0], x[7], x[8], x[9], x[1],
                                x[2], x[3], x[4], x[5], x[6]])
                tabla.sort()
                print(tabulate(tabla, tablefmt="fancy_outline", headers=head))
            except Exception as e:
                print("Error al listar las propiedades: ", str(e))

    # Este es un metodo para listar las prop disponibles para venta(opcion 6 del menu)

    def ListarPropiedadesDispVenta(self):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad, Ambientes, P.Direccion, Localidad, Nombre, Pro.Direccion, Contacto, Nombre_tipo, Nombre_Estado, Nombre_Operatoria_Comercial FROM Propiedad as P JOIN Propietario as Pro on P.Id_Propietario=Pro.Id_Propietario JOIN Tipo as T on P.Id_Tipo=T.Id_Tipo JOIN Estado as E on P.Id_Estado=E.Id_Estado JOIN OperatoriaComercial as O on P.Id_Operacion_Comercial=O.Id_Operatoria_Comercial WHERE P.Id_Estado= 1 AND P.Id_Operacion_Comercial= 2 ")
                lista = cursor.fetchall()
                head = ['Id', 'Tipo', 'Estado', 'Operatoria', 'Ambientes', 'Direccion',
                        'Localidad', 'Dueño', 'Direccion', 'Contacto', ]
                tabla = []
                for x in lista:
                    tabla.append([x[0], x[7], x[8], x[9], x[1],
                                x[2], x[3], x[4], x[5], x[6]])
                print(tabulate(tabla, tablefmt="fancy_outline", headers=head))
            except Exception as e:
                print(
                    "Error al listar las propiedades disponibles que estan para la venta: ", str(e))

    # Este es un metodo para listar las prop disponibles para alquiler(opcion 7 del menu)
    def ListarPropiedadesDispAlquiler(self):
        cone = conexion()
        if cone.conectado():
            try:

                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad, Ambientes, P.Direccion, Localidad, Nombre, Pro.Direccion, Contacto, Nombre_tipo, Nombre_Estado, Nombre_Operatoria_Comercial FROM Propiedad as P JOIN Propietario as Pro on P.Id_Propietario=Pro.Id_Propietario JOIN Tipo as T on P.Id_Tipo=T.Id_Tipo JOIN Estado as E on P.Id_Estado=E.Id_Estado JOIN OperatoriaComercial as O on P.Id_Operacion_Comercial=O.Id_Operatoria_Comercial WHERE P.Id_Estado= 1 AND P.Id_Operacion_Comercial= 1 ")
                lista = cursor.fetchall()
                head = ['Id', 'Tipo', 'Estado', 'Operatoria', 'Ambientes', 'Direccion',
                        'Localidad', 'Dueño', 'Direccion', 'Contacto', ]
                tabla = []
                for x in lista:
                    tabla.append([x[0], x[7], x[8], x[9], x[1],
                                x[2], x[3], x[4], x[5], x[6]])

                print(tabulate(tabla, tablefmt="fancy_outline", headers=head))

            except Exception as e:
                print(
                    "Error al listar las propiedades disponibles que estan para alquiler: ", str(e))

    # Este es un metodo para listar las propiedades vendidas(opcion 8 del menu)
    def ListarPropiedadesVendidas(self):
        cone = conexion()
        if cone.conectado():
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad, Ambientes, P.Direccion, Localidad, Nombre, Pro.Direccion, Contacto, Nombre_tipo, Nombre_Estado, Nombre_Operatoria_Comercial FROM Propiedad as P JOIN Propietario as Pro on P.Id_Propietario=Pro.Id_Propietario JOIN Tipo as T on P.Id_Tipo=T.Id_Tipo JOIN Estado as E on P.Id_Estado=E.Id_Estado JOIN OperatoriaComercial as O on P.Id_Operacion_Comercial=O.Id_Operatoria_Comercial WHERE P.Id_Estado= 3 ")
                lista = cursor.fetchall()
                head = ['Id', 'Tipo', 'Estado', 'Operatoria', 'Ambientes', 'Direccion',
                        'Localidad', 'Dueño', 'Direccion', 'Contacto', ]
                tabla = []
                for x in lista:
                    tabla.append([x[0], x[7], x[8], x[9], x[1],
                                x[2], x[3], x[4], x[5], x[6]])

                print(tabulate(tabla, tablefmt="fancy_outline", headers=head))

            except Exception as e:
                print("Error al listar las propiedades que estan vendidas: ", str(e))

        # Este es un metodo para listar las propiedades vendidas(opcion 9 del menu)
    def ListarPropiedadesAlquiladas(self):
        cone = conexion()
        if cone.conectado():
            try:

                cursor = cone.conexion.cursor()
                cursor.execute("SELECT Id_Propiedad, Ambientes, P.Direccion, Localidad, Nombre, Pro.Direccion, Contacto, Nombre_tipo, Nombre_Estado, Nombre_Operatoria_Comercial FROM Propiedad as P JOIN Propietario as Pro on P.Id_Propietario=Pro.Id_Propietario JOIN Tipo as T on P.Id_Tipo=T.Id_Tipo JOIN Estado as E on P.Id_Estado=E.Id_Estado JOIN OperatoriaComercial as O on P.Id_Operacion_Comercial=O.Id_Operatoria_Comercial WHERE P.Id_Estado= 2 ")
                lista = cursor.fetchall()
                head = ['Id', 'Tipo', 'Estado', 'Operatoria', 'Ambientes', 'Direccion',
                        'Localidad', 'Dueño', 'Direccion', 'Contacto', ]
                tabla = []
                for x in lista:
                    tabla.append([x[0], x[7], x[8], x[9], x[1],
                                x[2], x[3], x[4], x[5], x[6]])

                print(tabulate(tabla, tablefmt="fancy_outline", headers=head))

            except Exception as e:
                print("Error al listar las propiedades que estan alquiladas: ", str(e))


if __name__ == '__main__':
    print("Soy la Clase Propiedad")
