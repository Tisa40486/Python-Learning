class User:
    def __init__(self, name : str, age:int):
            self.name = name
            self.age = age
            
    def greet(self) -> str:
        return f"Hello, i'm {self.name}"
    
user = User("Picasso", 13)

print(user.greet())