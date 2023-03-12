from uuid import uuid4

class Avto:
    num_avto=0
    def __init__(self,make,model,color,years,coast,km=0):
        self.make=make
        self.model=model
        self.color=color
        self.years=years
        self.coast=coast
        self.__km=km
        self.__id=uuid4()
        Avto.num_avto += 1
    @classmethod
    def get_num_avto(cls):
        return cls.num_avto
    
    def get_km(self):
        return self. __km
    def add_km(self,num):
        if(num>0):
            return self.__km+num
        else:
            print("ERROR")
    def get_id(self):
        return self.__id
    
    
car_1=Avto("Make", "Jeep","Red",2022,1455,2000)
car_1=Avto("Make", "Jeep","Red",2022,1455,2000)

