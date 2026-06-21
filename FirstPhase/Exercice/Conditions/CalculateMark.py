print("--------------------------")
print("   Calculate mark school  ")
print("--------------------------")
# Input: note (0-100)
# Output: A (90+), B (80-89), C (70-79), D (60-69), F (<60)

mark = input("Input mark ")
mark = int(mark)

if mark > 100:
    print("ERROR ! Mark should be between 0 and 100")
     
if mark >= 90 and mark <= 100:
    print("Your mark is : A, WELL DONE !")

elif mark >= 80 and mark <= 89:
    print("Your mark is : B, CONGRATS !")

elif mark >= 70 and mark <= 79:
    print("Your mark is : C, I WILL GET IT NEXT TIME !!!")
    
elif mark > 60 and mark <= 69:
    print("Your mark is : D, STILL BELIEVE AND WORK HARDER !!")

elif mark < 60:
    print("Your mark is : F, WORK HARDER !!!")
    