import mysql.connector

__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx == None:
        __cnx = mysql.connector.connect(host="remotemysql.com",user="91yKbjoVQb",password="hu2iwKd7wK",database="91yKbjoVQb")
    return __cnx
