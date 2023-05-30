import random

ch = "y"

while(ch=="y"):
    
    ans = random.randint(1,6)
    
    if(ans == 1):
        print("|-------|")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("|-------|")
    elif(ans==2):
        print("|-------|")
        print("|*      |")
        print("|       |")
        print("|      *|")
        print("|-------|")
    elif(ans==3):
        print("|-------|")
        print("|       |")
        print("| * * * |")
        print("|       |")
        print("|-------|")
    elif(ans==4):
        print("|-------|")
        print("|*     *|")
        print("|       |")
        print("|*     *|")
        print("|-------|")
    elif(ans==5):
        print("|-------|")
        print("|*     *|")
        print("|   *   |")
        print("|*     *|")
        print("|-------|")
    elif(ans==6):
        print("|-------|")
        print("|*     *|")
        print("|*     *|")
        print("|*     *|")
        print("|-------|")


    ch = input("Enter 'y' to roll and 'n' to exit")

