import random
list = ['rock','paper','scissors']
user_score = 0
comp_score =0

while True:
    print('''
--------- This is Rock Paper Scissor-game  ----------------
TYPE   ::       Rock - Paper - Scissors    :: only:)         
        ''')
    comp = random.choice(list)
    # Taking input from user 
    print("Enter your choice")
    user=''
    while user not in list:
        user = input().lower()
    

    # logic
    if user ==comp:
        print("\tDRAW")

    # user winning cases --
    elif user == 'paper' and comp =='rock':
        print('\tYOU WIN')
        user_score+=1
    elif user == 'rock' and comp =='scissors':
        print('\tYOU WIN')
        user_score+=1
    elif user == 'scissors' and comp =='paper':
        print('\tYOU WIN')
        user_score+=1

    # computer winning cases ---
    elif user == 'scissors' and comp =='rock':
        print('\tYOU LOSE')
        comp_score+=1
    elif user == 'rock' and comp =='paper':
        print('\tYOU LOSE')
        comp_score+=1
    elif user == 'paper' and comp =='scissors':
        print('\tYOU LOSE')
        comp_score+=1  

    else:
        print("It is not possible hahaha ......") 



    # printing the input of user or computer 
    print(f"\nYour choice was '{user.capitalize()}' and computer's choice was '{comp.capitalize()}'. ")

    # aksing user to play again 
    print("Do you want to play again : ")
    if not input().lower().startswith('y'):
        break

print(f"User total score : {user_score}\nComputer total score : {comp_score}")
print("\n\n *Thank you for playing this game ***")