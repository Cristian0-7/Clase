import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Documents\Software\Baseprueba.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM persona1")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close
 