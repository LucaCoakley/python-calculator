import operator

# function to convert string input to float
def convert_to_float(num):
    if 'm' in num.lower():
        num = float(num[:-1]) * 1_000_000
    elif 'k' in num.lower():
        num = float(num[:-1]) * 1_000
    else:
        num = float(num)
    return num

# dictionary to map operator strings to operations
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "%": operator.mod
}

while True:
    op = input("Please enter an operator (*, +, %, -) or 'exit' to stop: ")
    if op == "exit":
        break
    try:
        num1 = convert_to_float(input("What is your first number: "))
        num2 = convert_to_float(input("What is your second number: "))
        if op in operations:
            ans = operations[op](num1, num2)
            print("Your answer is: ", ans)
        else:
            print("Please enter a valid operator.")
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
