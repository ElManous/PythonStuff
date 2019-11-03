# ##################
# author: minatawfik
# date: 2019-04-18
#
# OMIS 30
# Spring 2019
# Class 7
# Temperature Converter between miles and kilometers
##########

# Ask the user for which scale they are going to start with?
print('Are you starting with miles or kilometers?')
print('Acceptable inputs are: ')
acceptable_user_scale_inputs = ['m','M','miles','Miles','km','KM','k','K','Kilometers','kilometers']
print(acceptable_user_scale_inputs)
starting_scale = input()



# If they did not, print out a statement telling them they did not do so and then quit out of the program.
# If they did, then continue with the rest of the program.
if starting_scale in acceptable_user_scale_inputs:
    print('you did good, you can move on')
else:
    print('you messed up')
    quit()

# Ask user for distance in the above scale
print('What is your starting distance in ' + starting_scale + '?')
print('please enter it in a float format:')
starting_distance = input()


# Check to make sure that the user entered a valid distance.  

acceptable_user_input = float
print(type(starting_distance))
print(type(float(starting_distance)))

if type(float(starting_distance)) is float:
   print('you did good')
elif type(float(starting_distance)) is str:
   print('you messed up. sucks to be you.')
   quit()

print('here you go')



#print result

if starting_scale[0] == 'm' or starting_scale[0] == 'M':
    KM = 1.6 * float(starting_distance)
    print(starting_distance  + ' miles ' + ' is equal to ' + (str(round(KM,1))) + ' in kilometers ')
elif starting_scale[0] == 'k' or starting_scale == 'K':
    M = float(starting_distance)/1.6
    print(starting_distance  + ' kilometers ' + ' is equal to ' + (str(round(M,1))) + ' in miles ')
else:
    print('you failed')




