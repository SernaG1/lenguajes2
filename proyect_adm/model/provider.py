class Provider:
    def __init__(self, nit, comp_name,address,phone, email):
        self.__nit = nit
        self.__comp_name = comp_name
        self.__address = address
        self.__phone = phone
        self.__email = email

    @property
    def nit(self):
        return self.__nit
    
    @nit.setter
    def nit(self, value):
        self.__nit = value
    
    @property
    def comp_name(self):
        return self.__comp_name
    
    @comp_name.setter
    def comp_name(self, value):
        self.__comp_name = value

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, value):
        self.__address = value
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    @property
    def email(self):   
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value