# File: lists_warmup.py

numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions:
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False (because "3" is a string, not an integer)
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Print the values to check if predictions are correct
print(numbers[0])          #  3
print(numbers[-1])         #  2
print(numbers[3])          #  1
print(numbers[:-1])        #  [3, 1, 4, 1, 5, 9]
print(numbers[3:4])        #  [1]
print(5 in numbers)        #  True
print(7 in numbers)        #  False
print("3" in numbers)      #  False
print(numbers + [6, 5, 3]) #  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]



# Additional tasks:
# 1. Change the first element of `numbers` to "ten" (the string, not the number 10).
numbers[0] = "ten"

# 2. Change the last element of `numbers` to 1.
numbers[-1] = 1

# 3. Get all the elements from `numbers` except the first two (slice).
numbers_slice = numbers[2:]

# 4. Check if 9 is an element of `numbers`.
is_nine_in_numbers = 9 in numbers

# Print the results of the additional tasks
print(numbers)             # Should print ['ten', 1, 4, 1, 5, 9, 1]
print(numbers_slice)       # Should print [4, 1, 5, 9, 1]
print(is_nine_in_numbers)  # Should print True