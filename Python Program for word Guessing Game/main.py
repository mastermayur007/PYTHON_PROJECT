import random

name = input("What is your name? ")
print(f"Welcome {name}, best of luck")

words = ["mayur", 'master', 'kamala', 'kajal', 'kalyani', 'kanchan', 'kishor', 'sajan', 'sapana', 'samay']
word = random.choice(words)

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    if failed == 0:
        print("\nYou win!")
        print(f"The word is {word}")
        break

    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print(f"Wrong guess. You have {turns} more guesses.")

    if turns == 0:
        print("You lose.")
        print(f"The word was {word}")           