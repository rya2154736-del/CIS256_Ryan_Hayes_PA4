# Ryan Hayes
# CIS256 Fall 2026
# Programming Assignment 4

import random

MAX_GUESSES = 10

guess_word_list = [
    "abacus",
    "beaut",
    "candy",
    "steak"
]

guessed_letters = []

chosen_word = random.choice(guess_word_list)
guess_number = 0
unguessed_word = list("_" * len(chosen_word))


while guess_number < MAX_GUESSES and unguessed_word != chosen_word:
    for letter in unguessed_word:
        print(letter, end="")
    #print(unguessed_word)
    print()
    print(f"Guess number {guess_number + 1} of {MAX_GUESSES}")
    #try: 
    letter_guess = input("Guess a letter: ").lower()
    if len(letter_guess) != 1:
        print("Invalid guess. Please try again.")
    elif letter_guess not in guessed_letters:
        guess_number = guess_number + 1
        guessed_letters.append(letter_guess.lower())
        if letter_guess in chosen_word:
            for i in range(len(chosen_word)):
                if letter_guess == chosen_word[i]:
                    unguessed_word[i] = letter_guess
            print(f"{letter_guess} appears {1} time(s).")
        elif letter_guess not in chosen_word:
            print(f"{letter_guess} does not appear.")
    elif letter_guess in guessed_letters:
        print(f"{letter_guess} already guessed.")
#except:
    #print(f"{letter_guess} is not a valid guess. Try again.")
            
