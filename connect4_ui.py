# connect4_ui.py
#
# ICS 32 
# Project #2
#
# This module contains utility functions that can be called from a console-
# based UI for a Connect Four game.
# 
# The signatures for the four required functions are provided.
# Hint: It would be useful to create helper functions.

import connect4

DROP = 1
POP = 2


def make_new_game() -> connect4.GameState:
    '''Asks the user for a board size, then creates a new game and return connect4.GameState'''
    pass

def print_board(state: connect4.GameState) -> str:
    '''Returns a string holding the contents of a game board, given a GameState'''

    pass

def choose_move(state: connect4.GameState) -> tuple[int, int]:
    '''
    Asks the user to choose a move, returning a tuple whose first element
    is DROP or POP and whose second element is a valid column number.
    '''
    pass


def make_move(state: connect4.GameState, move: tuple[int, int]) -> connect4.GameState:
    '''
    Makes the given move against the given state, returning the new state.
    For a valid move, return new state.
    
    Raise connect4.InvalidMoveError if invalid operation detected.
    Implement exception handler to catch this exceptions.
    If connect4.InvalidMoveError exception is caught, return original state inside the exception handler.
    '''

    pass
