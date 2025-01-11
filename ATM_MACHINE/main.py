import time

print("please enter your card ")
time.sleep(5)
password=1234

pin=int(input("enter your pin"))

balance=500000
while True:
    if pin==password:
        print("1.balance \n2.withdrow balance \n3.deposite balance\n4.exit")
        try:
            opt=int(input("enter your choice"))
        except:
            print("please choose valid options:") 


        if opt==1:
            print(f"your balance is {balance}")       

        elif opt==2:
            withdrow_amont=int(input("how much amount you want to withdraw"))
            balance=balance-withdrow_amont
            print(f"{withdrow_amont} is debited from your account")
            print(f"your updated balace is {balance}")
            
        elif opt==3:
            deposit_amount=int(input("enter the deposite amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is created to your account..")
            print(f"your updated balace is {balance}")   

        elif opt==4:
            print(f"thanks for using this atm")
            break
                
    else:
        print("you enter a wrong pin pliz try again")    