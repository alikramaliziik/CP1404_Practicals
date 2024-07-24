is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: Set is_finished to True if the result is valid
    except ValueError:  # TODO: Specify the exception to catch
        print("Please enter a valid integer.")
print("Valid result is:", result)
