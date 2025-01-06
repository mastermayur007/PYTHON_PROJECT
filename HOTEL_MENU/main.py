menu={
    'pizza':120,
    'burger':80,
    'French frice':150,
    'biryani':200,
    'cocotale rice':120,
    'coffie':80,
    'chai':20,
    'poha':30
}

print("Welcome to groupze cafe")
print(f"Pizza: Rs120\nBurger: Rs80\nFrench frice: Rs150\nbiryani: Rs200\ncocotale rice: Rs120\ncoffie: Rs80\nchai: Rs20\npoha: Rs30")

order_total=0

item_1=input("enter the item you have to order:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"you have orderd {item_1} and it will be added ")
else:
    print(f"the {item_1} is not currently available in the cafe.....")
another_order=input("you want to add another ither in (yes/no)")    
if another_order=="yes":
    item_2=input('Enter the another item in the menu:')
    if item_2 in menu:
        order_total+=menu[item_2] 
        print("your another item is also added......") 
    else:
        print(f"this item is not available in the cafe yet...")
print(f"The total amount has to pay you is {order_total}")              