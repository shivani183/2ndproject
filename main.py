import mysql.connector
dbConn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop",
)
dbcursor = dbConn.cursor()
sql = "delete from packing where id = 6"
dbcursor.execute(sql)
dbConn.commit()


import mysql.connector
dbConn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop"
)
dbcursor=dbConn.cursor()
dbcursor.execute("drop table bill")

import mysql.connector
dbConn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop"
)
dbcursor = dbConn.cursor()
sql = "insert into packing (expdate,packedby,madeby,itemcode) values (%s,%s,%s,%s)"
val = ("22 june 2029", "heritage", "gold", "5678")
dbcursor.execute("sql,val")
dbConn.commit()
