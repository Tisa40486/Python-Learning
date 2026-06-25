fileName = "SecondPhase/Exercice/test.txt"

with open(fileName) as file:
    content = file.read()
    print(content)
    
with open(fileName) as file:
    for line in file:
        print(line.strip())
        
with open("SecondPhase/Exercice/Output.txt", "w") as file:
    file.write("Hello World")

with open("SecondPhase/Exercice/Log.txt", "a") as file:
    file.write("New log entry\n")
    
try:
    number = int(input("Enter an number:"))
    result = 10 / number
except ZeroDivisionError:
    print("Error")
    with open("SecondPhase/Exercice/Log.txt", "a") as file:
        file.write("New log entry\n")
        file.write("Cannot devide by zero \n")
except ValueError: 
        print("Error")
        with open("SecondPhase/Exercice/Log.txt", "a") as file:
            file.write("New log entry\n")
            file.write("Invalid Input \n")
finally :
    print("Done")
    


