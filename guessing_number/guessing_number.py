# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:12:31 2022

@author: LUCIANOGARIM
"""
import random
from art import logo

def new_guess(chances):
  if chances == 0:
    return
  else:
    print(f"You have {chances} attempts to guess the number. \n")
    guess = int(input("Make a guess \n "))
    return guess

def guess_mensage(chances):
  if chances>0:
    print("Guess again")
  else:
    print("You have no more attempts. You Lose!")

def guess_function(chances):
  """This function tells if the number guessed is greater or lower than a number choosen by the computer"""
  while chances>0:
    guess = new_guess(chances)
    if guess>correct_number:
      print("Too high. \n")
      chances -=1
      guess_mensage(chances)
    elif guess<correct_number:
      print("Too low.")
      chances -=1
      guess_mensage(chances)
    else:
      print(f"You got it! The answer is {correct_number} ")
      return
  
print(logo)
print("Welcome to the Number Guessing Game! \n")
print("I'm thinking of a number between 1 and 100. \n")
level = input("Choose a difficulty. Type 'easy' or 'hard' \n")

correct_number = random.randint(1,100)

if level=='easy':
  chances = 10
  guess_function(chances)
elif level == 'hard':
  chances = 5
  guess_function(chances)