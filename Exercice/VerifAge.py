print("------------------")
print(" AGE VERIFICATION ")
print("------------------")


usaOrEurope = input("Choose rules : \n 1) usa \n 2) Europa \n")
usaOrEurope = int(usaOrEurope)

if usaOrEurope == 1:
    majority = 21
    
elif usaOrEurope == 2:
    majority = 18
    
else :
    print("Wrong input, read carefully.")
    quit()
    
age = input("Enter your age ")
age = int(age)

if  age >= majority :
    print("Adult")
else : 
    
    print("minor")
