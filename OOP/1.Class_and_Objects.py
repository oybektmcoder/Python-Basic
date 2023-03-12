class Student:
    def __init__(self,first_name,last_name,birth_date):
        self.first_name=first_name
        self.last_name=last_name
        self.birth_date=birth_date
    def introduce_me(self):
        print(f"Name:{self.first_name.title()}\nFName:{self.last_name.title()}\nData Birth:{self.birth_date}")
    def get_name(self):
        self.first_name.title()
        return ( self.first_name)
    def get_age(self,years):
        return years-self.birth_date
    
    

st1=Student("Oybek","Tursunov",2022)
