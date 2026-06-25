import json
import os
folderName = "SecondPhase/FinalProject/Data"
jsonFile = f"{folderName}/task.json"
Choice = {
    "Add" : 1,
    "List" : 2,
    "Remove" : 3,
    "Quit" : 4
}


if not os.path.exists(jsonFile) or os.path.getsize(jsonFile) == 0:
    with open(jsonFile, "w") as f:
        json.dump([], f)
        
Task = []
command = 0 

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
        
    if command == Choice["List"]:
        print(Task)
        
    if command == Choice["Remove"]:
        element = input("Choose a Task to remove ")
        element = str(element)
        Task.remove(element)
        
with open(f"{jsonFile}", "w") as file:
        json.dump(Task,file)

