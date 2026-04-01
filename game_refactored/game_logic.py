"""Core game logic for the guessing game."""

import random

from config import MAX_NUMBER, MIN_NUMBER


def generate_secret_number():
    """Return a random number inside the configured range."""
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def is_guess_in_range(guess):
    """Return True if guess is inside the allowed number range."""
    return MIN_NUMBER <= guess <= MAX_NUMBER


def evaluate_guess(secret_number, guess):
    """Compare guess with secret number and return result key."""
    if guess == secret_number:
        return "correct"
    if guess < secret_number:
        return "low"
    return "high"
