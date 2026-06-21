print("-----------------")
print("   ODD OR EVEN   ")
print("-----------------")

number = input("Enter Number : ")

number = int(number)
result = number % 2

if result == 0 :
    print(number, "is odd")
else:
    print(number, "is even")