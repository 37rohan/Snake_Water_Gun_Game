import random
rounds = 10
comp_point = 0
user_point = 0
print("Welcome To Snake, Water and Gun game")
user_name = input("Tell your name:\n")
while rounds > 0:
    rounds -= 1
    computer = ['s', 'w', 'g']
    computer = random.choice(computer)
    # taking random alphabet from rand list

    user_choice = input("Give what you choose (s)snake, (w)water and (g)gun\n")
    # user giving there choice which is feed in user_choice

    # Code for Snake case
    if user_choice == 's' and computer == 's':
        print("Tied")
        print("Both choosing Snake")
        print(f"Chances you left {rounds}\n")

    elif user_choice == 's' and computer == 'w':
        print(f"{user_name} chose {user_choice}")
        print(f"Computer chose {computer}")
        print(f"{user_name} won")
        print("Snake drink water")
        user_point += 1
        print(f"Points scored by {user_name}: {user_point}")
        print(f"Chances you left {rounds} \n")

    elif user_choice == 's' and computer == 'g':
        print(f"{user_name} chose {user_choice}")
        print(f"Computer chose {computer}")
        print("Computer won")
        print("Gun hits snake")
        comp_point += 1
        print(f"Points scored by Computer {comp_point} ")
        print(f"Chances you left {rounds}\n")


    # Code for Water case
    elif user_choice == 'w' and computer == 'w':
        print("Tied")
        print("Both choosing Water")
        print(f"Chances you left {rounds}\n")
   
    elif user_choice == 'w' and computer == 'g':
        print(f"{user_name} chose {user_choice}")
        print(f"Computer chose {computer}")
        print(f"{user_name} Won")
        print("Gun lost in Water")
        user_point += 1
        print(f"Points scored by {user_name} {user_point}")
        print(f"Chances you left {rounds}\n")
   
    elif user_choice == 'w' and computer == 's':
        print(f"{user_name} chose {user_choice}")
        print(f"Computer chose {computer}")
        print("Computer won")
        print("Snake drinks water")
        comp_point += 1
        print(f"Points scored by Computer {comp_point} ")
        print(f"Chances you left {rounds}\n")


    # Code for Gun case
    elif user_choice == 'g' and computer == 'g' :
        print("Tied")
        print("Both choosing Gun")
        print(f"Chances you left {rounds}\n")


    elif user_choice == 'g' and computer == 's':
        print(f"{user_name} chose {user_choice}")
        print(f"Computer chose {computer}")
        print(f"{user_name} Won")
        print("Gun hits Snake")
        user_point += 1
        print(f"Points scored by {user_name} {user_point} ")
        print(f"Chances you left {rounds}\n")


    elif user_choice == 'g' and computer == 'w':
        print(f"{user_name} chose {user_choice}")
        print(f"Computer chose {computer}")
        print("Computer Won")
        print("Gun lost in Water")
        comp_point += 1
        print(f"Points scored by Computer {comp_point}\n ")
        print(f"Chances you left {rounds}\n")

    else:
        print("Invalid Input")
        rounds += 1
        print(f"Chances you left {rounds}\n")


    if rounds == 0:
        if rounds == 0:
            print(f"Total score by {user_name}: {user_point} points")
            print(f"Total score by computer: {comp_point} points")
        if user_point > comp_point:
            print(f"{user_name} won this game by {user_point - comp_point} points")
        elif user_point == comp_point:
            print(f"{user_name} and Computer both Tied by {user_point}, {comp_point} ")
        else:
            print(f"Computer won this game by {comp_point - user_point} points")
        break
    
