from configuration import *
from controller import Controller
from preprocessing import PreProcessing
from dbconnection import Connection
from dboperation import DatesDB
import datetime
import numpy as np
import string 

def connect_bd():
    con = Connection(DATABASE["DB_HOST"],DATABASE["DB_SERVICE"], DATABASE["DB_USER"], DATABASE["DB_PASSWORD"])
    con.connect()
    return con

if __name__ == "__main__":
	controller = Controller()
	preprocessing = PreProcessing()
	con = connect_bd()
	oferta_detalle = controller.dbofertadetalle
	datos = oferta_detalle.select_ofertadetalle_dimension(con,3)
	datos = np.array(datos)
	i = 2#columna que queremos obtener
	matrix = [fila[i] for fila in datos]

	#normalizar data
	matrix = preprocessing.remove_non_ascii(matrix)
	matrix = preprocessing.remove_punctuation_space_start(matrix)
	matrix = preprocessing.remove_punctuation_space_end(matrix)
	matrix = preprocessing.remove_space(matrix)

	#modificar la columna de descripcion
	for indice in range(0,len(matrix)):
		datos[indice][2] = matrix[indice]

	#actualizar bbdd
	for row in datos:
		oferta_detalle.update_ofertadetalle_normalized(con,row)

