class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        name: string, name of the car (optional, defaults to "")
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self._odometer += distance_driven
        return distance_driven

    def __str__(self):
        """Return a string representation of the Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
from car import Car

def test_car():
    """Run tests on the Car class."""
    # Create a Car object with 100 units of fuel
    my_car = Car("My Car", fuel=100)
    print(f"Initial fuel: {my_car.fuel}")

    # Add 50 units of fuel
    my_car.add_fuel(50)
    print(f"Fuel after adding 50 units: {my_car.fuel}")

    # Attempt to drive 120 kilometers
    distance_driven = my_car.drive(120)
    print(f"Distance driven: {distance_driven}")
    print(f"Fuel left: {my_car.fuel}")
    print(f"Odometer reading: {my_car._odometer}")

    # Attempt to drive another 50 kilometers
    distance_driven = my_car.drive(50)
    print(f"Distance driven: {distance_driven}")
    print(f"Fuel left: {my_car.fuel}")
    print(f"Odometer reading: {my_car._odometer}")

    # Create a new Car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to "limo"
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(f"Current fuel amount in limo: {limo.fuel} units")

    # Attempt to drive the car 115 km
    distance_driven = limo.drive(115)
    print(f"Distance driven: {distance_driven} km")
    print(f"Fuel remaining: {limo.fuel} units")

    # Print the car object using the __str__ method
    print(limo)

    # Testing the Car class with named cars
    your_car = Car("Honda")
    your_car.add_fuel(70)
    your_car.drive(150)
    print(your_car)

if __name__ == "__main__":
    test_car()
