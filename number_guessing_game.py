#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program is a game where the user tries to guess a randomly
#   generated number and will not crash


import random


def main():
    # This function tells the user if their guess is correct

    # Input
    integer_as_string = input("Guess what the integer between 0 and 10 is: ")
    print("")

    # Process & Output
    correct_number = random.randint(0, 10)
    try:
        integer_as_number = int(integer_as_string)

        if integer_as_number == correct_number:
            print("You guessed it!")
        else:
            print("Incorrect! The number was {}.".format(correct_number))
    except Exception:
        print("{} is not an integer.".format(integer_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
