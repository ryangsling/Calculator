logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)



def add(a1,b1):
    return a1+b1

def subtract(a1,b1):
    return a1-b1

def multiply(a1,b1):
    return a1*b1

def divide(a1,b1):
    return a1/b1

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
        
    num1 = float(input("\nWrite the first number: "))

    for key in operations:
        print(key)
    run_program = True
    while run_program:
        symbol = input("Choose operation: ")
        num2 = float(input("Write the second number: "))
        func = operations[symbol]
        answer = func(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        option = input(f"Type 'y' to continue calculating with {answer}, type new to start new calculation, or type 'n' to exit.")
        if option == "y":
            num1=answer
        else:
            run_program=False
            calculator()


calculator()