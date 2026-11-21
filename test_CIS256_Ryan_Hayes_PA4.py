# Ryan Hayes
# CIS256 Fall 2026
# Test Programming Assignment 4

import pytest
from CIS256_Ryan_Hayes_PA4 import check_is_letter, if_letter_in_word, main

#Checks to see if letter can equal "a" if "a" is in the guessed letters
def test_check_is_letter():
    assert check_is_letter(["a"]) == "a"

#Checks to see if "a" is in "candy"
def test_if_letter_in_word():
    assert if_letter_in_word("a", ["_", "_", "_", "_", "_"], "candy") == ["_", "a", "_", "_", "_"]

#Checks if main runs
def test_main():
    assert main()