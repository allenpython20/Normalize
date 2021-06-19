import psycopg2
from datetime import datetime

class DBOferta:
    def __init__(self):
        pass

class DBOfertadetalle:
    def __init__(self):
        pass

    def filtrar(self,connection,word):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = """select od.id_ofertadetalle,trim(od.descripcion_normalizada) as descripcion
                    from webscraping w inner join oferta o
                    on (w.id_webscraping=o.id_webscraping)
                    inner join oferta_detalle od
                    on (o.id_oferta=od.id_oferta)
                    left outer join ofertaperfil_tipo opt
                    on (od.ofertaperfil_id=opt.ofertaperfil_id)
                    where  length(trim(od.descripcion_normalizada))<=120
                    and o.id_estado is null and opt.ofertaperfil_id is null and ind_activo is null
                    and ( position(%s in trim(descripcion_normalizada))>0
                    --or position('VISITA DE INMUEBLES.' in trim(descripcion_normalizada))>0
                    )
                    order by 2;
                    """
            params = (word)
            mycursor.execute(sql,params)
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
        
    def select_ofertadetalle_dimension(self,connection,dimension):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = """SELECT id_ofertadetalle,ofertaperfil_id,descripcion,count(*) 
                     FROM oferta_detalle 
                     WHERE ofertaperfil_id=3
                     GROUP BY id_ofertadetalle,ofertaperfil_id,descripcion 
                     ORDER BY 1,2,3 ASC
                     LIMIT 100
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

    def select_ofertadetalle_dimension2(self,connection,dimension):
        mydb = connection.connect()
        try:
            mycursor = mydb.cursor()
            sql = """SELECT id_ofertadetalle,descripcion
                     FROM oferta_detalle 
                     WHERE ofertaperfil_id=3 
                     GROUP BY id_ofertadetalle,descripcion 
                     ORDER BY 1,2 ASC
                     LIMIT 5000
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

    def update_ofertadetalle_normalized2(self,connection,requisito,equipo):
        mydb = connection.connect()
        fecha_modificacion = datetime.today().strftime('%Y-%m-%d')
        try:
            mycursor = mydb.cursor()
            sql = "CREATE TEMP TABLE temp_od(DKEY INTEGER, DVALUE TEXT)"
            mycursor.execute(sql)
            print("CREANDO....")
            mydb.commit()
            sql = "INSERT INTO temp_od (DKEY, DVALUE) VALUES(%s, %s)"
            print("INSERTANDO....")
            mycursor.executemany(sql, requisito)
            mydb.commit()
            sql = """UPDATE oferta_detalle
                        SET descripcion_normalizada = temp_od.dvalue
                        FROM   temp_od
                        WHERE  oferta_detalle.id_ofertadetalle = temp_od.dkey;"""
            print("ACTUALIZANDO....")   
            mycursor.execute(sql)         
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



