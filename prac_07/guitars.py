import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display the details of each guitar in the list."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def main():
    """Main function to load, sort, and display guitars."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    display_guitars(guitars)


if __name__ == "__main__":
    main()


#ask users to enter guitar
import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display the details of each guitar in the list."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def add_new_guitars(guitars):
    """Prompt the user to enter details of new guitars and add them to the list."""
    print("Enter new guitars. Leave the name blank to stop.")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")


def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Main function to load, add new guitars, sort, display, and save guitars."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    # Add new guitars from user input
    add_new_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    display_guitars(guitars)

    # Save all guitars to the CSV file
    save_guitars(filename, guitars)


if __name__ == "__main__":
    main()


#guitar_test.py
import csv
from guitar import Guitar
from guitars import load_guitars, display_guitars, add_new_guitars, save_guitars

def test_load_guitars():
    """Test loading guitars from the CSV file."""
    guitars = load_guitars('guitars.csv')
    assert len(guitars) == 6  # Assuming the file initially contains 6 guitars
    assert guitars[0].name == "Fender Stratocaster"
    assert guitars[1].year == 1922
    assert guitars[2].cost == 1512.9
    print("test_load_guitars passed")

def test_add_new_guitars():
    """Test adding new guitars to the list."""
    guitars = load_guitars('guitars.csv')
    add_new_guitars(guitars)  # Enter new guitar details during this test
    assert len(guitars) > 6  # Ensure at least one new guitar was added
    print("test_add_new_guitars passed")

def test_sort_guitars():
    """Test sorting guitars by year."""
    guitars = load_guitars('guitars.csv')
    guitars.sort()
    for i in range(len(guitars) - 1):
        assert guitars[i].year <= guitars[i + 1].year
    print("test_sort_guitars passed")

def test_save_guitars():
    """Test saving guitars to the CSV file."""
    guitars = load_guitars('guitars.csv')
    add_new_guitars(guitars)  # Enter new guitar details during this test
    save_guitars('guitars_test.csv', guitars)
    # Load the test file and verify its contents
    test_guitars = load_guitars('guitars_test.csv')
    assert len(test_guitars) == len(guitars)
    print("test_save_guitars passed")

def main():
    """Run all tests."""
    test_load_guitars()
    test_add_new_guitars()
    test_sort_guitars()
    test_save_guitars()
    print("All tests passed!")

if __name__ == "__main__":
    main()

