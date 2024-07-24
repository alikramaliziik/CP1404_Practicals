#1
name = input("Enter your name: ")

with open('name.txt', 'w') as file:
    file.write(name)

#2
with open('name.txt', 'r') as file:
    name = file.read().strip()

print(f"Hi {name}!")


#3
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())

result = number1 + number2
print(result)

#4
total = 0

with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)

print(total)

#refactored code
#1
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

#2
with open('name.txt', 'r') as file:
    name = file.read().strip()
print(f"Hi {name}!")

#3
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
print(first_number + second_number)

#4
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(total)
