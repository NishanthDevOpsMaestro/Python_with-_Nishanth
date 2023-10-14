import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

all_characters = lower + upper + numbers + symbols
password_length = 16

password = ''.join(random.choices(all_characters, k=password_length))
print("Your new Password IS: " + password)
