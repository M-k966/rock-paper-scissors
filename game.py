import random
#display the game rules
print("Welcome to the rock-paper scissors game!")
print("Winning rules are:")
print("Rock vs scissors: Rock wins")
print("Scissors vs paper: Scissors wins")
print("Paper vs scissors: Paper wins")

choices = ["rock", "paper", "scissors"]

while True:
    print("choice an option: ")
    print("1-Rock")
    print("2-paper")
    print("3-scissors")

#validate user input
    try:
        choice=int(input("Enter your choice"))
    except ValueError:
        print("please enter a valid number\n")
        continue

    while choice < 1 or choice > 3:
        choice=int(input("Please enter valid choice(1-3):"))

    #user choise
    user_choise=choices[choice-1]

    print("User choise is:",user_choise)
    print("Now it's computer turn:")

    #computer choice
    comp_choice=random.randint(1,3)
    computer_choice=choices[comp_choice-1]

    print("Computer choice is",computer_choice)
    print(user_choise,"vs",computer_choice)

    #ditermine winner
    if choice==comp_choice:
        print("<==It's a tie!==>")
    elif(
        (choice == 1 and comp_choice == 3)or
        (choice==2 and comp_choice == 1)or
        (choice==3 and comp_choice==2)
    ):
       print("<==User winn!==>")
       
    else:
         print("<==Computer winn!==>")

     #play again    
    while (True):
        ans=input("\n Do you want to play again:(Y/N):").lower()

        if ans in['y','n']:
            break
        print("Please enter Y or N")

        if ans =='n':
            break
            print()
    print("\n Thanks for playing!")
    
        

     
