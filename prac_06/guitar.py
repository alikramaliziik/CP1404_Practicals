from guitar import Guitars

def run_tests():
    """Run tests on the Guitar class."""
    # Test data
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    another_name = "Another Guitar"
    another_year = 2013
    another_cost = 1512.9

    # Create guitar instances
    guitar1 = Guitar(name, year, cost)
    guitar2 = Guitar(another_name, another_year, another_cost)

    # Test get_age() method
    expected_age_1 = 2024 - year
    expected_age_2 = 2024 - another_year

    print(f"{guitar1.name} get_age() - Expected {expected_age_1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age_2}. Got {guitar2.get_age()}")

    # Test is_vintage() method
    expected_is_vintage_1 = True
    expected_is_vintage_2 = False

    print(f"{guitar1.name} is_vintage() - Expected {expected_is_vintage_1}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_is_vintage_2}. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    run_tests()
