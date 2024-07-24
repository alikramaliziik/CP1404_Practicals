line = "CP1401,Ada Lovelace,192"
parts = line.split(',')
subject = parts[0]  # "CP1401"
lecturer = parts[1]  # "Ada Lovelace"
student_number = int(parts[2])  # 192 (converted to integer)


#load_data
def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)  # Append the parts list to the data list
    input_file.close()
    return data  # Return the data list

#full code would be:
FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)  # Append the parts list to the data list
    input_file.close()
    return data  # Return the data list


main()


##new function 'display_subject_details'
def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


def main():
    data = load_data()
    display_subject_details(data)


main()

#the full code would be :
FILENAME = "subject_data.txt"


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data


def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


def main():
    data = load_data()
    display_subject_details(data)


if __name__ == "__main__":
    main()
