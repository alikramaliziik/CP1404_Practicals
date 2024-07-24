To simulate the stock price behavior, we will need to use two functions from the `random` module:

1. `randint(a, b)`: This function will help us simulate the 50% chance of increase or decrease in the stock price. We will use it to generate a random integer, where if it's 1, the price increases, otherwise, it decreases.

2. `uniform(a, b)`: This function will generate a random floating-point number between the specified range. We will use it to generate the percentage increase or decrease in the stock price.


#1
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
number_of_days = 0  # Initialize the number of days

print(f"Starting price: ${price:,.2f}")  # Print initial price

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1  # Increment the number of days
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}")  # Print price for each day

#2
import random

MIN_PRICE = 1.0  # Minimum allowed price
MAX_PRICE = 100.0  # Maximum allowed price
MAX_INCREASE = 0.175  # Maximum increase percentage (17.5%)
MAX_DECREASE = 0.05  # Maximum decrease percentage (5%)
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
number_of_days = 0  # Initialize the number of days

print(f"Starting price: ${price:,.2f}")  # Print initial price

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1  # Increment the number of days
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}")  # Print price for each day

#3
import random

MIN_PRICE = 1.0  # Minimum allowed price
MAX_PRICE = 100.0  # Maximum allowed price
MAX_INCREASE = 0.175  # Maximum increase percentage (17.5%)
MAX_DECREASE = 0.05  # Maximum decrease percentage (5%)
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"  # Define the output file name

out_file = open(FILENAME, 'w')  # Open the file for writing

price = INITIAL_PRICE
number_of_days = 0  # Initialize the number of days

print(f"Starting price: ${price:,.2f}", file=out_file)  # Write initial price to file

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1  # Increment the number of days
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)  # Write price for each day to file

out_file.close()  # Close the file
