import random
import os

def intro():
    print(" ***** Welcome to Rock, Paper, Scissors Game *****\n")
    print("Press any key to continue...\n ")
    input()

def clear():
    os.system('cls')

def menu():
    clear()
    print(" ----- MENU ----- \n")
    print("1. Start Game\n")
    print("2. Rules\n")
    print("3. Exit\n")

    menu_option = input("Please select an option: ")
    if menu_option == "1":
        game()
    elif menu_option == "2":
        rules()
    else:
        exit()

def rules():
    clear()
    print("If you don't know the rules yet, what the h*ll did you do in your childhood?\n")
    print("Well, it's easy. You pick one of the three options: rock, paper, or scissors.\n")
    print("Rock beats scissors, scissors beats paper, and paper beats rock.\n")
    print("Press any key to continue...\n")
    input()

def game():
    print("Choose your weapon: rock, paper, or scissors.\n")
    user_action = input("")

    if user_action not in ["rock", "paper", "scissors"]:
        print("Invalid selection. Please try again.\n")
        game()

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    print("Wanna play again? (y/n)\n")

    if input() == "y":
        game()


def main():
    intro()
    while True:
        menu()

if __name__ == "__main__":
    main()