# -*- coding: utf-8 -*-
"""
Guessing Game
Created on Sat Feb  6 17:40:39 2021

@author: madig
"""
import random

#%%
def main():
    score = 100
    prize = random.randint(1, 101);
    while(True):
            try:
                print("Guess a random number!  Score:",score)
                guess = int(input())
                if guess > prize:
                    print("Too high!  Minus 5 points!")         
                elif guess < prize:
                    print("Too low!  Minus 5 points!")
                elif guess == prize:
                    print("You WIN! Your score is",score)
                    break
                score = score - 5
            except TypeError:
                print("Enter an integer dummy...")
                continue
            
#%%
if __name__ == '__main__':
    main()
            
            
    
    