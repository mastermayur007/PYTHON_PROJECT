import random

words=['python','java','javascript','jquery','html','css','pandas']

chosen_word=random.choice(words)
word_display=['_' for _ in chosen_word]
attempt=8

print("WELCOME TO HAGMAN_GAME")

while attempt>0 and '_' in word_display:
    print('\n'+' '.join(word_display))
    guess=input("Guess the letter:").lower()
    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if letter==guess:
                word_display[index]=guess
    else:
        print("That word doesent apper in the word idiot...")
        attempt-=1
        
if '_' not in word_display:
    print("You guess the word:") 
    print(' '.join(word_display))
    print("you sirvived")
else:
    print("You run out of attempt .The word was: ",chosen_word) 
    print("You lost")              