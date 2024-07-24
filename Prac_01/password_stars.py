"""Password Check Program"""

def main():
    """Main function to execute the program."""
    password = get_password()
    print_password_stars(password)

def get_password():
    """Get the password from the user."""
    return input("Enter your password: ")

def print_password_stars(password):
    """Print stars (*) for each character in the password."""
    print("*" * len(password))

if __name__ == "__main__":
    main()
git