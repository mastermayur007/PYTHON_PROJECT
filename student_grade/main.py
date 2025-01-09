student_dict={
    
}

def add_student(name,grade):
    student_dict[name]=grade
    print(f"Added {name} with the {grade}")
    
def update_student(name,grade):
    if name in student_dict:
        student_dict[name]=grade
        print(f"updated {name} with the {grade}")
    else:
        print(f"{name} are not present in the student dict")

def delete_student(name,grade):
    if name in student_dict:
        del student_dict[name]
        print(f"{name} has been successufully deleted.......")
    else:
        print(f"{name} has not been  present in student dict")
def view_student():
    if student_dict:
        for name,grade in student_dict.items():
            print(f'{name}:{grade }')      
    else:
        print("student dict are empty")       
        
        
def main():
    while True:
        print("welcome to the balaji high school nagpur")
        print("1.Add Student")         
        print("2.Update Student")         
        print("3.Delete Student")         
        print("4.View Student")         
        print("5.Exit")         
        
        choice=int(input("select the choice you want to enter:"))
        if choice==1:
            name=input("Enter the name of the student:")
            grade=int(input("Enter the grade of the student:"))
            add_student(name,grade)
        elif choice==2:
            name=input("Enter the name of the student:")
            grade=int(input("Enter the grade of the student:"))
            add_student(name,grade)
        elif choice==3:
            name=input("enter the name of the student you want to delete:") 
            delete_student(name,grade)   
        elif choice==4:
            print("===============================================")
            view_student()
            print("===============================================")
        elif choice==5:
            print("thanks for using this code") 
            break
        else:
            print("you enter the wrong choose pliz enter again") 
main()              