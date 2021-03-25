import random
from os import system
import sys
import os
import json
import turtle

def screen_clear():
    # for linux and Mac
    if os.name == 'posix':
      _ = os.system('clear')
    else:
    # for windows platfrom
      _ = os.system('cls')

def start():
    choice = input("Do you want to start? (Y)es/(N)o. \n")
    choice = choice.upper()
    if choice == 'YES':
        input("\n Ok, lets go! Press ENTER. . .\n")
        screen_clear()
    else:
        print("Okay, good bye!")
        sys.exit()

def select_type():
    screen_clear()
    print("Select the category of words what you want")
    tpe = input("\n 1 > Colors \n 2 > Animals \n 3 > Fruits \n 4 > Sports\n\n")
    
    file_name = None
    list_type = None

    while True:
        if tpe == '1':
            file_name = 'colors.txt'
            break
        elif tpe == '2':
            file_name = 'animals.txt'  
            break
        elif tpe == '3':
            file_name = 'fruits.txt'           
            break
        elif tpe == '4':
            file_name = 'sports.txt'           
            break
        else:
            sys.exit()
    screen_clear()
    return file_name

def set_type(file_name):
    data_dir = os.path.join(os.path.dirname(__file__))
    file_loc = os.path.join(data_dir,file_name)
    word_list = open(file_loc).read().splitlines()

    return word_list

def display_hang(attempts):
    stages = [# head, body, arms and legs: dead.
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / ∖
                   -
                """,
                # head, body e arms, leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, body e arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, body e arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head e body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # start
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    return stages[attempts]

def play(word_list):
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    word = random.choice(word_list)
    word_len = len(word)
    space = "︿"
    word_completion = (space* word_len)    
    stages = display_hang(attempts)
    
    print(stages)
    print(f"Tip: {word_len} letters!\n")
    print(word_completion)
    ##print(word)

    while not guessed and attempts > 0:
        guess = input("Say one letter...!")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You just said that...")
            elif guess not in word:
                print("Wrong.... =(")
                attempts -= 1
                guessed_letters.append(guess)

            else:
                print("It is on word!!!")
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]

                for index in indexes:
                    word_as_list[index] = guess
                
                word_completion = "".join(word_as_list)
                
                if "︿" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You just tried " , guess)
            elif guess != word:
                print("Isnt the word...")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid!")

        screen_clear()
        print(display_hang(attempts))
        print(word_completion)
        print("\n")
        print(f"Attempts left: {attempts}")
    
    if guessed:
        screen_clear()
        print("\n\nWoow, you win!!!! \n\n")

    else:
        print(f"You lost =( \n The word is {word}")

def main():
    start()
    word_type = select_type()
    word_list = set_type(word_type)
    attempts = play(word_list)


if __name__ == "__main__":
    main()


