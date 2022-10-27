from sqlite3 import Cursor
import mysql.connector

class conexionBD ():

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
                print("¡Conexión Exitosa!")
        except mysql.connector.Error as DescripcionError:
            print ("¡Conexión Fallida!", DescripcionError)
        finally:
            if self.conexion.is_connected():
               self.conexion.close()
               print ("Conexión Cerrada")
               
conexion = conexionBD ()

print (conexion)