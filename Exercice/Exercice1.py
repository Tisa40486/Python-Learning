print("      EXO 1")
print("-----------------")

name = input("What is your name? ")
age = input("What is your age? ")
age = int(age)

print("Hello", name + "!", "You are", age, "years old.")

print("      EXO 2")
print("-----------------")

c= input("Enter a temperature in Celsius: ")
C = float(c)
F = (C * 9/5) + 32

print("The temperature in Fahrenheit is:", F)


print("      EXO 3")
print("-----------------")

number = input("Enter Number :")

number = int(number)
result = number % 2

if result == 0 :
    print(number, "is odd")
else:
    print(number, "is even")