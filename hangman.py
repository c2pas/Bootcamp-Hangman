from time import sleep
from random import choice


name = input("Enter your name: ")

print (f"Hello! {name}! Time to play the Hangman!")
print ("Start guessing...")

sleep(1)

words = ("toys", "dolls", "girls", "water", "milk")
word = choice(words)
hint = len(word)
print(f"Word has {hint} letters")

turns = 5

while turns > 0:
    guess = input("Guess the word: ") 

    if guess != word:
        turns -= 1
        if turns == 4:
            sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong answer! You have, {turns}, more guesses!" )

        elif turns == 3:
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong answer! You have, {turns}, more guesses!" )

        elif turns == 2:
           sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print(f"Wrong answer! You have, {turns}, more guesses!" )

        elif turns == 1:
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong answer! You have, {turns}, more guess!" )

        elif turns == 0:
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!")
            break
    else:
        print  ("Congratulations! You guessed the word!") 
        break