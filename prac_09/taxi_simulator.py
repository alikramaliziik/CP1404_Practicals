from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the list of taxis with their indices."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_taxi_choice(taxis):
    """Get the user's taxi choice and return the corresponding Taxi object."""
    while True:
        try:
            choice = int(input("Choose taxi: "))
            if 0 <= choice < len(taxis):
                return taxis[choice]
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid input. Please enter a number.")


def drive_taxi(taxi):
    """Drive the chosen taxi and return the cost of the trip."""
    while True:
        try:
            distance = float(input("Drive how far? "))
            if distance >= 0:
                cost = taxi.drive(distance)
                print(f"Your {taxi.name} trip cost you ${cost:.2f}")
                return cost
            else:
                print("Distance cannot be negative. Please enter a valid distance.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    # Create taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    while True:
        print("\nq)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            display_taxis(taxis)
            current_taxi = get_taxi_choice(taxis)
            print(f"Selected taxi: {current_taxi}")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                cost = drive_taxi(current_taxi)
                total_bill += cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")


if __name__ == "__main__":
    main()

