class Student:
    """Stdent class with name,grade"""
    def __init__(self,name,fname,birth,grade):
        self.name=name
        self.fname=fname
        self.birth=birth
        self.grade=grade
    def get_name(self):
        return self.name
    def get_fname(self):
        return self.fname
    def get_age(self):
        return self.birth
    def get_grade(self):
        return self.grade
    def change_grade(self,new_grade):
        self.grade=new_grade
    def update_grade(self):
        return self.grade+1
    def info(self):
        return self.name,self.fname,self.grade
    
class Subject:
    def __init__(self,sub_name):
        self.sub_name=sub_name
        self.numbers_of_students=0
        self.students=[]
    def add_student(self,pupil):
        self.students.append(pupil)
        self.numbers_of_students += 1
        
    def get_name_sub(self):
        return self.sub_name
    
    def get_student_subject(self):
        return [x.get_name() for x in self.students]
    
    def get_number(self):
        return self.numbers_of_students
    
def see_method(klass):
    return [m for m in dir(klass) if m.startswith("__") is False]
    
st1=Student("Oybek", "Tursunov", 2005, 1)
st2=Student("Jasur","Qoliyev",2004,2)
st3=Student("UmarBek","Qoldirjanibov",2000,4)

Math=Subject("Mathematic")
Math.add_student(st1)
Math.add_student(st2)
Math.add_student(st3)

        