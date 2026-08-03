def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def mod(a, b):
    if b == 0:
        return "Modulo by zero is not allowed"
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n===== CLI Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Calculator Closed")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(a, b))
    elif choice == 2:
        print("Result =", sub(a, b))
    elif choice == 3:
        print("Result =", mul(a, b))
    elif choice == 4:
        print("Result =", div(a, b))
    elif choice == 5:
        print("Result =", mod(a, b))
    elif choice == 6:
        print("Result =", power(a, b))
    else:
        print("Invalid Choice")