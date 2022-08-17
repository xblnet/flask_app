from numpy import random

element = ['Sissor', 'Rock','Paper']

#input from user
user = int(input("Please enter your action: 0. Sissor, 1. Rock, 2. Paper: "))
robot = element[random.randint(2)]
print("you have enter: ", element[user], "and robot is: ", robot)
if(user<=2):
    if(element[user] == robot):
        print("draw")
    elif(element[user] == "Sissor"):
        if(robot =="Paper"):
            print("You have winned!")
        else:
            print("You have losed!")

    elif(element[user] == "Rock"):
        if(robot =="Sissor"):
            print("You have winned!")
        else:
            print("You have losed!")

    elif(element[user] == "Paper"):
        if(robot =="Rock"):
            print("You have winned!")
        else:
            print("You have losed!")
        
else:
    print("You have enter out of scoop!")

