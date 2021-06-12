import psycopg2
from datetime import datetime

class DBOferta:
    def __init__(self):
        pass

class DBOfertadetalle:
    def __init__(self):
        pass

    def select_ofertadetalle_dimension(self,connection,dimension):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = """SELECT id_ofertadetalle,ofertaperfil_id,descripcion,count(*) 
                     FROM oferta_detalle 
                     WHERE ofertaperfil_id=3
                     GROUP BY id_ofertadetalle,ofertaperfil_id,descripcion 
                     ORDER BY 1,2,3 ASC
                     """
            #params f (requisito["descripcion_normalizada"], requisito["iddescripcion"])
            mycursor.execute(sql)

            array_de_tuplas = []
            row = mycursor.fetchone()
            while row is not None:
                array_de_tuplas.append(row)
                row = mycursor.fetchone()

            # close the communication with the PostgreSQL
            mycursor.close()
            mydb.close() 

        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE UPDATE OFERTA_DETALLE ERROR")
            mydb.close()

        return array_de_tuplas

    def update_ofertadetalle_normalized(self,connection,requisito,equipo):
        mydb = connection.connect()
        fecha_modificacion = datetime.today().strftime('%Y-%m-%d')
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE OFERTA_DETALLE SET descripcion_normalizada=%s,f_equipo=%s,equipo=%s where id_ofertadetalle=%s"
            #params = (requisito["descripcion_normalizada"], requisito["iddescripcion"])
            params = (requisito[2],fecha_modificacion,equipo,requisito[0])
            mycursor.execute(sql, params)
            mydb.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE UPDATE OFERTA_DETALLE ERROR")
            mydb.close()


    def select_ofertadetalle(self,connection):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = "SELECT * FROM OFERTA_DETALLE LIMIT 1"
            #params = (requisito["descripcion_normalizada"], requisito["iddescripcion"])
            mycursor.execute(sql)

            array_de_tuplas = []
            row = mycursor.fetchone()
            while row is not None:
                array_de_tuplas.append(row)
                row = mycursor.fetchone()

            # close the communication with the PostgreSQL
            mycursor.close()
            mydb.close() 

        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE UPDATE OFERTA_DETALLE ERROR")
            mydb.close()

        return array_de_tuplas

    def update_ofertadetalle(self, connection, requisito):
        mydb = connection.connect()
        fecha_modificacion = datetime.today().strftime('%Y-%m-%d')
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE OFERTA_DETALLE SET descripcion_normalizada=:1,fecha_equipo=:2 where id_ofertadetalle=:3"
            params = (requisito["descripcion_normalizada"],fecha_modificacion, requisito["iddescripcion"])

            mycursor.execute(sql, params)
            mydb.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE UPDATE OFERTA_DETALLE ERROR")
            mydb.close()

    def insertOfertaDetalle(self, connection, listaDetalle):
        mydb = connection.connect()
        try:
            #mydb= connection.connect()
            mycursor= mydb.cursor()

            for detalle in listaDetalle:
                sql= "insert into oferta_detalle ( id_ofertadetalle, id_oferta, descripcion, fecha_creacion, fecha_modificacion) values (DEFAULT,%s,%s,current_date,current_date)"
                params= (detalle["id_oferta"],detalle["descripcion"].strip())
                mycursor.execute(sql, params)
                mydb.commit()

            # close the communication with the PostgreSQL
            mycursor.close()
            mydb.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE INSERTAR OFERTA_DETALLE ERROR")
            mydb.close()
        
        return 1

    def update_prueba(self,connection,requisito):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE alumno SET nombre=%s where id=%s"
            #params = (requisito["nombre"], requisito["id"])
            params = (requisito[1], requisito[0])

            mycursor.execute(sql, params)
            mydb.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE UPDATE OFERTA_DETALLE ERROR")
            mydb.close()

    def select_prueba(self,connection):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = "SELECT * FROM alumno"
            #params = (requisito["descripcion_normalizada"], requisito["iddescripcion"])
            mycursor.execute(sql)

            array_de_tuplas = []
            row = mycursor.fetchone()
            while row is not None:
                array_de_tuplas.append(row)
                row = mycursor.fetchone()

            # close the communication with the PostgreSQL
            mycursor.close()
            mydb.close() 

        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            print("OFERTA DETALLE UPDATE OFERTA_DETALLE ERROR")
            mydb.close()

        return array_de_tuplas
        
class DatesDB:
    def __init__(self):
        pass



