Choice = {
    "Add" : 1,
    "Subtract" : 2,
    "Multiply" : 3,
    "Divide" : 4,
    "Quit" : 5
}

command = 0

def Add (a:float, b:float):
    return a + b

def Subtract(a:float, b:float):
    return a - b

def Multiply (a:float, b:float):
    return a * b

def Divide (a:float, b:float ):
    return a / b


while command != Choice["Quit"] : 
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    command = input("Choose an operation : ")
    command = int(command)
    
    if command != Choice["Quit"] :
        number1 = input("Choose a first number : ")
        number1 = float(number1)
        
        number2 = input("Choose a second number : ")
        number2 = float(number2)
        if command == Choice["Add"]:
            print(f"The result is {Add(number1, number2)}")    
        if command == Choice["Subtract"]:
            print(f"The result is {Subtract(number1, number2)}")
        if command == Choice["Multiply"]:
            print(f"The result is {Multiply(number1, number2)}")
        if command == Choice["Divide"]:
            print(f"The result is {Divide(number1, number2)}")
    