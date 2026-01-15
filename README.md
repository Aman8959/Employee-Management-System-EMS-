# Employee Management System
A simple command-line based Employee Management System written in Python. This application allows users to add, view, search, and update employee records.

## Features

- **Add Employee**: Add new employees with ID, name, age, department, and salary.
- **View Employees**: Display all employees in a tabular format.
- **Search Employee**: Search for an employee by ID.
- **Update Employee**: Update specific fields (name, age, department, salary) of an existing employee.
- **Menu-Driven Interface**: Easy-to-use menu for navigation.

## Requirements

- Python 3.x

## How to Run

1. Ensure Python is installed on your system.
2. Download or clone the repository.
3. Run the script using the command:
   ```
   python Employe_management_system.py
   ```
4. Follow the on-screen menu to perform operations.

## Usage

- Choose option 1 to add a new employee.
- Choose option 2 to view all employees.
- Choose option 3 to search for an employee by ID.
- Choose option 4 to update an employee's details.
- Choose option 5 to exit the program.

## Data Structure

Employees are stored in a dictionary where:
- Key: Employee ID (integer)
- Value: Dictionary containing 'Name', 'Age', 'Department', 'Salary'

## Notes

- Employee IDs must be unique.
- Age is stored as an integer.
- Salary is stored as a float.
- All inputs are taken via command-line prompts.

## Contributing

Feel free to fork the repository and submit pull requests for improvements.


