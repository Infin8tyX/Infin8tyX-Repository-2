import random


def number_guessing_game():
    secretnumber = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("enter your guess: "))
        attempts += 1

        if guess < secretnumber:
            print("Guess is too low.")
        elif guess > secretnumber:
            print("Guess is too high.")
        elif guess > 10:
            print("Invalid answer.")
        else:
            print(f"Congrats, you have guessed the secret number in {attempts} attempts!")
            break


number_guessing_game()