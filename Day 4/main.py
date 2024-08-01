# My solution to the Rock Paper Scissors game.

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
import random
user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

computer_choice = random.randint(0, 2)

if user_choice == 0:
  print(rock)
elif user_choice == 1:
   print(paper)
elif user_choice == 2:
   print(scissors)
else:
    print("Invalid choice. Please select 0, 1, or 2. Try again!")

if computer_choice == 0:
    print(f"Computer chose:\n{rock}")

if computer_choice == 1:
    print(f"Computer chose:\n{paper}")

if computer_choice == 2:
    print(f"Computer chose:\n{scissors}")

# rock
if user_choice == 0 and computer_choice == 0:
    print("You have tied! Try again!")
elif user_choice == 0 and computer_choice == 1:
    print("You have lost! Try again!")
elif user_choice == 0 and computer_choice == 2:
    print("You have won! Congratulations!")

# paper
if user_choice == 1 and computer_choice == 1:
    print("You have tied! Try again!")
elif user_choice == 1 and computer_choice == 2:
    print("You have lost! Try again!")
elif user_choice == 1 and computer_choice == 0:
    print("You have won! Congratulations!")

# scissors
if user_choice == 2 and computer_choice == 2:
    print("You have tied! Try again!")
elif user_choice == 2 and computer_choice == 0:
    print("You have lost! Try again!")
elif user_choice == 2 and computer_choice == 1:
    print("You have won! Congratulations!")
