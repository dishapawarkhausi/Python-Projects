import random
import tkinter as tk
from tkinter import messagebox
import time

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Score tracking
player_score = 0
computer_score = 0
player2_score = 0

# Game Logic
def determine_winner(player_choice, mode="single"):
    global player_score, computer_score, player2_score

    if mode == "single":
        computer_choice = random.choice(choices)
        result_text.set(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            winner_text.set("It's a Tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            winner_text.set("You Win! 🎉")
            player_score += 1
        else:
            winner_text.set("Computer Wins! 😢")
            computer_score += 1
    else:
        player2_choice = random.choice(choices)
        result_text.set(f"Player 2 chose: {player2_choice}")

        if player_choice == player2_choice:
            winner_text.set("It's a Tie!")
        elif (player_choice == "Rock" and player2_choice == "Scissors") or \
             (player_choice == "Paper" and player2_choice == "Rock") or \
             (player_choice == "Scissors" and player2_choice == "Paper"):
            winner_text.set("Player 1 Wins! 🎉")
            player_score += 1
        else:
            winner_text.set("Player 2 Wins! 🎉")
            player2_score += 1

    # Update score
    update_score()
    animate_text()

# Update the score display
def update_score():
    score_label.config(text=f"Player 1: {player_score}  |  Computer: {computer_score}" if mode.get() == "single" else f"Player 1: {player_score}  |  Player 2: {player2_score}")

# Animation effect for winner text
def animate_text():
    for _ in range(3):
        winner_label.config(fg="red")
        root.update()
        time.sleep(0.2)
        winner_label.config(fg="black")
        root.update()
        time.sleep(0.2)

# UI Setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")

# Game mode selection
mode = tk.StringVar(value="single")

# Title Label
tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16, "bold")).pack(pady=10)

# Result Display
result_text = tk.StringVar()
winner_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Helvetica", 12)).pack(pady=5)
winner_label = tk.Label(root, textvariable=winner_text, font=("Helvetica", 14, "bold"))
winner_label.pack(pady=10)

# Score Display
score_label = tk.Label(root, text="Player 1: 0  |  Computer: 0", font=("Helvetica", 12, "bold"))
score_label.pack(pady=10)

# Mode Selection
tk.Radiobutton(root, text="Single Player", variable=mode, value="single").pack()
tk.Radiobutton(root, text="Two Players", variable=mode, value="multi").pack()

# Buttons
frame = tk.Frame(root)
frame.pack()

for choice in choices:
    tk.Button(frame, text=choice, font=("Helvetica", 14), width=10, 
              command=lambda c=choice: determine_winner(c, mode.get())).pack(side=tk.LEFT, padx=5)

# Quit Button
tk.Button(root, text="Quit", font=("Helvetica", 12), command=root.quit).pack(pady=10)

# Run the Game
root.mainloop()
