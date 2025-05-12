# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []
    for item in employee_data:
        if int(age_lower_limit) < item["age"] < int(age_upper_limit):
            result.append(item)
    return result

def calculate_average_salary():
    total = 0
    average = 0
    for i in employee_data:
        total += i["salary"]
        average = round(total / len(employee_data), 2)
    return average

def get_employees_by_dept(department):
    result = []

    # Add your implementation from here


    return result

def display_records(employee_info):
    print("\nName\tAge\tDepartment\tSalary".expandtabs(15))
    for item in employee_info:
        print(f"{item["name"]}\t{item["age"]}\t{item["department"]}\t{item["salary"]}".expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range (not inclusive of limits)")
    print("4 - Display employee in a department")


    print("Q - Quit")

    option = input("Enter selection => ")
    match option:
        case '1':
            display_records(employee_data)

        case '2':
            average_salary = calculate_average_salary()
            print(f"Average salary = {average_salary}")

        case '3':
            age_lower_limit = input("age (Lower Limit) = ")
            age_upper_limit = input("age (Uper Limit) = ")
            employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
            display_records(employee_info)

        case '4':
            department = input("Name of Department = ")
            employee_info = get_employees_by_dept(department)
            display_records(employee_info)

        case _:
            quit()

def main():

    while True:
        display_main_menu()


if __name__ == "__main__":
    main()