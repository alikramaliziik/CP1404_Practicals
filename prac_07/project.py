class Project:
    """Represent a project with name, start date, end date, priority, and cost."""

    def __init__(self, name, start_date, end_date, priority, cost):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.priority = priority
        self.cost = cost

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, end: {self.end_date}, priority: {self.priority}, cost: ${self.cost:,.2f}"

    def __lt__(self, other):
        """Define less-than comparison based on priority."""
        return self.priority < other.priority



#update
class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Define less-than comparison based on priority."""
        return self.priority < other.priority


#update datetime
from datetime import datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Define less-than comparison based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        """Update the project's completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority

#update for datetime
from datetime import datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Define less-than comparison based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        """Update the project's completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority


#final update woth output
from datetime import datetime

class Project:
    """Represent a project with a name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
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
#defining utility functions
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
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
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
#main program with menu
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

