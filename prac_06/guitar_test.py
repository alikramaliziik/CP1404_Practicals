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
from guitar import Guitar

def run_tests():
    # Test data
    name = "Gibson L-5 CES"
    year = 1922
    another_name = "Another Guitar"
    another_year = 2013

    # Expected values
    expected_age_1 = 2024 - year
    expected_age_2 = 2024 - another_year
    expected_is_vintage_1 = True
    expected_is_vintage_2 = False

    # Create guitars
    guitar1 = Guitar(name, year)
    guitar2 = Guitar(another_name, another_year)

    # Test get_age() method
    print(f"{guitar1.name} get_age() - Expected {expected_age_1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age_2}. Got {guitar2.get_age()}")

    # Test is_vintage() method
    print(f"{guitar1.name} is_vintage() - Expected {expected_is_vintage_1}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_is_vintage_2}. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    run_tests()

