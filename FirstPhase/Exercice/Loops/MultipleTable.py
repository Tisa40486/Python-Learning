print("--------------------------")
print("      Multiple Table      ")
print("--------------------------")


choose = input("Enter your number : ")
choose = int(choose)

for i in range(1,11):
    result = choose * i
    print(choose, "x", i, "=", result)