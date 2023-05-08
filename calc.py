import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x, base):
    return math.log(x, base)

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Power")
print("7. Logarithm")

while True:
    choice = input("Enter choice (1-7): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print("Error:", str(e))
                continue

        print("Result:", result)

    elif choice in ['5', '6', '7']:
        num = float(input("Enter the number: "))

        if choice == '5':
            result = square_root(num)
        elif choice == '6':
            power_num = float(input("Enter the power: "))
            result = power(num, power_num)
        elif choice == '7':
            base = float(input("Enter the base: "))
            result = logarithm(num, base)

        print("Result:", result)

    else:
        print("Invalid input. Please enter a valid choice.")
    
    break
