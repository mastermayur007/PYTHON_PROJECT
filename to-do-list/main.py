def task():
    tasks=[]
    print("----------WELCOME TO THE TASK MANAGEMENT APP---------------")
    total_task=int(input("Enter how many task you have to enter:"))
    for i in range(1,total_task+1):
        task_name=input("Enter the task you want to add:")
        tasks.append(task_name)
    print(f"Todays task arr\n{tasks}") 
    while True:
       operations=int(input("Enter \n 1-add \n 2-update \n 3-delete \n 4-views \n 5-Exit/stop/"))
       if operations==1:
           add=input("Enter the task you have to add:") 
           tasks.append(add)
           print(f"Task{add} has been successufully added....")
        
       elif operations==2:
           update_task=input("Enter the task you have to update") 
           if update_task in tasks:
               up=input("Enter new task:")                
               ind=tasks.append(update_task)
               tasks[ind]=up
               print(f"updated task {up}")
       elif operations==3:
                   del_val=input("Enter the task that you have to delete")
                   if del_val in tasks:
                       ind=task.index(del_val)
                       del tasks[ind]
                       print(f"task{del_val} has been deleted successufully.....")
       elif operations==4:
           print(f"Total task is {tasks}")
       elif operations==5:
           print(f"clossing the program....") 
           break
       else:
           print(f"pliz enter the correct options") 
task()                            
                           