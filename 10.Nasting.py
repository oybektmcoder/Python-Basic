"""car_1={
       'Model':'audio',
       'Years':2020,
       'Coast':12_000,
       'Make':'avto'
       }
car_2={
       'Model':'roys royce',
       'Years':2020,
       'Coast':13_000,
       'Make':'avto'
       }
car_3={
       'Model':'bmw',
       'Years':2020,
       'Coast':14_000,
       'Make':'role'
       }
cars=[car_1,car_2,car_3]
for car in cars:
    for key,value in car.items():
        print(
            f"{key}:{value}"
            )
    print('\n\n')    
"""
"""
GM_company=[]
for car in range(10):
    new_car={
       'Model':'None',
       'Years':2020,
       'Coast':'None',
       'Make':'None',
       'Color':'none' 
        }
    GM_company.append(new_car)
for car in GM_company[0:5]:
    car['Make']="role"    
for car in GM_company[5:]:
    car['Make']="avto"    
for car in GM_company[:3]:
    car['Model']='Malibu'
    car['Color']='Red'
for car in GM_company[3:]:
    car['Model']='Inpala'
    car['Color']='Black'
        

for i in GM_company:
    if(i['Make']=='role'):
        i['Coast']=20_000
    else:
        i['Coast']=25_000    
    print(i)
"""
Classmates={
    'Oybek':['C++','phyton','c#'],
    'Asad':['PHP','phyton','Java'],
    'Jasur':['C','Js','Kotlin'],
    'Manzur':['Html','Css','Js']
    }
for name,lang in Classmates.items():
    print(
        f"Oquvchi:{name} shu tilarni biladi:",end=" "
        )
    for l in lang:
        print(l.title(),end=" ")
    print('\n')




print("sadasdasdasdas")




  