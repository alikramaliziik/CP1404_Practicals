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
