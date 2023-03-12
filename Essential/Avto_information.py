def avto_info(company,model,make,years,machine,coast=None):
    avto={
        'company':company,
        'model':model,
        'make':make,
        'years':years,
        'machine':machine,
        'coast':coast
        }
    return avto

def avto_registration():
    print("Let`s create cars")
    cars=[]
    f=True
    while(f):
        company=input("Company: ")
        model=input("Model: ")
        make=input("Make: ")
        years=input("Years: ")
        machine=input("Machine: ")
        coast=input("Coast($): ")
        fu=input("Do you want continue....\n Please answer with(Yes/No): ")
        cars.append(avto_info(company, model, make, years, machine,coast))
        if(fu=='No'):
            break

def avto_printer(cars):
    for car in cars:
        print("--------------------")
        for key,value in car.items():
            print(f"{key}:{value}")
        print("--------------------")
            
#car_1={
#      'name':'car_1'
#       }
#car_2={
#       'name':'car_2'
#       }
#car_3={
#       'name':'car_3'
#       }
#
#cars=[car_1,car_2,car_3]
#
#
#avto_printer(cars)
            
    
        
