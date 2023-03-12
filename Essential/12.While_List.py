# print("Your friends name:")
# names=[]
# n=1
# while True:
#     question = f"{n}-name of friend:"
#     n=n+1
#     name=input(question)
#     names.append(name)
#     question_again = "You want to add new one (Yes/No):"
#     check=input(question_again)
#     if check=='No':
#         break
# print("Finished",len(names))
# for name in names:
#     print(name.title(),end="  ")
#
# print("Age of Friends")
# friends={}
# stamp=True
# n=0
# while stamp:
#     n = n + 1
#     name=input(f"Name of {n}-Friends:")
#     age=int(input(f"Age of {n}({name})-Frineds:"))
#     question_again = input("You want to add new one (Yes/No):")
#     friends[name]=age
#     if question_again=="No":
#         stamp=False
#
# print("Finished",n)
# for key,value in friends.items():
#     print(f"Name:{key.title()} age is {value}")
#
# #
# cars=['mers','gelik','nexia','avantra','audio','gelik','gelik',]
# print(cars)
# cars.remove('gelik')
#
# print(cars)
# while 'gelik' in cars:
#     cars.remove('gelik')
# print(cars)

# students=['asad','jasur','olim','botir']
# grade_students={}
# while students:
#     student=students.pop()
#     grade=input(f"{student.title()}ning bahola:")
#     grade_students[student]=grade
#
# print("Finished")
# for name,grade in grade_students.items():
#     print(f"{name.title()}ning ogan bahosi - {grade}")
