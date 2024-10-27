### Part Two -- your code goes here. 
import random

random_number = random.randint(1, 10)

def number_guesser():
    guess = int(input("Guess the random number between 1 and 100: "))
    while guess == random_number:
        print("Correct!")
        break
    else:
        print("Incorrect. Guess again.")
        number_guesser()

number_guesser()