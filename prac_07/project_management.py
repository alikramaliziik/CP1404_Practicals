import csv
from project import Project


def load_projects(filename):
    """Load projects from a CSV file."""
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, start_date, end_date, priority, cost = row
            project = Project(name, start_date, end_date, int(priority), float(cost))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Start Date", "End Date", "Priority", "Cost"])
        for project in projects:
            writer.writerow([project.name, project.start_date, project.end_date, project.priority, project.cost])


def display_projects(projects):
    """Display all projects."""
    for project in projects:
        print(project)


def main():
    """Main function to run the project management program."""
    filename = 'projects.txt'
    projects = load_projects(filename)
    display_projects(projects)

    # Add your code here for user input and other functionalities

    # Save projects back to file
    save_projects(filename, projects)


if __name__ == '__main__':
    main()

#udate with main program and extended menu
import csv
from project import Project
from datetime import datetime


def load_projects(filename):
    """Load projects from a CSV file."""
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            name, start_date, priority, cost_estimate, completion_percentage = row
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost_estimate,
                 project.completion_percentage])


def display_projects(projects):
    """Display all projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("\nCompleted projects:")
    for project in sorted(completed_projects):
        print(project)


def filter_projects_by_date(projects):
    """Filter projects by date and display them."""
    date_str = input("Enter the date (DD/MM/YYYY) to filter projects: ")
    filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]

    print("\nFiltered projects:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_project(projects):
    """Add a new project to the list."""
    name = input("Enter project name: ")
    start_date = input("Enter start date (DD/MM/YYYY): ")
    priority = int(input("Enter priority: "))
    cost_estimate = float(input("Enter cost estimate: "))
    completion_percentage = int(input("Enter completion percentage: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i + 1}. {project}")

    project_number = int(input("Enter the number of the project to update: ")) - 1
    project = projects[project_number]

    completion_percentage = input(f"Enter new completion percentage (current: {project.completion_percentage}): ")
    priority = input(f"Enter new priority (current: {project.priority}): ")

    project.update(
        completion_percentage=int(completion_percentage) if completion_percentage else None,
        priority=int(priority) if priority else None
    )


def main():
    """Main function to run the project management program."""
    filename = 'projects.txt'
    projects = load_projects(filename)
    print("Projects loaded from file:")

    while True:
        print("\nMenu:")
        print("1. Load projects")
        print("2. Save projects")
        print("3. Display projects")
        print("4. Filter projects by date")
        print("5. Add new project")
        print("6. Update project")
        print("7. Save and exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print("Projects loaded from file.")
        elif choice == "2":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved to file.")
        elif choice == "3":
            display_projects(projects)
        elif choice == "4":
            filter_projects_by_date(projects)
        elif choice == "5":
            add_project(projects)
        elif choice == "6":
            update_project(projects)
        elif choice == "7":
            save_choice = input("Do you want to save to the default file before exiting? (y/n): ")
            if save_choice.lower() == 'y':
                save_projects('projects.txt', projects)
                print("Projects saved to default file.")
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()


#last update
import datetime

class Project:
    """Represent a project with a name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update_completion(self, new_completion):
        self.completion_percentage = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority

    def starts_after(self, date):
        return self.start_date > date


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = sorted([project for project in projects if project.starts_after(date)], key=lambda p: p.start_date)

    print("Filtered projects:")
    for project in filtered_projects:
        print(f"  {project}")

def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_index = int(input("Project choice: "))

    new_completion = input("New Percentage (leave blank to keep current): ")
    if new_completion:
        projects[project_index].update_completion(int(new_completion))

    new_priority = input("New Priority (leave blank to keep current): ")
    if new_priority:
        projects[project_index].update_priority(int(new_priority))


def main():
    """Main function to run the project management program."""
    filename = 'projects.txt'
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")

    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

    while True:
        print(menu)
        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 'S':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved projects to {filename}")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input(f"Would you like to save to {filename}? (Y/N): ").upper()
            if save_choice == 'Y':
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()

