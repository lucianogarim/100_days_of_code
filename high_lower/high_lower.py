# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:58:42 2022

@author: LUCIANOGARIM
"""
from game_data import data
from art import logo,vs
from random import randint
import os

def people(data):
  """This function prints two people, including their native country and what they do."""
  first = data[randint(0,len(data)-1)]
  print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']} \n")
  print(vs)
  second = data[randint(0,len(data)-1)]
  print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']} \n")
  return first, second

def compare(first, second):
  """This function compare the number of followers from these two people."""
  if first['follower_count']>second['follower_count']:
    higher = 'A'
  else:
    higher = 'B'
  return higher
  
def scores(higher, score, game_over):
  """This function calculate the score"""
  if more_followers == higher:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    game_over = False
  return score, game_over


score = 0
game_over = True
while game_over==True:
  print(logo)
  first, second = people(data)
  more_followers = input("Who has more followers? Type 'A' or 'B': \n")
  os.system('cls')
  higher = compare(first, second)
  score, game_over = scores(higher, score, game_over)
  

