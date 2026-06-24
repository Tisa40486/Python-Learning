def greet(name):
    return f"Hello {name}"

print(greet("Pablo"))


def add(a,b):
    return a + b

print(add(1,2))

def greet(name = "World"):
    return f"Hello {name}"

print(greet("Juan"))
print(greet())

def add(a, b:int) :
    return a + b

print(add(5,3))


def sum_all (*args):
    return sum(args)

print(sum_all(1, 5, 3, 4)) 

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Mattis", age=19, city="Geneva")

def process_user(name:str, age : int = 18, **extra) -> dict :
    return {
        "Name": name,
        "Age" : age,
        "Extra" : extra
    }
    
print(process_user("Sarah", 22, city="Sao Paulo"))
