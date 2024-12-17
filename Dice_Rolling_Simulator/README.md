# Dice Rolling Simulator

A Python-based dice rolling simulator that generates random dice rolls and displays the result using ASCII art. Users can roll the dice multiple times and enjoy a visually engaging simulation.

---

## Features
- Simulates rolling a 6-sided dice.
- Displays the dice face using ASCII art.
- Allows users to roll the dice repeatedly until they choose to stop.
- Beginner-friendly and easy to understand.

---

## How It Works
1. The program uses Python's built-in `random` module to generate random numbers between 1 and 6.
2. Each number corresponds to a pre-defined ASCII art representation of a dice face.
3. Users can decide whether to roll the dice again or exit the program.

---

## Installation and Setup

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone or download the project files.
2. Navigate to the project directory.
3. Run the script using the command:
   ```bash
   python dice_rolling_simulator.py
   ```

---

## Usage
1. Run the program.
2. The dice will roll, and an ASCII art representation of the dice face will be displayed.
3. Enter `yes` to roll the dice again or `no` to exit the program.

---

## Code Explanation

### Core Components
- **Random Module:** Used to generate random dice rolls.
- **Dictionary for ASCII Art:** Maps numbers (1-6) to their corresponding ASCII art dice faces.
- **While Loop:** Keeps the simulator running until the user decides to quit.

### Key Functions
- `roll_dice()`: Generates a random number between 1 and 6.
- `display_dice_face(number)`: Prints the ASCII art for the given dice number.
- `dice_simulator()`: The main function that runs the simulator.

---

## Example Output
```
Rolling the dice...
 ------- 
| *     |
|       |
|     * |
 ------- 

Do you want to roll the dice again? (yes/no): yes

Rolling the dice...
 ------- 
| *   * |
|   *   |
| *   * |
 ------- 

Do you want to roll the dice again? (yes/no): no
Thank you for playing! Goodbye!
```

---

## Enhancements (Optional)
1. **Custom Dice Faces:** Add support for different types of dice (e.g., 8-sided or 12-sided).
2. **Multiplayer Mode:** Allow multiple players to roll the dice and determine a winner.
3. **Sound Effects:** Add sound effects during dice rolls using the `playsound` library.
4. **GUI Version:** Use a library like `tkinter` to create a graphical interface for the simulator.

---

## Contributing
Feel free to fork the repository and submit pull requests to improve the project. Suggestions and feedback are always welcome!

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the license terms.

---

## Contact
For any questions or suggestions, feel free to reach out via [GitHub Issues](https://github.com/your-repo/issues).
