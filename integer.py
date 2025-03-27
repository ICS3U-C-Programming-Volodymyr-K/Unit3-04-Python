#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 25, 2025
# This program is defines different integers


def main():
    # gets number from the user
    user_number = float(input("Enter the random number please."))
    # Defines constant 0
    ZERO_NUMBER = 0
    # Compares our constant with user number to present message based on it
    if user_number == ZERO_NUMBER:
        print("Your number, {} is equal to zero".format(user_number))
    elif user_number >= ZERO_NUMBER:
        print("Your number, {:.2f} is positive".format(user_number))
        # Represents the negative number answer where it will show that it is negative.
    elif user_number <= ZERO_NUMBER:
        print("Your number, {:.2f} is negative".format(user_number))
        # Creates the display for the case where number is neither bigger or smaller than 0.
    elif user_number == ZERO_NUMBER:
        print("Your number, {} is equal to zero".format(user_number))


if __name__ == "__main__":
    main()
