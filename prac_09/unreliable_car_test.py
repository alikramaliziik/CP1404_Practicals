from prac_09.unreliable_car import UnreliableCar

def main():
    # Create an UnreliableCar with 50% reliability
    unreliable_car = UnreliableCar("Dodge", 100, 50)

    # Try to drive the car a few times and print the result each time
    for i in range(1, 11):
        distance = unreliable_car.drive(20)
        print(f"Attempt {i}: Drove {distance} km")
        print(unreliable_car)

if __name__ == "__main__":
    main()

