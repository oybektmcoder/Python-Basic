# def sumn(*numbers):
#   sums=0
#   for num in numbers:
#     sums += num
#   return sums
# print(sumn(1,2,3))
    
# def sumn(*numbers):
#     return sum(numbers)
# print(sumn(1,2,3))

# def sumn(x,y,*numbers):
#     """Summs"""
#     return x+y+sum(numbers)
# print(sumn(1,2,3))

#def avto_info(company,model,**refences):
#    """avto_info"""
#    refences['company']=company
#    refences['model']=model
#    return refences
#car_1=avto_info("GM","Malibu",color='black')
#car_2=avto_info("BMW","BMW",Years=2019)
#print(car_1,car_2)