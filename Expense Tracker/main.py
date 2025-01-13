import datetime
expenses = []

def add_expense():
    description = input("Enter expense description: ").strip()
    category = input("Enter category (e.g., food, transport, entertainment): ").strip()
    try:
        amount = float(input("Enter amount (in USD): "))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expenses.append({"description": description, "category": category, "amount": amount, "date": date})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")

def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\nRecorded Expenses:")
    print(f"{'Date':<20}{'Description':<20}{'Category':<15}{'Amount (USD)':<10}")
    print("-" * 65)
    for expense in expenses:
        print(f"{expense['date']:<20}{expense['description']:<20}{expense['category']:<15}${expense['amount']:<10.2f}")

def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def filter_by_category():
    category = input("Enter the category to filter by: ").strip()
    filtered_expenses = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    if not filtered_expenses:
        print(f"\nNo expenses found for the category '{category}'.")
        return
    
    print(f"\nExpenses for category '{category}':")
    print(f"{'Date':<20}{'Description':<20}{'Category':<15}{'Amount (USD)':<10}")
    print("-" * 65)
    for expense in filtered_expenses:
        print(f"{expense['date']:<20}{expense['description']:<20}{expense['category']:<15}${expense['amount']:<10.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Filter Expenses by Category")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
