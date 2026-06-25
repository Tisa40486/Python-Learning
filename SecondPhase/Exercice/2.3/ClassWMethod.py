class Calculator : 
    def __init__(self, starting_value: int = 0):
        self.value = starting_value
        
    def add(self, n:int):
        self.value += n
        return self.value
    
    def multiply(self, n:int):
        self.value *= n
        return self.value
    
    def reset(self):
        self.value = 0
        

calc = Calculator(10)

print(calc.add(5))

print(calc.multiply(2))
