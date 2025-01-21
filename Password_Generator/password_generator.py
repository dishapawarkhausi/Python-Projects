import random
import string

def generate_password(length=12, use_numbers=True, use_special_chars=True):
    letters = string.ascii_letters
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    all_chars = letters + numbers + special_chars
    if not all_chars:
        return "Please enable at least one character set!"
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

print("Generated Password:", generate_password(length, use_numbers, use_special_chars))
