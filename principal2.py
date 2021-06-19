from configuration import *
from controller import Controller
from preprocessing import PreProcessing
from dbconnection import Connection
from dboperation import DatesDB
import datetime
import numpy as np
import string 
from bs4 import BeautifulSoup


def connect_bd():
    con = Connection(DATABASE["DB_HOST"],DATABASE["DB_SERVICE"], DATABASE["DB_USER"], DATABASE["DB_PASSWORD"])
    con.connect()
    return con

if __name__ == "__main__":
	controller = Controller()
	preprocessing = PreProcessing()
	con = connect_bd()
	oferta_detalle = controller.dbofertadetalle
	# words=[' C ','C++','JAVA','PYTHON','SQL','.NET',' R ',
	# 		'MYSQL','ORACLE',
	# 		'IBM','WORD','ACCES','ISO',
	# 		'ANDROID','COBOL','PERL','WEB','WEB SERVICES','API DE GOOGLE','APLICACIONES','SOFTWARE', 
	# 		'REST'
	# 	]

	words=['JASPER REPORTS']

	nro_rows = 0
	for w in words:
		rows = oferta_detalle.filtrar(con,w)
		nro_rows += len(rows)
		print(rows,"\n")
		#oferta_detalle.update_tuple(con,rows,"CloudX")
		# for row in rows:
		# 	id_rows.append(row)

	print(nro_rows)

	#id_strings = ','.join(map(str,id_rows))

	#oferta_detalle.update_tuple(con,id_rows,"CloudX")
		