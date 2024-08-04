import csv
from collections import defaultdict


def read_wimbledon_data(filename):
    champions = defaultdict(int)
    countries = set()

    # Open and read the CSV file
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # Skip header if there's any
        next(reader, None)

        # Iterate over each row in the CSV file
        for row in reader:
            champion = row[0]
            country = row[1]

            # Count the number of times each champion has won
            champions[champion] += 1

            # Collect the countries of the champions
            countries.add(country)

    return champions, sorted(countries)  # Return sorted countries


def display_champions(champions):
    print("Champions and their number of wins:")
    for champion, wins in champions.items():
        print(f"{champion}: {wins} wins")


def display_countries(countries):
    print("\nCountries of the champions in alphabetical order:")
    for country in countries:
        print(country)


def main():
    filename = 'wimbledon.csv'
    champions, countries = read_wimbledon_data(filename)
    display_champions(champions)
    display_countries(countries)


if __name__ == "__main__":
    main()

#count number of champions and listing the countries of champs in alphabetical order
import csv
from collections import defaultdict


def read_wimbledon_data(filename):
    champions = defaultdict(int)
    countries = set()

    # Open and read the CSV file
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # Skip header if there's any
        next(reader, None)

        # Iterate over each row in the CSV file
        for row in reader:
            champion = row[2]
            country = row[1]

            # Count the number of times each champion has won
            champions[champion] += 1

            # Collect the countries of the champions
            countries.add(country)

    return champions, sorted(countries)  # Return sorted countries


def display_champions(champions):
    print("Champions and their number of wins:")
    for champion, wins in champions.items():
        print(f"{champion}: {wins} wins")


def display_countries(countries):
    print("\nCountries of the champions in alphabetical order:")
    for country in countries:
        print(country)


def main():
    filename = 'wimbledon.csv'
    champions, countries = read_wimbledon_data(filename)
    display_champions(champions)
    display_countries(countries)


if __name__ == "__main__":
    main()


#read the wimbledon data and rpocess data into data structures and display functions
import csv

def read_wimbledon_data(filename):
    champions = {}
    countries = set()

    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header

        for row in reader:
            champion = row[2]
            country = row[1]

            if champion in champions:
                champions[champion] += 1
            else:
                champions[champion] = 1

            countries.add(country)

    return champions, sorted(countries)

def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion}: {wins}")

def display_countries(countries):
    countries_str = ', '.join(countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:\n{countries_str}")

def main():
    filename = 'wimbledon.csv'
    champions, countries = read_wimbledon_data(filename)
    display_champions(champions)
    display_countries(countries)

if __name__ == "__main__":
    main()
