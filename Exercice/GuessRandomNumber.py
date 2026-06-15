import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
print("------------------")
print(" Guess The number ")
print("------------------")

number = random.randint(0,100)
guess = 0
Nbguess = 0

while guess != number:
    guess = input("choose a number: ")
    guess = int(guess)
    
    if guess > number:
        Nbguess += 1
        print(bcolors.FAIL, "too high... \n",end=" ")
        print(bcolors.ENDC,"Number of try : ",Nbguess)
        
    else:
        Nbguess += 1
        print(bcolors.FAIL, "too low... \n", end=" ")
        print(bcolors.ENDC,"Number of try : ", Nbguess)
        
        
print("WELL DONE !! The number was", number)