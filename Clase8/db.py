import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SENTENCIA SQL")


data = cursor.fetchone() #trae una fila del resultado
todo = cursor.fetchall() #trae un iterable con todas las filas


for fila in todo:
    print(fila[0], fila[1])

db.close()
