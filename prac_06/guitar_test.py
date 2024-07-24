from guitar import Guitar

def main():
    """Test the Guitar class methods get_age and is_vintage."""

    # Create guitar instances
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1512.9)

    # Test get_age method
    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")

    # Test is_vintage method
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

if __name__ == "__main__":
    main()

#output
Gibson L-5 CES get_age() - Expected 102. Got 102
Another Guitar get_age() - Expected 11. Got 11
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False

#update
from guitar import Guitar

def main():
    """Test the Guitar class methods get_age and is_vintage."""

    # Create guitar instances
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1512.9)

    # Test get_age method
    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")

    # Test is_vintage method
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

if __name__ == "__main__":
    main()
#to run the file
python guitar_test.py
#output
Gibson L-5 CES get_age() - Expected 102. Got 102
Another Guitar get_age() - Expected 11. Got 11
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
