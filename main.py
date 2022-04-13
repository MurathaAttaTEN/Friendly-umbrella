from unicodedata import name


name = input("Type your name:")
print("Welcome",name,"to this adventure!")

answer = input(
    "You are on a dirty road,it has come to an end and you can go left or right"
 ).lower()

if answer == "left":
    answer = input("You come to a river,you can walk around or swim innit:")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles,ran out of water and lost the game.")
    else:
        print('Not a valid option.You lose.')
elif answer == "right":
    print()
else:
    print('Not a valid option.You lose')

         