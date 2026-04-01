"""Input helper functions for safe terminal input handling."""


def read_int(prompt):
    """Read and return an integer from user input, or None when invalid."""
    raw_value = input(prompt)
    try:
        return int(raw_value)
    except ValueError:
        return None


def ask_play_again():
    """Ask whether user wants to play again and return True/False."""
    while True:
        answer = input("Vai velies spelet velreiz? (j/n): ").strip().lower()
        if answer == "j":
            return True
        if answer == "n":
            return False
        print("Ludzu ievadi 'j' vai 'n'.")
