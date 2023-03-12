class Avto:
    num_avto=0
    def __init__(self,make,model,color,years,coast,km=0):
        self.make=make
        self.model=model
        self.color=color
        self.years=years
        self.coast=coast
        self.__km=km
        Avto.num_avto+=1
        
  #  def __str__(self):
  #     return f"Name:{self.make}"
    def __repr__(self):
        return f"Name:{self.model}"
    def __eq__(self, o):
        return self.coast==o.coast
    def __lt__(self,o):
        return self.coast<o.coast
    def __le__(self,o):
        return self.coast>o.coast
    
class AvtaSalon:
    def __init__(self,name):
        self.name=name
        self.cars=[]
    def __getitem__(self,indeks):
        return self.cars[indeks]
    def __len__(self):
        return len(self.cars)
    def __setitem__(self,indeks,value):
        self.cars[indeks]=value
        return self.cars[indeks]
    def add_car(self,*value):
        for c in value:
            if isinstance(c, Avto):
                self.cars.append(c)
            else:
                print("Eror")
                
                
                
G_salon=AvtaSalon("GM")
car_1=Avto("Make", "Jeep","Red",2022,1455,2000)
car_2=Avto("Make", "Jeep","Red",2022,1455,4500)
G_salon.add_car(car_1,car_2)
