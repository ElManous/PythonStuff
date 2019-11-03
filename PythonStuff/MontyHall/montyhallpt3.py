# Monty Hall game Pt 3 by Mina Tawfik
############################################


import random

# ask user for # of doors
print('Enter how many doors you want to play with')

# check whether user input is valid
cont = True
while (cont):
    doors = input()
    try:
        doors = int(doors)
        if (doors >= 3):
            cont = False
        else:
            print('Please select an integer greater than or equal to 3')  
    except:
        print('Please select an integer greater than or equal to 3')



# ask user how many times they want to play
print('How many powers of 10 would you like to run the simulation for?')

# check whether user input is valid
cont = True
while (cont):
    m = input()
    try:
        m = int(m)
        m = 10**m # makes m to the power of 10 
        cont = False
    except:
        print('Please select an integer')



# simulation
switch_wins = 0

for _ in range(m):
    # assign prize
    prize = random.randint(1,doors)

    # player's choice of which door
    pick = random.randint(1,doors)

    if prize != pick:
        switch_wins += 1

print('You would have won ' + str(switch_wins/m * 100)[0:5] + '% of the time if you switched')

# show how many times you would win if you stayed
stay_wins = m - switch_wins

print('You would have won ' + str(stay_wins/m * 100)[0:5] + '% of the time if you stayed')