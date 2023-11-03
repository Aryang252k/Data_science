import mysql.connector
import sys

class DBhelper:
    def __init__(self):
         
         try:
          self.conn=mysql.connector.connect(host='localhost',user='root',password='Aryan@25',database='first_app')
          self.mycursor=self.conn.cursor()

         except:
            print("Some error occured , could not connect to database.")
            sys.exit()

         else:
            print('Connected to Database.')
