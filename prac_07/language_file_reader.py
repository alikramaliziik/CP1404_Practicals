import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()  # Ignore the header line
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)

# Uncomment the following line to run this version
# main()

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
