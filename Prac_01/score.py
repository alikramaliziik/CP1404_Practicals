"""Score Program"""
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

def main():
    """Main function to execute the score program."""
    score = float(input("Enter your score: "))
    result = determine_score_result(score)
    print(result)

    # Generate a random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    random_result = determine_score_result(random_score)
    print(f"Result for random score: {random_result}")

if __name__ == "__main__":
    main()
