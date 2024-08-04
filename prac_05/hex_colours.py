"""
CP1404/CP5632 Practical
Hexadecimal colour lookup program
"""

# Dictionary of colour names and their hexadecimal codes
COLOUR_TO_HEX = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF",
    "BlueViolet": "#8A2BE2",
    "Brown": "#A52A2A",
    "BurlyWood": "#DEB887",
    "CadetBlue": "#5F9EA0",
    "Chartreuse": "#7FFF00",
    "Chocolate": "#D2691E",
    "Coral": "#FF7F50",
    "CornflowerBlue": "#6495ED",
    "Cornsilk": "#FFF8DC",
    "Crimson": "#DC143C"
}

# Print the dictionary
print(COLOUR_TO_HEX)

# Prompt for user input
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()

# Print all colour names and their hexadecimal codes neatly lined up
print("\nAll colour names and their hexadecimal codes:")
for colour, hex_code in COLOUR_TO_HEX.items():
    print(f"{colour:15} is {hex_code}")


#CONSTANT DIC
"""
CP1404/CP5632 Practical
Hexadecimal colour lookup program
"""

# Dictionary of colour names and their hexadecimal codes (constants)
COLOUR_TO_HEX = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

# Print the dictionary (optional)
print(COLOUR_TO_HEX)

# Prompt for user input and convert to uppercase to make case-insensitive
colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()

#HANDLES INVALID COLOR CODES
"""
CP1404/CP5632 Practical
Hexadecimal colour lookup program
"""

# Dictionary of colour names and their hexadecimal codes (constants)
COLOUR_TO_HEX = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

# Print the dictionary (optional)
print(COLOUR_TO_HEX)

while True:
    colour_name = input("Enter colour name (blank to stop): ").strip().upper()

    if colour_name == "":
        break

    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")

print("Program terminated.")
