class User:
    def __init__(self, username:str, password:str,role:int):
        self.__username = username
        self.__password = password
        self.__role = role
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def name(self, username):
        self.__username = username
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, role):
        self.__role = role


    