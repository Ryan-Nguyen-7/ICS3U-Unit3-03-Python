#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program asks the user to guess a random number
#   between 1 and 10


import random


def main():
    # This function generates a random number
    #   and asks the user to guess it

    # generates random number between 1 and 10
    random_number = random.randint(1, 10)

    # input
    guess = int(input("Enter guess: "))
    print("")

    # process
    if random_number == guess:

    # output
        print("Correct!")
    else:
        print("The correct answer was {}".format(random_number))


if __name__ == "__main__":
    main()
