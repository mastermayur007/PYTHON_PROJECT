a='''
======================RENT_CALCULATOR_FOR_DESTRIBUTE_THE_RENT=============================
'''
print(a)
food=int(input("Enter the amount you spend on the Food:"))
Water=int(input("Enter the amount you spend on the Water:"))
Rent=int(input("Enter the amount you have to pay for the rent:"))
Electricity=int(input("enter the electricty unite you use"))
Unites=int(input("enter the electricty Rs per unite you use"))
Total=Electricity*Unites
split=(food+Water+Rent+Total)//4

print(f"Each one you have to pay {split} for the rent")