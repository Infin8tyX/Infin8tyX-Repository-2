import random


def number_guessing_game():
    secretnumber = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secretnumber:
            print("Guess is too low.")
        elif guess > secretnumber:
            print("Guess is too high.")
        else:
            print(f"Congrats, you have guessed the secret number in {attempts} attempts!")
            break
number_guessing_game()