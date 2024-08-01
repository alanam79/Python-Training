# Code with teacher, also had to debug and fix some errors
# Added the quit statement to allow the code to end if the wrong number was chosen
# Added the quit statement at the end to allow the user to immediately run the code again
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if user_choice >= 3 or user_choice < 0:
    print("You didn't chose a weapon, you lose!")
    quit()
else:
    print(game_images[user_choice])

    #the rest of the code is indented as the if statement ends the code if the wrong number is entered
    #otherise the else statement kicks in an runs the rest of the code
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # if user_choice >= 3 or user_choice < 0:
    #     print("You didn't chose a weapon, you lose!")
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("Its a draw!")
        quit()
