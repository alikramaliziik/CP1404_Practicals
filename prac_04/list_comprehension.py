


# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# List comprehension to create a list of integers from the above list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)

# List comprehension to create a list of only the numbers that are greater than 9
# from the numbers (not strings) you just created
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)

# Use a list comprehension and the join string method
# to create a string (not list) of the last names for those full names longer than 11 characters
# The result should be: 'Harlem, Hendrix, Lovelace'
long_last_names = [name.split()[1] for name in full_names if len(name) > 11]
long_last_names_str = ", ".join(long_last_names)
print(long_last_names_str)
