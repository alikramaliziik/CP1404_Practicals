from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi with fanciness of 2
    silver_taxi = SilverServiceTaxi("Lexus", 100, 2)

    # Drive the taxi 18 km
    silver_taxi.drive(18)

    # Calculate the fare and print the result
    fare = silver_taxi.get_fare()
    print(f"The fare for an 18 km trip is: ${fare:.2f}")

    # Ensure the fare is as expected (should be $48.78)
    assert fare == 48.78, f"Test failed: Fare was {fare}, expected $48.78"

    # Print the taxi's details
    print(silver_taxi)

if __name__ == "__main__":
    main()
