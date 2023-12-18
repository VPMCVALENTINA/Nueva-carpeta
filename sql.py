##############################
## SQL SERVER DB CONNECTION
##############################

#(USING DSN)
db = pypyodbc.connect('DSN=dsn name;')

cur = db.cursor()
cur.execute("SELECT * FROM dbo.tablename")

cur.close()
db.close()


# (USING DRIVER)
constr = 'Trusted_Connection=yes;DRIVER={SQL Server};SERVER=servername;' \
         'DATABASE=database name;UID=username;PWD=password'
db = pypyodbc.connect(constr)

cur = db.cursor()
cur.execute("SELECT * FROM dbo.tablename")

cur.close()
db.close()