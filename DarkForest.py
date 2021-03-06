#darkforest console game
#Created by Christos Mappouras

from sys import exit

def start():
    print("""
        Welcome to the dark forest
        You must find all the correct answers to reach 10points
        Once you reach 10points you will get out alive from the dark forest
        Be careful! You have only 1 chance to answer!
        See you on the other side.
    """)

    points = 0;
    print(f"\nCurrent points: {points}")

    username = input("Type your Username: ")

    # QUESTION: 1
    print(f"\nHello {username},")
    print("Let's Begin, Shall we?")
    q1 = input("> ")
    if q1 == "yes":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 2nd question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 2
    print("\n\nDid you ever tried vodka?")
    q1 = input("> ")
    if q1 == "yes":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 3rd question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 3
    print("\n\nWhat is the result of 5x6?")
    q1 = input("> ")
    if q1 == "30":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 4th question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 4
    print("\n\nWhat is the result of 111 (binary to decimal system)?")
    q1 = input("> ")
    if q1 == "7":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 5th question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 5
    print("\n\nWhat is the result of 64 (decimal to octal system)?")
    q1 = input("> ")
    if q1 == "100":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 6th question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 6
    print("\n\nWhat is the result of 420 (hexadecimal to decimal system)?")
    q1 = input("> ")
    if q1 == "1056":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 7th question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 7
    print("\n\nWhat is the result of 999 (decimal to hexadecimal system)?")
    q1 = input("> ")
    if q1 == "3E7":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 8th question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 8
    print("\n\nWhat is the result of 1567 (decimal to binary system)?")
    q1 = input("> ")
    if q1 == "11000011111":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the 9th question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 9
    print("\n\nWhat is the opposite of good? (Think like Cindy Sheeran)")
    q1 = input("> ")
    if q1 == "apathy":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        print("\nLets move to the final question")
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

    # QUESTION: 10
    print("\n\nAlways think ...... the box?")
    q1 = input("> ")
    if q1 == "outside":
        print("\nGood!")
        points += 1;
        print(f"Current points: {points}")

        class color:
            PURPLE = '\033[95m'
            CYAN = '\033[96m'
            DARKCYAN = '\033[36m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m'

        print(color.BOLD + "\n\n\nCONGRATULATION! You made it out alive!\n\n\n\n" + color.END)
        print("Made by Chris Mappouras")
        exit(0)
    else:
        print("\nI HATE YOU")
        print("Come on, You died...\n")
        exit(0)

start()

