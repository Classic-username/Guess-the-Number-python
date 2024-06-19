import random
number = random.randint(1, 100)
is_game_over = False
tries = 0

print("Hello, welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100, try to guess...")
while not is_game_over:
    guess = int(input("Enter a number... "))
    tries += 1
    if guess < number:
        print("The number is higher")
    elif guess > number:
        print("The number is lower")
    else:
        is_game_over = True

print(f"Excellent, you guessed in {tries} tries, the number is {number}")
