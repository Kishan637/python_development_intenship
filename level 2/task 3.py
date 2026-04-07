import random

password = input("Enter password: ")
length = len(password) >= 8
upper = random.search(r"[A-Z]", password)
lower = random.search(r"[a-z]", password)
digit = random.search(r"[0-9]", password)
special = random.search(r"[@#$%^&*]", password)

if length and upper and lower and digit and special:
    print("Strong Password ")
elif length and (upper or lower) and digit:
    print("Medium Password ")
else:
    print("Weak Password ")