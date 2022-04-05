#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tells if you are approved by a grandmother


def main():
    # this function calculates if you are approved by a grandmother

    # input
    age_number_string = input("Enter your age:")

    # procces and output
    try:
        age_number = int(age_number_string)
        if age_number >= 25 and age_number <= 40:
            print("You are approved")
        else:
            print("You are not approved")
    except Exception:
        print("Please input an integer")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
