#!/usr/local/bin/ python3
import os

# say welcome to hangman
print("Welcome to Hangman!")

class Player():
    name = ""
    word = ""
    enterALetter = ""

while True: 
    # Let host enter their name
    host = Player()
    host.name = input("Enter game host: ")

    # Let player enter their name
    guesser = Player()
    guesser.name = input("Enter player name: ")

    # Say welcome to the players
    print("\n""This game is hosted by " + host.name + " and the contestant is " + guesser.name + "!" + "\n")

    # Choose a word
    word = input(host.name + ", " + "Write a word: ")
    word = word.lower()

    # clear screen
    os.system('clear')

    # Show the underscores accroding to the length of the word 
    wordLength = word.__len__()
    progress = "*" * wordLength
        
    # Display a total guess time!
    print("\t***********************************************")
    print("\t  Hi " + guesser.name + ", " + "In total,you have 9 erros can make. ")
    print("\t***********************************************")
    print("\n\n""Current State: " + progress + "\n")

    # Save guessed letters
    guessed_letters = []



    errorCount = 0 
    while True:
        enterALetter = input("\n" + guesser.name + ", " + "Enter a letter: ")
        enterALetter = enterALetter.lower()
        print(enterALetter.lower())
        guessed_letters.append(enterALetter.lower())
        print("The letters you have guessed: " + ', '.join(guessed_letters))
    
        # Check if the word contains the guess letter
        if word.find(enterALetter) != -1:
            # Find the position, replace the underscore with the letter
            occurrences = word.find(enterALetter)
            indices = [i for i,  a in enumerate(word) if a == enterALetter]
            # Print(indices)??
            
            tmp_progress = list(progress)
            for index in indices:
                tmp_progress[index] = enterALetter

            progress = "".join(tmp_progress)
            print("CURRENT STATE: " + progress)
            print("NUMBER OF ERRORS: " + str(errorCount))

            if progress.find("*") == -1:
                print("You won!")
                break
            

        else:
            errorCount += 1
            print("\n""Opps,no "  + enterALetter + " in the word. Keep going!""\n")
            print("NUMBER OF ERRORS: " + str(errorCount))
            if errorCount == 9:
                print("\n""You have reached the total missing times, Game Over!")
                break
                
    choice = input("Press q to quit the game. Press anything to start again.")
    
    if choice == "q":
        break
    # elif choice == "":
    #     print("Welcome to Hangman!")
                



   


         













