import oracledb #No olvidar instalar con "pip install oracledb"
import getpass


#CREDENCIALES
user = 'system' #Aqui cambiar por el usuario que tengan ustedes
pswd = 'inacap'
#pswd = getpass.getpass("Ingrese contraseña: ")
dsn = 'localhost/xe'


#Para hacer una consulta se requiere una query y un tipo de query. Este tipo de query puede ser 'select','insert','update','delete'
def hacer_consulta(query, tipo_query, variables=None):
    try:
        #Crear conexion
        connection = oracledb.connect(user=user, password=pswd, dsn=dsn)
        
        # Crear cursor
        cursor = connection.cursor()
        
        try:
            if tipo_query == 'select':
                cursor.execute(query)
                return cursor.fetchall()
            else:
                cursor.execute(query,variables)
                connection.commit()
        
        except Exception as e:
            print(f"Error al ejecutar query: {e}")
            connection.rollback()
        
        finally:
            # Cerrar cursor y conexion
            cursor.close()
            connection.close()
    
    except Exception as e:
        print(f"Hubo un error al intentar conectar a la base de datos: {e}")