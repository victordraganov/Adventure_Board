import random

"""
    This module contains all functions related to luck, probabilities, etc...
"""


# CONSTANTS:

# The denominator of the bonus turn probability.
BONUS_TURN_CNANCE = 16


def roll_die():
    """Rolls a single die of fate. Score is between 0 and 5 (including)."""
    return random.randint(0, 5)


def roll_dice():
    """
        Rolls the two dices of fate. returns tuple (sum, pair) which contains the
        sum of the two and a boolean "pair" which indicates if they are pares.
    """
    die_1 = roll_die()
    die_2 = roll_die()
    pair = die_1 == die_2
    return (die_1 + die_2, pair)


def bonus_turn(luck):
    """
        The player has 1/luck chance to play one bonus turn when in battle.
        Returns 0 or 1.
    """
    number = random.randint(0, BONUS_TURN_CNANCE - luck)
    return number == 0

