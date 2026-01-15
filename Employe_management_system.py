Employees ={}

def emp_add():
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in Employees:
          print("Employee ID already exists. please Enter a new id")
        else:
            break
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))
    Employees[emp_id] = {
        'Name': name,
        'Age': age,
        'Department': department,
        'Salary': salary
    }
    print("Employee added successfully.")
    
def emp_view():
    if not Employees:
        print("No employees to display.")
        return
    
    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 50)

    for emp_id, details in Employees.items():
        print(f" {emp_id}\t{details['Name']}\t{details['Age']}\t{details['Department']}\t{details['Salary']}")

def search_emp():
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in Employees:
        details = Employees[emp_id]
        print(f"ID: {emp_id}, Name: {details['Name']}, Age: {details['Age']}, Department: {details['Department']}, Salary: {details['Salary']}")
    else:
        print("Employee not found.")

def update_emp():
    emp_id = int(input("Enter Employee ID to update: "))

    if emp_id  not in Employees:
        print("Employee not found.")
        return
    print("\n What do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Department")
    print("4. Salary")
    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        Employees[emp_id]['Name'] = new_name
        print("Name updated successfully.")
    elif choice == '2':
        new_age = int(input("Enter new age: "))
        Employees[emp_id]['Age'] = new_age
        print("Age updated successfully.")
    elif choice == '3':
        new_department = input("Enter new department: ")
        Employees[emp_id]['Department'] = new_department
        print("Department updated successfully.")
    elif choice == '4':
        new_salary = float(input("Enter new salary: "))
        Employees[emp_id]['Salary'] = new_salary
        print("Salary updated successfully.")
    else:
        print("Invalid choice.")
        
    
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            emp_add()
        elif choice == '2':
            emp_view()
        elif choice == '3':
            search_emp()
        elif choice == '4':
            update_emp()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()



