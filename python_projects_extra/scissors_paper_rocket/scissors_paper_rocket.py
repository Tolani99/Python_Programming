import random

def get_user_choice():
    while True:
        print("Enter your choice: \n1 - Rock \n2 - Paper \n3 - Scissors \n")
        choice = int(input("Enter your choice (1-3): "))
        if 1 <= choice <= 3:
            return choice
        else:
            print("Please enter a valid choice (1-3)")

def get_choice_name(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissors'

def play_game():
    print("Winning rules of the game ROCK PAPER SCISSORS are:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

    while True:
        user_choice = get_user_choice()
        user_choice_name = get_choice_name(user_choice)

        comp_choice = random.randint(1, 3)
        comp_choice_name = get_choice_name(comp_choice)

        print(f"User choice is: {user_choice_name}")
        print("Computer's Turn...")
        print(f"Computer choice is: {comp_choice_name}")

        if user_choice == comp_choice:
            print("It's a Draw!")
        elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (
                user_choice == 3 and comp_choice == 1):
            print(f"{comp_choice_name} Wins!")
        else:
            print(f"{user_choice_name} Wins!")

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

# Start the game
play_game()
