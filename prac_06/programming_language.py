"""
CP1404/CP5632 Practical - Programming language class
Estimate: 30 minutes
Start time: 14:00
End time: 14:50
Actual time taken: 50 minutes
"""
class Programming Language:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, Typing: {self.typing}, Reflection: {self.reflection}, First appeared in: {self.year}"

# Example usage
if __name__ == "__main__":
    java = ProgrammingLanguage("Java", "Static", "Yes", 1995)
    cpp = ProgrammingLanguage("C++", "Static", "No", 1983)
    python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)

    languages = [java, cpp, python, vb, ruby]
    for language in languages:
        print(language)


#modification
class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, Typing: {self.typing}, Reflection: {self.reflection}, First appeared in: {self.year}"

    def is_dynamic(self):
        """Return True if the language is dynamically typed, otherwise False."""
        return self.typing.lower() == "dynamic"

# Example usage
if __name__ == "__main__":
    java = ProgrammingLanguage("Java", "Static", "Yes", 1995)
    cpp = ProgrammingLanguage("C++", "Static", "No", 1983)
    python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)

    languages = [java, cpp, python, vb, ruby]
    for language in languages:
        print(language)


#update
class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the Programming Language object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed."""
        return self.typing.lower() == "dynamic"
