# ROCK PAPER SCISSORS GAME

import os
from random import choice
import sys

from moves import Rock, Paper, Scissors


class Game:
    def __init__(self, player, rounds=3):
        self.rounds = rounds
        self.player = player
        self.score = [0, 0]

    def _convert_move(self, move):
        """Returns a Rock, Paper, or Scissors class"""
        if move == 'r':
            return Rock()
        elif move == 'p':
            return Paper()
        elif move == 's':
            return Scissors()

    def summary(self, title):
        """Gives a score summary of the game at the end of each round"""
        print("\n{}".format(title))
        print("-"*len(title))
        print("{}: {}".format(self.player, self.score[0]))
        print("Computer: {}".format(self.score[1]))
        print("-"*len(title))
        print("\n")

    def get_move(self, move=None):
        """Returns the players move"""
        move = move or input("[R]ock, [P]aper, [S]cissors? ").lower()
        if move == 'q':
            print("Bye!")
            sys.exit()
        elif move not in list('rps'):
            return self.get_choice()
        return self._convert_move(move)

    def game_round(self):
        """Goes through a round of the game"""
        player_move = self.get_move()
        computer_move = self._convert_move(choice(list('rps'))) # Random choice for computer
        print("\n")
        print("Computer chose {}".format(computer_move.__class__.__name__))
        # Player Wins
        if player_move > computer_move: # Calls dunder method
            self.score[0] += 1
            print("\nYou won that round, {}!".format(self.player))
        # Computer Wins
        elif computer_move > player_move: # Calls dunder method
            self.score[1] += 1
            print("\nYou lost that round, {}!".format(self.player))
        # Draw
        else:
            print("\nYou tied!")
        self.summary("Current score")

    def game_over(self):
        """Display whether or not you won the game"""
        if self.score[0] > self.score[1]:
            print("Congratulations {}! You won the game!".format(self.player))
        else:
            print("Sorry {}. You just weren't good enough!".format(self.player))

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    game = Game(player = input("What's your name? "))

    while 3 not in game.score:
        game.game_round()
    else:
        game.game_over()