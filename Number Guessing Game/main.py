import random

def number_guessing():
    print("========WELCOME TO THE NUMBER GUESSING GAME==========") 
    print("========PLIZ CHOOSE THE CORRECT NUMBER TO WIN THE GAME=========")
    
    guess_number=random.randint(1,100)
    attemp=0
    
    while True:
        try:
            guess=int(input("enter the guess:"))
            attemp+=1  
            
            if guess<guess_number:
                print(f"the number you choose is lower ")  
            
            elif guess>guess_number:
                print("the number you choose is bigger ")
             
            else:
                print("congrast you choose the write number ")
        except ValueError:
            print("pliz chooose the correct value and try again")

if __name__=="__main__":
    number_guessing()                              