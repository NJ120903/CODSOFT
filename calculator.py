# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function
def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter operation choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the calculation based on the user's choice
    if choice == '1':
        print("Addition is :", add(num1, num2))
    elif choice == '2':
        print("Substraction is :", subtract(num1, num2))
    elif choice == '3':
        print("Product is :", multiply(num1, num2))
    elif choice == '4':
        print("Divide is :", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()