import random
import csv
number = random.randint(1, 100)
is_game_over = False
tries = 0

user_name = input("Hello, welcome to Guess the Number! Please enter your name: ")
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

print(f"Excellent work {user_name}, you guessed in {tries} tries, the number is {number}")

with open("scores.csv", "a", newline = "") as csvfile:
    scorewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    scorewriter.writerow([user_name, tries, number])