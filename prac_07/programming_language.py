class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def is_dynamic(self):
        """Determine if a programming language is dynamically typed."""
        return self.typing == "Dynamic"
#using csv module
import csv
from programming_language import ProgrammingLanguage

def using_csv():
    """Language file reader version using the csv module."""
    languages = []
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            reflection = row[2] == "Yes"
            pointer_arithmetic = row[4] == "Yes"
            language = ProgrammingLanguage(row[0], row[1], reflection, int(row[3]), pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)

# Uncomment the following line to run this version
# using_csv()
#

#using namedtuple
import csv
from collections import namedtuple

def using_namedtuple():
    """Language file reader version using a named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    languages = []
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            reflection = row[2] == "Yes"
            pointer_arithmetic = row[4] == "Yes"
            language = Language(row[0], row[1], reflection, int(row[3]), pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(f"{language.name}, {language.typing} Typing, Reflection={language.reflection}, "
              f"Pointer Arithmetic={language.pointer_arithmetic}, First appeared in {language.year}")

# Uncomment the following line to run this version
# using_namedtuple()


#using csv with namedtuple
import csv
from collections import namedtuple

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    languages = []
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in map(Language._make, reader):
            languages.append(row)

    for language in languages:
        print(f"{language.name}, {language.typing} Typing, Reflection={language.reflection}, "
              f"Pointer Arithmetic={language.pointer_arithmetic}, First appeared in {language.year}")

# Uncomment the following line to run this version
# using_csv_namedtuple()
