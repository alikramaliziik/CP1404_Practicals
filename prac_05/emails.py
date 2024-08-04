"""
Emails Program
Estimate: 30 minutes
Actual:   48 minutes
"""


def get_name_from_email(email):
    """Extracts and returns the name from an email address."""
    # Remove the domain part from the email
    name_part = email.split('@')[0]
    # Split the name by dots and capitalize each part
    name_parts = name_part.split('.')
    capitalized_name_parts = [part.title() for part in name_parts]
    # Join the parts into a single string
    name = ' '.join(capitalized_name_parts)
    return name


def main():
    email_dict = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name = get_name_from_email(email)
        default_prompt = f"Is your name {name}? (Y/n) "
        prompt = input(default_prompt).strip().lower()

        if prompt == "" or prompt == "y":
            email_dict[email] = name
        else:
            name = input("Name: ").strip()
            email_dict[email] = name

    print()
    for email, name in email_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
