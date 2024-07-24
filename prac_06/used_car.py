# used_cars.py
from car import Car

def main():
    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car(100)

    # You can add more code here to interact with the "limo" object if needed
    print(f"Limo fuel: {limo.fuel}")
    print(f"Limo odometer: {limo._odometer}")

if __name__ == '__main__':
    main()

#modification
# used_cars.py

from car import Car  # Assuming car.py is in the same directory

def main():
    # Create named Car objects
    my_car = Car("Toyota")
    your_car = Car("Honda")

    # Add fuel to the cars
    my_car.add_fuel(50)
    your_car.add_fuel(70)

    # Drive the cars
    my_car.drive(200)
    your_car.drive(150)

    # Display the cars using the __str__ method
    print(my_car)
    print(your_car)

if __name__ == "__main__":
    main()

#ouput
Toyota, fuel=0, odometer=200
Honda, fuel=0, odometer=150
