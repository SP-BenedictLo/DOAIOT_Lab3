import employee_info as eminfo

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]

def test_get_employees_by_age_range():
    result = []
    test_arr = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]

    input_lower = 20
    input_upper = 32
    
    result = eminfo.get_employees_by_age_range(input_lower, input_upper)

    assert result == test_arr


def test_calculate_average_salary():
    result = 0
    check_num = 60166.67
    result = eminfo.calculate_average_salary()

    assert result == check_num

def test_get_employees_by_dept():
    result = []
    input_string = "Engineering"
    test_arr = [
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},]

    result = eminfo.get_employees_by_dept(input_string)

    assert result == test_arr