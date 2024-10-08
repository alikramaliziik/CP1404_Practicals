"""
CP1404/CP5632 Practical - Programming class
Estimate: 30 minutes
Start time: 14:00
End time: 14:50
Actual time taken: 50 minutes
"""
from programming_language import ProgrammingLanguage

def main():
    # Create instances of ProgrammingLanguage
    java = ProgrammingLanguage("Java", "Static", "Yes", 1995)
    cpp = ProgrammingLanguage("C++", "Static", "No", 1983)
    python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)

    # Store them in a list
    languages = [java, cpp, python, vb, ruby]

    # Print each language's details
    for language in languages:
        print(language)

if __name__ == "__main__":
    main()

#test
$ python languages.py
Java, Typing: Static, Reflection: Yes, First appeared in: 1995
C++, Typing: Static, Reflection: No, First appeared in: 1983
Python, Typing: Dynamic, Reflection: Yes, First appeared in: 1991
Visual Basic, Typing: Static, Reflection: No, First appeared in: 1991
Ruby, Typing: Dynamic, Reflection: Yes, First appeared in: 1995

#modification
from programming_language import ProgrammingLanguage

def main():
    # Create instances of ProgrammingLanguage
    java = ProgrammingLanguage("Java", "Static", "Yes", 1995)
    cpp = ProgrammingLanguage("C++", "Static", "No", 1983)
    python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)

    # Store them in a list
    languages = [java, cpp, python, vb, ruby]

    # Print each language's details
    for language in languages:
        print(language)
        # Check if the language is dynamic
        print(f"Is {language.name} dynamically typed? {'Yes' if language.is_dynamic() else 'No'}")

if __name__ == "__main__":
    main()

#test
$ python languages.py
Java, Typing: Static, Reflection: Yes, First appeared in: 1995
Is Java dynamically typed? No
C++, Typing: Static, Reflection: No, First appeared in: 1983
Is C++ dynamically typed? No
Python, Typing: Dynamic, Reflection: Yes, First appeared in: 1991
Is Python dynamically typed? Yes
Visual Basic, Typing: Static, Reflection: No, First appeared in: 1991
Is Visual Basic dynamically typed? No
Ruby, Typing: Dynamic, Reflection: Yes, First appeared in: 1995
Is Ruby dynamically typed? Yes


#adding more languages in
from programming_language import ProgrammingLanguage

def main():
    # Create instances of ProgrammingLanguage
    java = ProgrammingLanguage("Java", "Static", "Yes", 1995)
    cpp = ProgrammingLanguage("C++", "Static", "No", 1983)
    python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)
    javascript = ProgrammingLanguage("JavaScript", "Dynamic", "Yes", 1995)
    swift = ProgrammingLanguage("Swift", "Static", "Yes", 2014)

    # Store them in a list
    languages = [java, cpp, python, vb, ruby, javascript, swift]

    # Print each language's details and check if it is dynamic
    for language in languages:
        print(language)
        print(f"Is {language.name} dynamically typed? {'Yes' if language.is_dynamic() else 'No'}")

if __name__ == "__main__":
    main()

#update
from programming_language import ProgrammingLanguage

def main():
    # Create instances of ProgrammingLanguage
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the details of the languages
    print(python)
    print(ruby)
    print(visual_basic)

    # Create a list of these languages
    languages = [python, ruby, visual_basic]

    # Print the languages in the list
    for language in languages:
        print(language)

if __name__ == "__main__":
    main()

#paper
from programming_language import ProgrammingLanguage

def main():
    # Create instances of ProgrammingLanguage
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the details of the languages
    print(python)
    print(ruby)
    print(visual_basic)

    # Create a list of these languages
    languages = [python, ruby, visual_basic]

    # Print the languages in the list
    for language in languages:
        print(language)

    # Print the names of all dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
