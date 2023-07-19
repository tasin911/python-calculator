def add(x, y):
    return  x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divid(x, y):
    if y == 0:
        return "can't divide by zero"
    else:
        return x / y


def calculator():
    print("here is a python calculator")
    print(f"write your formula +, -, *, /")


    while True:
        operator = input("enter your operator (+, -, *, /) or exit to quit it ")

        if operator == "exit":
            print("exiting the calculator")
            break
        if operator not in ('+', '-', '*', '/'):
            print("enter a valid operator")
            continue
        try:
            x = float(input("enter the first number:"))
            y = float(input("enter the second number:"))
        except ValueError:
            print("Enter a valid value")
            continue

        if operator == '+':
            result = add(x, y)
        elif operator == '-':
            result = sub(x,y)
        elif operator == '*':
            result = multi(x, y)
        elif operator == '/':
            result = divid(x, y)

        print("Result is", result)

if __name__ == "__main__":
    calculator()
        
        