import json


data = {"name": "John", "age": 34}
with open("SecondPhase/Exercice/data.json", "w") as file:
        json.dump(data,file)
        
with open("SecondPhase/Exercice/data.json", "r") as file:
    loaded = json.load(file)
    print(loaded["name"])