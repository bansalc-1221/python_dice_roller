import random

count = 0
roll_history = []


def welcome():
    print("=" * 40)
    print("Welcome to the Dice Roller!")
    print("=" * 40)


def roll_dice():
    global count

    input("\nPress Enter to roll the dice...")

    roll = random.randint(1, 6)

    roll_history.append(roll)
    count += 1

    print(f"\nRoll #{count}")
    print(f"You rolled: {roll}")


def play_again():

    while True:
        choice = input("\nDo you want to roll again? (y/n): ").strip().lower()

        if choice == "y":
            return True

        elif choice == "n":
            return False

        else:
            print("Invalid input! Please enter only 'y' or 'n'.")


def game_summary():
    
    print("=" * 20)
    print("\tGAME SUMMARY")
    print("=" * 20)

    print("\nRoll History:")

    print(roll_history)
    print(f"\nTotal Rolls : {count}")
    print(f"Highest Roll: {max(roll_history)}")
    print(f"Lowest Roll : {min(roll_history)}")
    print(f"Average Roll: {sum(roll_history) / len(roll_history):.2f}")

    print("=" * 40)

welcome()

while True:

    roll_dice()

    if not play_again():
        print("\nGreat game!")
        print(f"You rolled the dice {count} time/s.")
        print("Thanks for playing!")
        break

game_summary()
