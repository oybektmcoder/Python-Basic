# def HI_me():
#     """Hi to you"""
#     print("Hello")
# HI_me()

# f_name='Oybek'
# l_name='Tursunov'
# def Full_name(f_name,l_name):
#     fu_name=f"F_name:{f_name}\nL_name:{l_name}"
#     return fu_name
# student1=Full_name("Asad","Aliomov")
# student2=Full_name("Jasur","qodirov")
# print(student2,student1)
#
def avto_info(make,models,years,role,color,coast=None):
    avto={
        'Company':make,
        'Models':models,
        'Years':years,
        'Role':role,
        'Color':color,
        'coast':coast
    }
    return avto
# BMW_y=avto_info('GM','Malibu','2023','Avto','Black',1700)
# BMW_X=avto_info('GM','Gelik','2022','Avto','White',2600)
# BMW=[BMW_X,BMW_y]
# for car in BMW:
#     for key,value in car.items():
#         print(key,'\t=\t',value)
#     print('\n\n')
# #
# print("Hi,gonna to add:")
# f=True
# Cars=[]
# while f:
#     make=input("Make:"),
#     models=input("Models:"),
#     years=input("Years:"),
#     role=input("Role:"),
#     color=input("Color:"),
#     coast =input("Coast:")
#     fu=input("New one Yes/No:")
#     if fu=='No':
#         f=False
#     Cars.append(avto_info(make,models,years,role,color,coast))
#
#
# for car in Cars:
#     print('\n------------------------------------------')
#     for key,value in car.items():
#         print(key,'\t=\t',value)
#     print('\n------------------------------------------')
#






# def add_nums(min,max,step):
#     numbers=[]
#     while min!=max:
#         numbers.append(min)
#         min +=step
#     return numbers
#
#
# print(add_nums(0,15))
#

















