# Ryan Hayes
# CIS256 Fall 2026
# Programming Assignment 4

import random

def check_is_letter(guessed_letters):
    """
    Function checks to see if the input is a single alpha letter.

    :param guessed_letters: The list that has the list of letters already guessed.
    :return letter_guess: Returns the final value of the letter guessed
    """
    #Start the loop
    is_valid = False
    while not is_valid:
        #Ask for letter and convert to lower to prevent case sensitivity
        letter_guess = input("Guess a letter: ").lower()
        #Check if input is a single letter
        if len(letter_guess) != 1:
           #Loop if more than one letter
           print("Invalid guess. Please try again.")
        else:
            #Check if single input is an alpha letter
            if letter_guess.isalpha():
                #If the letter has not been guessed return letter
                if letter_guess not in guessed_letters:
                    return letter_guess
                #IF the letter has been guessed, loop again
                else:
                    print("Letter already guessed. Please try again.")
            #Loop if input is not a letter
            else:
                print("Invalid guess. Please try again.")

def if_letter_in_word(letter_guess, unguessed_word, chosen_word):
    """
    Function checks to see if the letter guessed is in the random word.

    :param letter_guess: The letter to check if it is in chosen_word
    :param unguessed_word: The list to update that contains all correctly guessed letters
    :param chosen_word: The word the player is trying to guess
    :return unguessed_list: Returnable version of list to update if letter was guessed correctly
    """
    #Counts the number of times letter_guess appears in chosen_word
    count = 0
    unguessed_list = unguessed_word
    #Checks if the letter appears in the word
    if letter_guess in chosen_word:
        #Checks to see which part of the string is letter_guess
        for i in range(len(chosen_word)):
            #For every index that is the guessed letter
            if letter_guess == chosen_word[i]:
                #Make the index of unguessed_list the letter
                unguessed_list[i] = letter_guess
                #Increment the amount of times letter_guess appears in chosen_word
                count = count + 1
        print(f"{letter_guess} appears {count} times.")
    #If the letter is not in the word
    else:
        print(f"{letter_guess} does not appear.")
    return unguessed_list

def main():
    """
    Main function runs the program. Does not return a value.
    """
    #The maximum amount of guesses a players has before game over.
    MAX_GUESSES = 10

    guess_word_list = [
        "abacus",
        "beaut",
        "candy",
        "steak"
    ]

    #Keeps track of letters that are guessed
    guessed_letters = []
    #Choose the word and start the guess number
    chosen_word = random.choice(guess_word_list)
    guess_number = 0
    #Create list of the unguessed word to create output
    #There are "_"s for every unguessed letter
    unguessed_word = list("_" * len(chosen_word))

    #End the game if word is guessed or guess count matches max guesses
    while guess_number < MAX_GUESSES and "_" in unguessed_word:
        #Print the letters that were guessed correctly
        for letter in unguessed_word:
            print(letter, end="")
        print()
        print(f"Guess number {guess_number + 1} of {MAX_GUESSES}")

        #Checks to see if input is a letter
        #Does not stop until a letter is inputted
        letter_guess = check_is_letter(guessed_letters)
        #Update the unguessed word to include any correct guesses
        unguessed_word = if_letter_in_word(letter_guess, unguessed_word, chosen_word)
        guess_number = guess_number + 1
        guessed_letters.append(letter_guess)
    #If any part of the word is unguessed, game over
    if "_" in unguessed_word:
        print("Game Over.")
    else:
        print("You win!")
    print(f"The word was {chosen_word}.")

#Run main program
main()