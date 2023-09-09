import sqlite3
import pandas as pd


conexion = sqlite3.connect('database.sqlite')

lectura="Team"
consulta_sql = "SELECT * FROM "+lectura  
df = pd.read_sql_query(consulta_sql, conexion)


nombre_archivo_excel = lectura+'.xlsx'  
df.to_excel(nombre_archivo_excel, index=False)


conexion.close()

print(f"Los datos se han exportado a {nombre_archivo_excel}")
