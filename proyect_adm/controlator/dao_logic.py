import mysql.connector
from mysql.connector import Error
from PyQt6 import QtCore, QtGui, QtWidgets
from model.owner import Owner
from model.device import Device
from model.user import User
from model.provider import Provider

class Dao:
    def __init__(self,db):
        self.db = db

    def create_owner(self, owner: Owner):
        cursor = self.db.cursor()
        query = "INSERT INTO owners (ownerid, names, surnames, email, phone) VALUES (%s, %s, %s, %s, %s)"
        values = (owner.ownerid, owner.name, owner.surname, owner.email, owner.phone)
        
        try:
            cursor.execute(query, values)
            self.db.commit()

        except mysql.connector.Error as error:
            print("Error while creating owner:", error)
            self.db.rollback()
        finally: 
            cursor.close()

    def create_provider(self, provider=Provider):
        cursor = self.db.cursor()
        query = "INSERT INTO providers ( nit, comp_name, address, phone, email) VALUES (%s, %s, %s, %s, %s)"
        values =  (provider.nit, provider.comp_name, provider.address, provider.phone, provider.email)
        try:
            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print("Error while creating provider:", error)
            self.db.rollback()
        finally:
            cursor.close()
    

    def create_device(self,device:Device):
        cursor=self.db.cursor()
        query = "INSERT INTO devices (deviceid, serial, brand, type, purchdate, warantee, classification, ownerid,locationid, supplierid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (device.deviceId, device.serial, device.brand, device.type, device.purchDate, device.warantee, device.classification, device.ownerId, device.locationId, device.supplierId)
        try:
            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print("Error while creating device:", error)
            self.db.rollback()
        finally:
            cursor.close()

    def create_user(self,user:User):
        cursor=self.db.cursor()
        query = "INSERT INTO users (user_name, pass, role_id) VALUES (%s, %s, %s)"
        values = (user.username, user.password, user.role)
        try:
            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print("Error while creating user:", error)
            self.db.rollback()
        finally:
            cursor.close()
    
    def search_owner(self,owner_id):
        search=(owner_id,)
        cursor=self.db.cursor()
        query = "SELECT * FROM owners WHERE ownerid= %s"
        try:
            cursor.execute(query, search)
            result = cursor.fetchone()
            return Owner(result[0], result[1], result[2], result[3], result[4])
        except:
            print("Error while searching owner")
            return None
        finally:
            cursor.close()

    def validate_credentials(self, username, password):
        search=(username,)
        cursor=self.db.cursor()
        query = "SELECT * FROM users WHERE user_name= %s"
        try:
            cursor.execute(query, search)
            result = cursor.fetchone()
            if result and result[1] == password:
                return True
            else:
                print('Could not find')
                return False
        except:
            print("Error while validating credentials")
            return None
        finally:
            cursor.close()


    def search_device(self, device_id):
        search=(device_id,)
        cursor=self.db.cursor()
        query = "SELECT * FROM devices WHERE deviceid= %s"
        try:
            cursor.execute(query, search)
            result = cursor.fetchone()
            return Device(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9])
        except:
            print("Error while searching device")
            return None
        finally:
            cursor.close()
    
