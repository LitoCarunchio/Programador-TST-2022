from sqlite3 import Cursor
import mysql.connector

class Consultas ():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect (
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'root',
            db  = 'Inmobiliaria'
            )
            if self.conexion.is_connected ():
                print("¡¡Conexión Exitosa!!")
        except mysql.connector.Error as DescripcionError:
            print ("¡¡Conexión Fallida!!", DescripcionError)
            


    def ListadoVendidas (self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select Propiedad.Nombre, Propiedad.Direccion, Propiedad.Contacto, OperatoriaComercial.Nombre_Operatoria_Comercial, Estado.Nombre_Estado from Propiedad, OperatoriaComercial, Estado Where Nombre_Operatoria_Comercial = 'Venta' and Nombre_Estado = 'No Disponible'; ")
                ResVendidas = cursor.fetchall()
                self.conexion.close()
                return ResVendidas

            except mysql.connector.Error as DescripcionError:
                print ("¡Conexión Fallida!", DescripcionError)


    def ListadoAlquiladas (self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select Propiedad.Nombre, Propiedad.Direccion, Propiedad.Contacto, OperatoriaComercial.Nombre_Operatoria_Comercial, Estado.Nombre_Estado from Propiedad, OperatoriaComercial, Estado Where Nombre_Operatoria_Comercial = 'Alquilar' and Nombre_Estado = 'No Disponible';")
                ResAlquiladas = cursor.fetchall()
                self.conexion.close()
                return ResAlquiladas

            except mysql.connector.Error as DescripcionError:
                print ("¡Conexión Fallida!", DescripcionError)
   




