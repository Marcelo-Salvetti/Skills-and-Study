import MySQLdb

def get_db_connection():
    return MySQLdb.connection(
        host="localhost",
        user="root",
        password="Root",
        db="login"
    )