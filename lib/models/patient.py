from __init__ import CURSOR, CONN




class Patient:
    def __init__(self,name,age,illness,hospital_id,id=None):
        self.name = name
        self.age = age
        self.illness = illness
        self.hospital_id =  hospital_id
        self.id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str) and len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if not isinstance(value,int) and value > 120:
            raise ValueError("Age must be a realistic integer")
    
hass =Patient("hass", 50,"Weak", 3)
print(hass.age)