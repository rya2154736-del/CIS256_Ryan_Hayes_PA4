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

def check_is_letter(guessed_letters):
    is_valid = False
    while not is_valid:
        letter_guess = input("Guess a letter: ").lower()
        if len(letter_guess) != 1:
           print("Invalid guess. Please try again.")
        else:
            if letter_guess.isalpha():
                if letter_guess not in guessed_letters:
                    return letter_guess
                else:
                    print("Letter already guessed. Please try again.")
            else:
                print("Invalid guess. Please try again.")

def if_letter_in_word(letter_guess, unguessed_word, chosen_word):
    count = 0
    unguessed_list = unguessed_word
    if letter_guess in chosen_word:
        for i in range(len(chosen_word)):
            if letter_guess == chosen_word[i]:
                unguessed_list[i] = letter_guess
                count = count + 1
        print(f"{letter_guess} appears {count} times.")
        return unguessed_list
    else:
        print(f"{letter_guess} does not appear.")
        return unguessed_list


while guess_number < MAX_GUESSES and unguessed_word != chosen_word:
    for letter in unguessed_word:
        print(letter, end="")
    print()
    print(f"Guess number {guess_number + 1} of {MAX_GUESSES}")
    
    letter_guess = check_is_letter(guessed_letters)
    unguessed_word = if_letter_in_word(letter_guess, unguessed_word, chosen_word)
    guess_number = guess_number + 1
    guessed_letters.append(letter_guess)
    
    """
    letter_guess = input("Guess a letter: ").lower()
    if len(letter_guess) != 1:
        print("Invalid guess. Please try again.")
        if letter_guess.isalpha:
            letter_guess not in guessed_letters:
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
"""