class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
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
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance
#test function
def test_car():
    my_car = Car(fuel=100)  # Create a Car object with 100 units of fuel
    print(f"Initial fuel: {my_car.fuel}")

    my_car.add_fuel(50)  # Add 50 units of fuel
    print(f"Fuel after adding 50 units: {my_car.fuel}")

    distance_driven = my_car.drive(120)  # Attempt to drive 120 kilometers
    print(f"Distance driven: {distance_driven}")
    print(f"Fuel left: {my_car.fuel}")
    print(f"Odometer reading: {my_car._odometer}")

    distance_driven = my_car.drive(50)  # Attempt to drive another 50 kilometers
    print(f"Distance driven: {distance_driven}")
    print(f"Fuel left: {my_car.fuel}")
    print(f"Odometer reading: {my_car._odometer}")


if __name__ == "__main__":
    test_car()

#Modifications
"""CP1404/CP5632 Practical - Car class example."""

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
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
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

#1 Create a new Car object called "limo" with 100 units of fuel
limo = Car(100)

#2 Add 20 more units of fuel to "limo"
limo.add_fuel(20)

#3 Print the amount of fuel in the car
print(f"Current fuel amount in limo: {limo.fuel} units")
#output
Current fuel amount in limo: 120 units

# Attempt to drive the car 115 km
distance_driven = limo.drive(115)

# Print the distance actually driven and the amount of fuel remaining
print(f"Distance driven: {distance_driven} km")
print(f"Fuel remaining: {limo.fuel} units")
#output
Distance driven: 100 km
Fuel remaining: 20 units

# Print the car object using the __str__ method
"""CP1404/CP5632 Practical - Car class example."""

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
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
        return f"Car, fuel={self.fuel}, odometer={self._odometer}"



print(limo)
#output
Car, fuel=120, odometer=0


"""CP1404/CP5632 Practical - Car class example."""

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

# Testing the Car class with named cars
if __name__ == "__main__":
    # Create named Car objects
    my_car = Car("Toyota")
    your_car = Car("Honda")

    # Add fuel to the cars
    my_car.add_fuel(50)
    your_car.add_fuel(70)

    # Drive the cars
    my_car.drive(200)
    your_car.drive(150)

    # Display the cars
    print(my_car)
    print(your_car)

#output
Toyota, fuel=0, odometer=200
Honda, fuel=0, odometer=150
