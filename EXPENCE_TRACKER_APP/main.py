def add_expense(expenses,description,amount):
    expenses.append({"description":description,"amount":amount})
    print(f"added expense:{description},{amount}")
    
def get_total_expenses(expenses):
    sum=0
    for expense in expenses:
        sum+=expense['amount']
    return sum
def get_balance(budget,expenses):
    return budget-get_total_expenses(expenses)

def show_budget_details(budget,expenses):
    print(f"Total Budget:",{budget})
    print(f"Expenses")
    for expense in expenses:
        print(f" -{expense["description"]},{expense['amount']}")
    print(f"total spent:{get_total_expenses(expenses)}")
    print(f"remaining budget :{get_balance(budget,expenses)}")            
    
def main():
    print("welocme to the budget App:")
    initial_budget=float(input("pliz enter your initial budget:"))
    budget=initial_budget
    expenses=[]
    while True:
       print("/n What would you like to do..?") 
       print("1.Add an expense")      
       print("2.Show budget details")      
       print("3.exit")   
       choice=int(input("enter the choice (1/2/3)")) 
    
       if choice==1:
           description=input("Enter the expenses description")
           amount=float(input('Enter the expense amount:'))
           add_expense(expenses,description,amount)      
       elif choice==2:
           show_budget_details(budget,expenses)
       elif choice==3:
           print("thanks for using expense tracker app ")
           break
       else:
           print("invalid choice pliz choose again") 
if __name__=="__main__":
    main()             