#1
A `ValueError` will occur when the input provided for either the numerator or the denominator cannot be converted into an integer. This happens if the input is not a valid integer, such as entering a string or a floating-point number.

#2
A `ZeroDivisionError` will occur when the denominator is 0. This is because division by zero is undefined in mathematics, and Python raises a `ZeroDivisionError` to indicate that the operation is not valid.

#3
Yes, you could change the code to avoid the possibility of a `ZeroDivisionError` by checking if the denominator is zero before performing the division operation. Here's how you can modify the code:

code
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
```

With this modification, if the user enters 0 as the denominator, the program will print "Cannot divide by zero!" before the `ZeroDivisionError` occurs.