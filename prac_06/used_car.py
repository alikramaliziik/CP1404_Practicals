from guitar import Guitar

def main():
    """Program to manage a list of guitars entered by the user."""
    print("My guitars!")
    guitars = []
    guitar_number = 1

    while True:
        name = input("Name: ")
        if name.strip() == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        guitars.append(Guitar(name, year, cost))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_status = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_status}")

if __name__ == "__main__":
    main()
#adapt guitar for testing with pre-defined data
from guitar import Guitar

def main():
    """Program to manage a list of guitars."""
    print("My guitars!")
    guitars = []
    guitar_number = 1

    # Test data for quick testing without user input
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Uncomment the below section for manual testing with user input
    """
    while True:
        name = input("Name: ")
        if name.strip() == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        guitars.append(Guitar(name, year, cost))
    """

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_status = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_status}")

if __name__ == "__main__":
    main()
#update
from guitar import Guitar

def main():
    """Program to manage a list of guitars."""
    print("My guitars!")
    guitars = []
    guitar_number = 1

    # Test data for quick testing without user input
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Uncomment the below section for manual testing with user input
    """
    while True:
        name = input("Name: ")
        if name.strip() == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        guitars.append(Guitar(name, year, cost))
    """

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_status = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_status}")

if __name__ == "__main__":
    main()
