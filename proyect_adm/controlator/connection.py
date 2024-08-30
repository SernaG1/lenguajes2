import mysql.connector

class DataBase:

   def __init__(self):
      self.connection=mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="",
         db="db_adm"
      ) 
      self.cursor = self.connection.cursor()