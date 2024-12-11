import tkinter as tk
from time import time
import random as r

def start_test():
    global start_time, test_sentence
    test_sentence = r.choice(sentences)
    prompt_label.config(text=test_sentence)
    input_text.delete("1.0", tk.END)
    start_time = time()
    result_label.config(text="")
    accuracy_label.config(text="")

def calculate_results():
    global start_time, test_sentence
    end_time = time()
    user_input = input_text.get("1.0", tk.END).strip()
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60

    word_count = len(user_input.split())
    speed = word_count / elapsed_minutes

    correct_chars = sum(1 for i in range(min(len(test_sentence), len(user_input))) if test_sentence[i] == user_input[i])
    total_chars = len(test_sentence)
    accuracy = (correct_chars / total_chars) * 100

    result_label.config(text=f"Speed: {round(speed, 2)} w/min")
    accuracy_label.config(text=f"Accuracy: {round(accuracy, 2)} %")

root = tk.Tk()
root.title("Typing Speed Calculator")
root.geometry("600x400")

sentences = [
    "The quick brown fox jumps over the lazy dog near the riverbank, testing its agility and speed.",
    "In the world of technology, innovation drives progress, and every idea counts towards building a better future."
]

prompt_label = tk.Label(root, text="Click 'Start' to begin the test", wraplength=500, font=("Arial", 14), justify="center")
prompt_label.pack(pady=20)

input_text = tk.Text(root, height=5, width=50, wrap=tk.WORD, font=("Arial", 12))
input_text.pack(pady=10)

start_button = tk.Button(root, text="Start", command=start_test, font=("Arial", 12))
start_button.pack(pady=5)

finish_button = tk.Button(root, text="Finish", command=calculate_results, font=("Arial", 12))
finish_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

accuracy_label = tk.Label(root, text="", font=("Arial", 14))
accuracy_label.pack(pady=10)

root.mainloop()
