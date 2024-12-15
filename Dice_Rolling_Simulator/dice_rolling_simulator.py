import random

DICE_FACES = {
    1: (
        " ------- \n"
        "|       |\n"
        "|   *   |\n"
        "|       |\n"
        " ------- "
    ),
    2: (
        " ------- \n"
        "| *     |\n"
        "|       |\n"
        "|     * |\n"
        " ------- "
    ),
    3: (
        " ------- \n"
        "| *     |\n"
        "|   *   |\n"
        "|     * |\n"
        " ------- "
    ),
    4: (
        " ------- \n"
        "| *   * |\n"
        "|       |\n"
        "| *   * |\n"
        " ------- "
    ),
    5: (
        " ------- \n"
        "| *   * |\n"
        "|   *   |\n"
        "| *   * |\n"
        " ------- "
    ),
    6: (
        " ------- \n"
        "| *   * |\n"
        "| *   * |\n"
        "| *   * |\n"
        " ------- "
    ),
}

def roll_dice():
    """Roll a dice and return a random number between 1 and 6."""
    return random.randint(1, 6)

def display_dice_face(number):
    """Display the ASCII art for a dice face based on the number rolled."""
    print(DICE_FACES[number])

def dice_simulator():
    """Run the dice simulator."""
    while True:
        print("\nRolling the dice...")
        dice_number = roll_dice()
        display_dice_face(dice_number)
        
        roll_again = input("Do you want to roll the dice again? (yes/no): ").strip().lower()
        if roll_again == 'no':
            print("Thank you for playing! Goodbye!")
            break

dice_simulator()
