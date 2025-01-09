contacts={}

while True:
    print("CONTACT INFORMATIONS APP")
    print("1.Create Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search Contact")
    print("6.Count Contact")
    print("7.Exit")
    
    choice=int(input('Enter the choice :'))
    
    if choice==1:
        name=input("Enter the name :")
        if name not in contacts:
            age=int(input("Enter the age :")) 
            email=input("Enter the email :")
            mobile=input("Enter the mobile number :")
            contacts[name]={'age':int(age),'email':(email),'mobile':(mobile)}
            print(f"Contact {name} has been created sucessufully.. ")
        else:
            print(f" Contact {name} has already present in the contact") 
    
    elif choice==2:
        name=input("Enter the name :")
        if name in contacts:
            contact=contacts[name]
            print(f"Name :{name}, Age :{age} ,Email:{email} ,Mobile Number:{mobile}")
        else:
            print(f" Contact {name} has not found in Contact list")
    
    elif choice==3:
        name=input("Enter the name:")
        if name in contacts:
            age=int(input("Enter the age :")) 
            email=input("Enter the email :")
            mobile=input("Enter the mobile number :")
            contacts[name]={'age':int(age),'email':(email),'mobile':(mobile)}
            print(f"Contact {name} has been updated sucessufully.. ")
        else:
            print(f" Contact {name} has not found in Contact list")
                
    
    elif choice==4:
        name=input("Enter the name :")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} has been deleted sucessufully.. ")
        else:
            print(f" Contact {name} has not found in Contact list") 
            
    elif choice==5:
        search_name=input("enter the name to search :")
        found=False
        for name ,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found -Name :{name}, Age :{age},Mobile Number:{mobile},Email:{email}")
                found=True
        if not found:
            print(f"NO contact found with the name") 
    elif choice==6:
        print(f"Total contact in your book:{len(contacts)}")                   
        
    elif choice==7:
        print("thanks for using this application")
        break
    else:
        print("you enter the wrong choice")                      
            
                    
                