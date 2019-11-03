###### Monty Hall Game pt2 by Mina Tawfik
######################################################

import random

#Ask player which door he/she initially wants
print('Which door would you like to choose? A, B, or C?:')
acceptable_doors = ['A','B','C']
doors = ['A','B','C']


# randomly assign prize to a door
prize = random.choice(doors)

cont = True
while (cont):
    firstchoice = input()
    if firstchoice in acceptable_doors:
        print('You chose ' + firstchoice)
        cont = False
    else:
        print('You messed, please choose door A, B, or C')


# randomly assign goats to other doors
goat = random.choice(doors)
while goat == prize or goat == firstchoice:
    goat = random.choice(doors)

doors.remove(goat)

#Reveal one of the doors
print('Now I will show you one of the doors that has a goat inside of it...')
print('Door ' + goat + ' has a goat inside of it!')


secondchoice = random.choice(doors)
while secondchoice == firstchoice or secondchoice == goat:
    secondchoice = random.choice(doors)

#Ask if the player wants to change doors
print('Now that you know the contents of door ' + goat + ', do you want to change to door ' + secondchoice + ' or keep door ' + firstchoice + '?')
updated_acceptable_choices = [firstchoice, secondchoice]
print('Please choose either door ' + secondchoice + ' or ' +  firstchoice)


#Reveal whether the player won or lost
cont = True
while(cont):
    answer = input()
    if answer in updated_acceptable_choices:
        if answer == prize:
            print('You just won a new Ferrari!')
        else:
            print('There is a goat behind that door!')
        cont = False
    else:
        print('You messed up, please choose ' + secondchoice + ' or ' + firstchoice)
        



