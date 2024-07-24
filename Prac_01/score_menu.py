"""Score Menu Program"""

import random

def determine_score_result(score):
    """Determine the result based on the user's score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_valid_score():
    """Get a valid score from the user."""
    while True:
        try:
            score = float(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_result(score):
    """Print the result for the given score."""
    result = determine_score_result(score)
    print(f"Result: {result}")

def show_stars(score):
    """Print stars based on the score."""
    print("*" * int(score))

def main():
    """Main function to execute the program."""
    score = get_valid_score()
    print_result(score)

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
