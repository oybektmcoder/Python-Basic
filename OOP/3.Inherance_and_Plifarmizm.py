class Shaxs:
    def __init__(self,name,fname,year,adress):
        self.name=name
        self.fname=fname
        self.year=year
        self.adress=adress
    def get_info(self):
        msg=f"Name:{self.name}"
        msg+=f"\nSurName:{self.fname}"
        msg+=f"\nAge:{2023-self.year}"
    def get_age(self,now):
        return now-self.year
class Talaba(Shaxs):
    def __init__(self, name, fname, year,adress,grade,id_number):
        super().__init__(name, fname, year,adress)
        self.grade=grade
        self.id_number=id_number
    def get_id(self):
        return self.id_number
    def get_grade(self):
        return self.grade
    def get_info(self):
        msg=f"Name:{self.name}"
        msg+=f" SurName:{self.fname}"
        msg+=f" Age:{2023-self.year}"
        msg+=f" Id_number:{self.id_number}"
        msg+=f" Grade:{self.grade}"
        return msg

class Adress:
    def __init__(self,country,region,number_house):
        self.country=country
        self.region=region
        self.number_house=number_house

    def get_adress(self):
        add=f"Country:{self.country}"
        add+=f" Region:{self.region}"
        add+=f" Number of House:{self.number_house}"
        return add
add=Adress("UZB", "Namangan", "U-24")
s_1=Talaba("Oybek", "Tursunov", 2005, add,1, "A12")



