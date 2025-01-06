import random
a='''
======================ROCK_PAPER_SCISSOR=============================
'''
print(a)
while True:
    item_list=['rock','paper','scissor']
    user=input("choose the choice =(rock/paper/scissor)")
    computer=random.choice(item_list)

    if user==computer:
        print(f"you and compute are choose same choice")
    elif user=="rock":
        if computer=="paper":
            print(f"paper cover the rock= computer win")
        else:
            print("rock break the scissor==You Win") 
    elif user=="paper":
        if computer=="scissor":
            print("scissor cut the paper==computer win") 
        else:
            print(f"paper cover the rock ==You Win") 
    elif user=="scissor":
        if computer=="rock":
            print("rock break the scissor==computer==computer win")
        else:
            print("scissor cut the paper==You Win")
             
                                        
                    

