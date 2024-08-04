#1
#the code runs well but doesnt adhere to PEP 8 .
#innitial dictionary printout
{'QLD': 'Queensland', 'NSW': 'New South Wales', 'NT': 'Northern Territory', 'WA': 'Western Australia', 'ACT': 'Australian Capital Territory', 'VIC': 'Victoria', 'TAS': 'Tasmania'}

#user interaction
Enter short state: QLD
QLD is Queensland
Enter short state: NSW
NSW is New South Wales

#when a user enters invalid code
Enter short state: ABC
Invalid short state
Enter short state: VIC
VIC is Victoria

#2
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary following PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

#3 case sensitive
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary following PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

#4 loop
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary following PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary
print(CODE_TO_NAME)

# Prompt for user input
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and names neatly lined up
print("\nAll states and their names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

#4 loop
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary following PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary
print(CODE_TO_NAME)

# Prompt for user input
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and names neatly lined up
print("\nAll states and their names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

#5 EAFP
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary following PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary
print(CODE_TO_NAME)

# Prompt for user input
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and names neatly lined up
print("\nAll states and their names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")


#FULL CODE
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary following PEP 8 conventions
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary
print(CODE_TO_NAME)

# Prompt for user input
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and names neatly lined up
print("\nAll states and their names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")
