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

rps = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if 0 <= user_input <= 2:
    print(rps[user_input])

    compChoice = random.randint(0, 2)

    compChoiceASCII = rps[compChoice]

    print(f"Computer chose: {compChoice}\n" + compChoiceASCII)

    if user_input == compChoice:
        print("It's a draw!")
    elif (user_input == 0 and compChoice == 2) or (user_input == 1 and compChoice == 0) or (user_input == 2 and compChoice == 1):
        print("You Win!")
    elif (user_input == 0 and compChoice == 1) or (user_input == 1 and compChoice == 2) or (user_input == 2 and compChoice == 0):
        print("You lose!")
    else:
        print("Something went wrong!")

else:
    print("Wrong input. You lose!")
