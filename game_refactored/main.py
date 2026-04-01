"""Entry point for the refactored guessing game."""

from config import MAX_ATTEMPTS, MAX_NUMBER, MIN_NUMBER
from game_logic import evaluate_guess, generate_secret_number, is_guess_in_range
from input_utils import ask_play_again, read_int


def play_one_game():
    """Play one game session and return when game ends."""
    secret_number = generate_secret_number()
    attempts = 0

    print("\nLaipni lugts minesanas spele!")
    print(f"Uzmini skaitli no {MIN_NUMBER} lidz {MAX_NUMBER}.")
    print(f"Tev ir {MAX_ATTEMPTS} meginajumi.\n")

    while attempts < MAX_ATTEMPTS:
        guess = read_int(f"Tavs minejums ({MAX_ATTEMPTS - attempts} palikusi): ")

        if guess is None:
            print("Kluda: jaievada vesels skaitlis!")
            continue

        if not is_guess_in_range(guess):
            print(f"Skaitlim jabut no {MIN_NUMBER} lidz {MAX_NUMBER}!")
            continue

        attempts += 1
        result = evaluate_guess(secret_number, guess)

        if result == "correct":
            print(f"\nPareizi! Skaitlis bija {secret_number}.")
            print(f"Tev bija nepieciesami {attempts} meginajumi.\n")
            return

        if result == "low":
            print("Par mazu! Megini lielaku skaitli.")
        else:
            print("Par lielu! Megini mazaku skaitli.")

    print("\nBeidzies meginajumu skaits!")
    print(f"Pareiza atbilde bija: {secret_number}\n")


def main():
    """Keep running games until user chooses to quit."""
    while True:
        play_one_game()
        if not ask_play_again():
            print("\nPaldies par spelesanu! Uz redzesanos!")
            break


if __name__ == "__main__":
    main()
