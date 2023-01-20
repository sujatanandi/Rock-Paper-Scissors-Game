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


rps_list = [rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice>=3 or choice<0 :
  print("You typed an invalid number ,You lose!")
else:
  print(rps_list[choice])
  ran_choice = random.randint(0,2)
  print("Computer chose:\n")
  print(rps_list[ran_choice])
  
  if choice == 0 and ran_choice == 2:
    print("You win!")
  elif ran_choice == 0 and choice == 2:
    print("You lose!")
  elif ran_choice > choice:
    print("You lose!")
  elif choice > ran_choice:
    print("You win!")
  elif ran_choice == choice:
    print("It's a Draw!")
  
