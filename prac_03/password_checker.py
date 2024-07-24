#starter
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: !@#$%^&*()_-=+`~,./'[]<>?{}|\\")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your", len(password), "character password is valid:", password)


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    # TODO: if length is right, check each character
    # TODO: if any character is not a digit, a letter, or in SPECIAL_CHARS, return False
    # TODO: if we get here (without returning False), then the password must be valid
    return True


main()

on the previous code we need to complete the "is-valid-password" function. this is done below:


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check if the length of the password is within the specified range
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Check if the password contains at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False

    # Check if the password contains at least one lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return False

    # Check if the password contains at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False

    # Check if the password contains at least one special character
    if SPECIAL_CHARS_REQUIRED:
        has_special = False
        for char in password:
            if char in SPECIAL_CHARACTERS:
                has_special = True
                break
        if not has_special:
            return False

    # If all criteria are met, return True
    return True

#real code now
# Constants
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def has_lowercase(password):
    """Check if the password has at least one lowercase character."""
    for char in password:
        if char.islower():
            return True
    return False


def has_uppercase(password):
    """Check if the password has at least one uppercase character."""
    for char in password:
        if char.isupper():
            return True
    return False


def has_digit(password):
    """Check if the password has at least one digit."""
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special(password):
    """Check if the password has at least one special character."""
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False


def is_valid_password(password):
    """Check if the password meets the specified criteria."""
    return (
        MIN_LENGTH <= len(password) <= MAX_LENGTH
        and has_lowercase(password)
        and has_uppercase(password)
        and has_digit(password)
        and has_special(password)
    )


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")
    print("    and 1 or more special characters:", SPECIAL_CHARACTERS)

    password = input("> ")

    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print("Valid password:", password)


if __name__ == "__main__":
    main()
