import sqlalhemy
from sqlalchemy import create_engine
import pyodbc
import pandas as pd 

servidor = ""#nombrwe del equipo o laptop
nombre_base_datos = ""# nombre bd

engine = create_engine("myssqlpiodbc://@"+servidor+"/"+nombre_base_datos+"?driver=OBDC+Driver+17+for+SQL+Server")
con = engine.conect()

#Crear querys
query = "SELECT * FROM NAME"


#Leer querys
df = pd.read_sql(query,con)
df.nead