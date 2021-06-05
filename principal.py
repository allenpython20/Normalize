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
	#matrix = np.array(columna)
	#matrix = ["/_:Allém","???!!!.....",""]
	print("=========")
	matrix = preprocessing.remove_non_ascii(matrix)
	matrix = preprocessing.remove_punctuation_space_start(matrix)
	matrix = preprocessing.remove_punctuation_space_end(matrix)
	matrix = preprocessing.remove_space(matrix)
	# for row in datos:
	#  	print(1,row)

	for indice in range(0,len(matrix)):
		datos[indice][2] = matrix[indice]
	# print("=========")

	# for row in range(0,pivot-1):
	# 	oferta_detalle.update_ofertadetalle_normalized(con,datos[row])

	for row in datos:
		oferta_detalle.update_ofertadetalle_normalized(con,row)
		#print(1,datos[row])

	#====================
	# dic= [{"id":1,"nombre":"pepe1"},{"id":2,"nombre":"pepe2"}]
	# array = [[1,"allen11"],[2,"allen22"]]
	# for i in dic:
	# 	print(i["id"])

	# preprocessing = PreProcessing()
	# controller = Controller()
	# con = connect_bd()
	# oferta = controller.dbofertadetalle
	# #datos = oferta.select_prueba(con)

	# cadena =["1.    #####fdfdf  C#      .","#   #··  !!!###??? !!#allen·####    ·----:::::","D","fff"]
	# cadena = preprocessing.remove_punctuation_space_start(cadena)
	# cadena = preprocessing.remove_punctuation_space_end(cadena)
	# print(cadena)

	# for val in array:
	# 	oferta.update_prueba(con,val)

	# datos = oferta.select_prueba(con)
	# print(datos)
	# for d in dic:
	# 	oferta.update_prueba(con,d)			
