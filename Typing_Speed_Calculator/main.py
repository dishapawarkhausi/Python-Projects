from time import time
import random as r

def calculate_accuracy(partest, usertest):
    correct_chars = sum(1 for i in range(min(len(partest), len(usertest))) if partest[i] == usertest[i])
    total_chars = len(partest)
    accuracy = (correct_chars / total_chars) * 100
    return round(accuracy, 2)

def calculate_speed(start_time, end_time, userinput):
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    word_count = len(userinput.split())
    speed = word_count / elapsed_minutes
    return round(speed, 2)

if __name__ == '__main__':
    while True:
        ck = input("Ready to test? (yes/no): ").lower()
        if ck == "yes":
            test_sentences = [
                "The quick brown fox jumps over the lazy dog near the riverbank, testing its agility and speed.",
                "In the world of technology, innovation drives progress, and every idea counts towards building a better future."
            ]
            print(" ***** Typing Speed Test *****")
            test_sentence = r.choice(test_sentences)
            print(test_sentence)
            print()
            
            start_time = time()
            user_input = input("Start typing: ")
            end_time = time()

            speed = calculate_speed(start_time, end_time, user_input)
            accuracy = calculate_accuracy(test_sentence, user_input)

            print(f"\nTyping Speed: {speed} w/min")
            print(f"Accuracy: {accuracy} %\n")

        elif ck == 'no':
            print("Thank you for using the Typing Speed Test. Goodbye!")
            break
        else:
            print("Invalid input! Please type 'yes' or 'no'.")
          
