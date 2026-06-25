import json
import os
from datetime import datetime

folderName = "SecondPhase/FinalProject/Data"
jsonFile = f"{folderName}/task.json"
Task = []
command = 0 
Choice = {
    "Add" : 1,
    "List" : 2,
    "Remove" : 3,
    "Quit" : 4
}

def writeLog(message : str) :
    dt = datetime.now()
    
    with open(f"{folderName}/log.txt", "a") as file:
        file.write(f"New log entry : {dt} \n")
        file.write(f" --{message} \n")

if not os.path.exists(jsonFile) or os.path.getsize(jsonFile) == 0:
    with open(jsonFile, "w") as f:
        json.dump([], f)
        
with open(f"{folderName}/task.json", "r") as file:
    loaded = json.load(file)
    Task = loaded

while command != Choice["Quit"]: 
    
    print("1. add")
    print("2. List")
    print("3. Remove")
    print("4. Quit")
    
    command = input("Choose an option : ")
    command = int(command)
    
    if command == Choice["Add"]:
        taskName = input("Enter task name : ")
        Task.append(taskName)
        print("Added!")
        writeLog(f" \"{taskName}\" added Successfully")
        
    if command == Choice["List"]:
        print(Task)
        writeLog(f"The list was printed")
        
    if command == Choice["Remove"]:
        try:
            element = input("Choose a Task to remove ")
            element = str(element)
            Task.remove(element)
            writeLog(f" \"{element}\" was removed.")
        except Exception as e:
            print("Oups problems, retry :(")
            writeLog(f" \"{e}\" run into a problem")
            
        
with open(f"{jsonFile}", "w") as file:
        json.dump(Task,file)

