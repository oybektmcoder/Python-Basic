"""User={
      'Name':'Oybek',
      'LastName':'Tursunov',
      'Spc':'KaliLinux',
      'Age':18,
      'Intr':'Hacking'
}
print(User.items())
for key,value in User.items():
    print(
        f"Key:{key} \nValue:{value}"
        )
"""
#Phone_own={
#    'Ali':'Iphone',
#    'Vali':'Samsung',
#    'Shodi':'OLG'
#    }
#for key,value in Phone_own.items():
#    print(
#        f"Telefon egasi:{key.title()} Telefon rusumi:{value}\n"
#        )

Market_Vaget={
    'Apple':12_000,
    'Cherry':15_000,
    'Banana':18_000,
    'Potato':22_000,
    'Chips':24_000
    }
print(sorted(Market_Vaget.keys()),"\n",sorted(Market_Vaget.values(),reverse=True))
for key,value in Market_Vaget.items():
    print(
        f"Mahsulot:{key.title()} narxi:{value}"
        )

#print(Market_Vaget.keys())