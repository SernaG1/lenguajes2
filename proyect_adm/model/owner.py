class Owner:
    def __init__(self,ownerid,name,surname,email,phone):
        self.__ownerid = ownerid
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone

    @property
    def ownerid(self):
        return self.__ownerid
    
    @ownerid.setter
    def ownerid(self, value):
        self.__ownerid = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value


