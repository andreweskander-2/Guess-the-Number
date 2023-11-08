logo = """ 
 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______  _ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )( )
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|| |
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|| |
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)| |
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (   (_)
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__ _ 
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/(_)
"""                                                    


import random
print (logo)

print("\n\nWelcome to the 'Guess The Number' Game! Let's Get Started?\n")

# Checks if the user input a valid response for the level of difficulty
valid_input_1 = False
while valid_input_1 == False:
  game_level = input("Let's start by defining the level of difficulty.. type 'h' for Hard or 'e' for Easy:\n").lower()
  if game_level == 'h':
    attempts = 4
    valid_input_1 = True
  elif game_level == 'e':
    attempts = 10
    valid_input_1 = True
  else:
    print ("\ninvalid input please try again!\n")

numbers_pool = [*range(0,101)]
random_number = random.choice(numbers_pool)

# Checks if the user input a valid response for the guessed number
valid_input_2 = False
while valid_input_2 == False:
  user_number = int(input("\nPlease enter a guess between 0 and 100: "))
  if user_number not in numbers_pool:
    print(f"\nYour guess of {user_number} is not within the specified range of 1 - 100, please try again!")
  else:
    valid_input_2 = True

# Repeat the part of the code where it asks the user to input their guesses
# untill they run out of attempts 
while attempts != 1:
  attempts -= 1
  
  if user_number > random_number and user_number in numbers_pool:
    print(f"Your guess of {user_number} is too high, try a lower number!")
    print(f"Your left number of attempts is {attempts}!")
  elif user_number < random_number and user_number in numbers_pool:
    print(f"Your guess of {user_number} is too low, try a higher number!")
    print(f"Your left number of attempts is {attempts}!")
  elif user_number == random_number:
    break

  valid_input_3 = False
  while valid_input_3 == False:
    user_number = int(input("\nPlease enter another guess: "))
    if user_number not in numbers_pool:
      print(f"\nYour guess of {user_number} is not within the specified range of 1 - 100, please try again!")
    else:
      valid_input_3 = True

#Decides how the game ends, either a winning message or a good luck message
if user_number == random_number:
  print(f"Your guess of {user_number} is correct! You Win!!")
else:
  print(f"\nYou have consumed all of your available attempts! The correct number was {random_number} Unfortunately you lose!")
  