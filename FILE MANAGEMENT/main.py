import os 

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"{filename} has been  created...")
    except FileExistsError:
        print(f"{filename} is alredy exist...") 
    except Exception as e:
        print("an error occured...") 

def view_all_file():
    files=os.listdir()
    if not files:
        print("files are not present..")
    else:
        print("files in directorty") 
        for file in files:
            print(file)
def delete_file(filename):
    try:
        files=os.remove(filename)
        print(f"{filename} has been deleted in the system")
    except FileNotFoundError:
        print(f"{filename} is not found")
    except Exception as e:
        print("an error occored...") 

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"content of {filename}:\n {content}")
    except FileNotFoundError:
        print(f"file has not been found...")
    except Exception as e:
        print("an error occure")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input("Enter data to add the file")
            f.write(content+"\n")
            print(f"content added to {filename} sucessufully")
    except FileNotFoundError:
        print(f"file has not present in the database..")
    except Exception as e:
        print("an error occour") 
def main():
    while True:
        print("WELCOME TO THE FILE MANAGEMNT APP")
        print("1.Create file")                                       
        print("2.view file")                                       
        print("3.Delete file")                                       
        print("4.read file")                                       
        print("5.edit file")                                       
        print("6.exit file")                                       
        
        choice=int(input("enter the option :"))
        
        if choice==1:
            filename=input("enter the file you want to create :")
            create_file(filename)
        elif choice==2:
            view_all_file()
        elif choice==3:
            filename=input("enter the file you want to Delete :")
            delete_file(filename)
        elif choice==4:
            filename=input("enter the file you want to Read :")
            read_file(filename)
        elif choice==5:
            filename=input("enter the file you want to Edit :")
            edit_file(filename)
        elif choice==6:
            print("thanks for using this app") 
            break
        else:
            print("you enter the wrong choice")           
               
if __name__=="__main__":
    main()                 