user=str(input('what is your name? '))
user_num = int(input("Enter the number between 0-50 "))
import random
py_num=random.randint(0,50)
lives=5
while lives>0:
    if user_num==py_num:
        print('congrats {} !,you have won the game '.format(user)) 
        break 
    elif user_num>py_num:
        print('Hint-choose a smaller number ')
        user_num=int(input('Guess the number again '))
    else :
        print('Hint-choose a larger number')
        user_num=int(input('Guess the number again '))
    lives = lives-1
if user_num == py_num:
    print("congrats {} you have won the match ".format(user))
    exit()

if lives==0:
    print('sorry {}, you have lost the game, try again '.format(user))
    print("correct number was{}" .format(py_num))
