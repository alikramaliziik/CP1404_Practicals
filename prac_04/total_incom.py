## File: accountant_annie

def get_incomes(number_of_months):
    """Prompt the user to enter incomes for the given number of months."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes

def calculate_cumulative_totals(incomes):
    """Calculate cumulative totals from a list of incomes."""
    cumulative_totals = []
    total = 0
    for income in incomes:
        total += income
        cumulative_totals.append(total)
    return cumulative_totals

def display_incomes_and_totals(incomes, cumulative_totals):
    """Display incomes and their cumulative totals."""
    print("\nIncome Report\n-------------")
    for month in range(1, len(incomes) + 1):
        print(f"Month {month:>2} - Income: ${incomes[month - 1]:>10,.2f}         Total: ${cumulative_totals[month - 1]:>10,.2f}")

def main():
    """Main program function."""
    number_of_months = int(input("How many months? "))
    incomes = get_incomes(number_of_months)
    cumulative_totals = calculate_cumulative_totals(incomes)
    display_incomes_and_totals(incomes, cumulative_totals)

if __name__ == "__main__":
    main()

To add values to a list in Python, you can use the append method. The append method adds an element to the end of the list. e.g


def get_incomes(number_of_months):
    """Prompt the user to enter incomes for the given number of months."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)  # Add the income to the list
    return incomes

# The rest of the code remains the same

To keep track of the month number and ensure it starts from 1 for printing purposes, you can use a counter variable. e.g


def main():
    """Main program to calculate and display monthly cumulative totals for incomes."""
    number_of_months = int(input("How many months? "))
    incomes = get_incomes(number_of_months)
    print_income_report(incomes)


def get_incomes(number_of_months):
    """Prompt the user to enter incomes for the given number of months."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    """Print a formatted income report including cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month_number, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month_number:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()


We'll need two loops:

For loop for getting incomes: We'll use a for loop to iterate over the range of months specified by the user. This loop will prompt the user to enter income for each month and store it in a list.

For loop for printing the income report: After collecting all the incomes, we'll use another for loop to iterate over the list of incomes. This loop will print the income report with cumulative totals for each month.

Yes, we'll need a cumulative total variable to update as we loop through the list to display the incomes. This variable will keep track of the total income up to the current month. We'll initialize this variable to 0 before starting the loop, and in each iteration, we'll add the current month's income to the cumulative total. This updated cumulative total will then be displayed in the income report.


#total.income.py
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()

#4 refactored code
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()


#6 refactor move
def print_report(incomes, months):
    """Print income report for the given incomes and number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes, num_months)


main()

#8.updated function
def print_report(month, income, total):
    """Print the income report for a given month."""
    print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
