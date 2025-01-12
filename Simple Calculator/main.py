def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Get user input for the operation
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please select a valid option.")
                continue
            
            # Get user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the selected operation
            if choice == 1:
                print(f"The result of {num1} + {num2} is {add(num1, num2)}.")
            elif choice == 2:
                print(f"The result of {num1} - {num2} is {subtract(num1, num2)}.")
            elif choice == 3:
                print(f"The result of {num1} * {num2} is {multiply(num1, num2)}.")
            elif choice == 4:
                print(f"The result of {num1} / {num2} is {divide(num1, num2)}.")
            
            # Ask the user if they want to perform another calculation
            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != "yes":
                print("Thanks for using the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Run the calculator
if __name__ == "__main__":
    calculator()
