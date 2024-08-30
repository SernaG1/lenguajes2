class Device:
    def __init__(self,deviceId,serial,brand,type,purchDate,warantee,classification,
                 ownerId,locationId,supplierId):
        self._deviceId = deviceId
        self._serial = serial
        self._brand = brand
        self._type = type
        self._purchDate = purchDate
        self._warantee = warantee
        self._classification = classification
        self._ownerId = ownerId
        self._locationId = locationId
        self._supplierId = supplierId
        
    @property
    def deviceId(self):
        return self._deviceId
    
    @deviceId.setter
    def deviceId(self, deviceId):
        self._deviceId = deviceId

    @property
    def serial(self):
        return self._serial
    
    @serial.setter
    def serial(self, serial):
        self._serial = serial

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def purchDate(self):
        return self._purchDate
    
    @purchDate.setter
    def purchDate(self, purchDate):
        self._purchDate = purchDate

    @property
    def warantee(self):
        return self._warantee
    
    @warantee.setter
    def warantee(self, warantee):
        self._warantee = warantee
    
    @property
    def classification(self):
        return self._classification
    
    @classification.setter
    def classification(self, classification):
        self._classification = classification
    
    @property
    def ownerId(self):
        return self._ownerId
    
    @ownerId.setter
    def ownerId(self, ownerId):
        self._ownerId = ownerId

    @property
    def locationId(self):   
        return self._locationId
    
    @locationId.setter
    def locationId(self, locationId):
        self._locationId = locationId
    
    @property
    def supplierId(self):
        return self._supplierId
    
    @supplierId.setter
    def supplierId(self, supplierId):
        self._supplierId = supplierId

    