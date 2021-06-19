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
	
	words=["JAVA"]
	for w in words:
		print(oferta_detalle.filtrar(con,w))
