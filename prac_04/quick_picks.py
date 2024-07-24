import random

MIN_NUM = 1
MAX_NUM = 45
NUM_PICKS = 6


def generate_quick_pick():
    """Generate a single quick pick."""
    quick_pick = []
    while len(quick_pick) < NUM_PICKS:
        number = random.randint(MIN_NUM, MAX_NUM)
        if number not in quick_pick:
            quick_pick.append(number)
    return sorted(quick_pick)


def main():
    num_quick_picks = int(input("How many quick picks? "))

    for i in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join("{:2}".format(number) for number in quick_pick))


if __name__ == "__main__":
    main()
