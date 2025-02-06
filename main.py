import os
from random import randrange
from art import text2art
from colorama import Fore

fPlayer = {
  1:'''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  ''',

  2:'''
      _______
  ---'    ____)____
            ______)
            _______)
          _______)
  ---.__________)
  ''',

  3:'''
      _______
  ---'   ____)____
            ______)
          __________)
        (____)
  ---.__(___)
  '''
}

fComputer = {
  1:
  '''
      _______
      (____   '---
    (_____)
    (_____)
      (____)
      (___)__.---
  ''',

  2:
  '''
        _______
  ____(____    '---
  (______
  (_______
  (_______
  (__________.---
  ''',

  3: '''
        _______
  ____(____   '---
  (______
  (__________
      (____)
      (___)__.---
  '''
}

replay = True

while replay:
  os.system('clear')
  print(text2art("Jokenpon game!", font="small"))

  player = int(input('''
    Choose between: 
    1> Rock 
    2> Paper 
    3> Scissors
  '''))

  os.system('clear')
  print(text2art("Jokenpon game!", font="small"))

  computer = randrange(1, 4) # 1 = rock, 2 = paper, 3 = scissors

  if player < 1 or player > 3:
    print(Fore.YELLOW + text2art ("Invalid option!", font="small"))
  elif player == computer:
    os.system('clear')
    print(fPlayer[player], end=" ")
    print(fComputer[computer])
    print(Fore.BLUE + text2art("Draw!",font="small"))
  elif \
    (player == 1 and computer == 2) or \
    (player == 2 and computer == 3) or \
    (player == 3 and computer == 1):
    os.system('clear')
    print(fPlayer[player], end=" ")
    print(fComputer[computer])
    print(Fore.RED + text2art("You lose!", font="small"))
  else:
    os.system('clear')
    print(fPlayer[player], end="")
    print(fComputer[computer])
    print(Fore.GREEN + text2art("You win!", font="small"))

  replay = bool(int(input('''
    Replay:
      1> Yes
      0> No
  ''')))