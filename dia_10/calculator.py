def sum(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : sum,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

result = None
while True:
    if result is None:
        n1 = float(input("Enter the first number: "))
    else:
        usr_choice = input("Do you want to continue with the previous result [r] or start a new operation [n]?: ")
        if usr_choice == "r":
            n1 = result
        elif usr_choice == "n":
            n1 = float(input("Enter the first number: "))

    usr_operation = input("Enter the operation (+, -, *, /): ")
    n2 = float(input("Enter the second number: "))

    result = operations[usr_operation](n1, n2)
    print(f"{n1} {usr_operation} {n2} = {result}")
    




    
