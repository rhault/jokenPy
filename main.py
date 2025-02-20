import os
import csv
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import random
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

with open("scores.csv", "r") as scoresFile:
  csv_scores = csv.DictReader(scoresFile)
  fieldnames = csv_scores.fieldnames
  rows = list(csv_scores)
  lenght = len(rows)
  lastGame = rows[-1] if lenght > 1 else 0
  numberGame = int(lastGame['n']) + 1

### Computer Class ###
class Computer:
  def __init__(self, name):
    self.name = name
    self.scores = {
      "won": 0,
      "lost": 0,
      "draw": 0
    }

  def showScore(self):
    print(self.scores)

  def newScore(self, score):
    key = [*score.keys()][0]
    self.scores[key] += 1

  def saveScoresFile(self, player, score):
    with open("scores.csv", "a", newline='') as saveScoreFile:
      csv_saveScore = csv.DictWriter(saveScoreFile, fieldnames= fieldnames)
      row = {**{'n': numberGame,'name':player}, **score}
      csv_saveScore.writerow(row)

  def showScore(self):
    print(f'''
      Player: {self.name}
      Score: {self.scores}
    ''')
    self.saveScoresFile(self.name, self.scores)

### Player Class ###
class Player(Computer):
  def __init__(self, name):
    super().__init__(name)

  def setName(self, name):
      self.name = name

  def entry(self):
    try:
      entryPlayer = inquirer.select(
        message= "Choose between:",
        choices= [
          Choice(value=1, name='Rock'), 
          Choice(value=2, name='Paper'), 
          Choice(value=3, name='Scissors')
        ]
      ).execute()

      return entryPlayer
    except ValueError:
      os.system('clear')
      print("Invalid input. Please enter a number between 1 and 3.")

### Game Class ###
class jokenPy:
  def __init__(self, player):
    self.player = player
  
  def play(self):
    computer = random.randint(1, 3) # 1 = rock, 2 = paper, 3 = scissors
    scorePlayer = {"lost": 0}
    scoreComputer = {"lost": 0}
    
    if self.player < 1 or self.player > 3:
      print(Fore.YELLOW + text2art ("Invalid option!", font="small"))
    elif self.player == computer:
      os.system('clear')
      print(fPlayer[self.player], end=" ")
      print(fComputer[computer])
      print(Fore.BLUE + text2art("Draw!",font="small"))
      scorePlayer = {"draw": 1}
      scoreComputer = {"draw": 1}
    elif \
      (self.player == 1 and computer == 2) or \
      (self.player == 2 and computer == 3) or \
      (self.player == 3 and computer == 1):
      os.system('clear')
      print(fPlayer[self.player], end=" ")
      print(fComputer[computer])
      print(Fore.RED + text2art("You lose!", font="small"))
      scorePlayer = {"lost": 1}
      scoreComputer = {"won": 1}
    else:
      os.system('clear')
      print(fPlayer[self.player], end="")
      print(fComputer[computer])
      print(Fore.GREEN + text2art("You win!", font="small"))
      scorePlayer = {"won": 1}
      scoreComputer = {"lost": 1}

    return {
      "player": scorePlayer, 
      "computer": scoreComputer
    }
  
  def score(self):
    pass


def start():
  os.system('clear')
  print(text2art("Jokenpon game!", font="small"))
  namePlayer = inquirer.text(message="Insert player name:").execute()
  
  replay = True
  player11 = Player(namePlayer)
  computer = Computer('Computer')

  while replay:
    os.system('clear')
    print(text2art("Jokenpon game!", font="small"))

    entryPlayer = player11.entry()
    newGame = jokenPy(entryPlayer)
    scores = newGame.play()
    player11.newScore(scores['player'])
    computer.newScore(scores['computer'])

    try:
      replay = inquirer.select(
          message= "Replay:",
          choices= [
            Choice(value=True, name='Yes'), 
            Choice(value=False, name='No')
          ]
      ).execute()
    except:
      replay = False

  os.system('clear')
  player11.showScore()
  computer.showScore()

start()
