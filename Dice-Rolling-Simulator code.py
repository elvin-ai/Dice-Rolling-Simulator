import random
print("Hello There! Welcome to the Dice Rolling Simulator. May I know your name please?")
name=input()
print("Okay, ",name,", Let's begin.")
while(True) :
    n=random.randint(1,6)
    print(n)
    print("Do you want to continue (y/n)? : ")
    choice=input()
    if(choice=='n'):
        break
    elif (choice=='y'):
        continue
    else :
        print("Invalid choice.Re-enter")
        choice=input()


print(f"Thank you {name} .Hope you enjoyed!!!")