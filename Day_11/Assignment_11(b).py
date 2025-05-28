'''
A company has a database of employees, and the HR department needs a system to query employee details efficiently. Each employee has the following attributes: , , , , and . The system should handle two types of queries:: Given an employee ID, retrieve and display all details of the employee.: Given a department name, retrieve and display the names and salaries of all employees in that department, sorted by salary in descending order.
The first line contains T (1≤T≤10), the number of test cases.
The first line of each test case contains N (1≤N≤1000) and Q (1≤Q≤100), space-separated, denoting the number of employees and the number of queries.
The next N lines contain a tuple of 5 fields: , , , , and  (It's guaranteed that no two employees have the same Employee ID).
The next Q lines contain a query:
If the query starts with id:, it is an . The rest of the line contains the Employee ID.
If the query starts with dept:, it is a . The rest of the line contains the department name.
For each , print the details of the employee in the following format:CopyEmployee ID: <id>
Name: <name>
Department: <department>
Salary: <salary>
Joining Date: <joining date>
For each , print the names and salaries of all employees in the department, sorted by salary in descending order:CopyEmployees in <department>:
<name1>: <salary1>
<name2>: <salary2>
...
If no employee is found for a query, print No details found.
1≤T≤10
1≤N≤1000
1≤Q≤100
Employee IDs are unique.
Department names may contain spaces.
Salaries are positive integers.
Joining dates are in the format YYYY-MM-DD.
1 
5 3 
101 John Doe IT 5000 2020-01-15 
102 Jane Smith HR 6000 2019-05-20 
103 Alice Johnson IT 7000 2021-03-10 
104 Bob Brown Finance 5500 2018-11-30 
105 Charlie Davis IT 6500 2022-07-25
 id: 103
dept: IT 
id: 106

Employee ID: 103 
Name: Alice Johnson 
Department: IT 
Salary: 7000 
Joining Date: 2021-03-10 

 Employees in IT:
 Alice Johnson: 7000
 Charlie Davis: 6500
 John Doe: 5000 
 No details found
'''


def process_test_case(N, Q, employees, queries):
    employee_dict = {}
    department_dict = {}

    for emp in employees:
        emp_id, name, dept, salary, join_date = emp
        salary = int(salary)

        employee_dict[emp_id] = (name, dept, salary, join_date)

        if dept not in department_dict:
            department_dict[dept] = []
        department_dict[dept].append((salary, name, emp_id))

    for dept in department_dict:
        department_dict[dept].sort(reverse=True, key=lambda x: x[0])

    for query in queries:
        if query.startswith("id:"):
            emp_id = int(query.split()[1])
            if emp_id in employee_dict:
                name, dept, salary, join_date = employee_dict[emp_id]
                print(f"Employee ID: {emp_id}")
                print(f"Name: {name}")
                print(f"Department: {dept}")
                print(f"Salary: {salary}")
                print(f"Joining Date: {join_date}")
            else:
                print("No details found")

        elif query.startswith("dept:"):
            dept_name = " ".join(query.split()[1:])
            if dept_name in department_dict:
                print(f"Employees in {dept_name}:")
                for salary, name, emp_id in department_dict[dept_name]:
                    print(f"{name}: {salary}")
            else:
                print("No details found")


T = int(input())

for x in range(T):
    N, Q = map(int, input().split())
    employees = []

    for a in range(N):
        employee_data = input().split()
        emp_id = int(employee_data[0])
        name = " ".join(employee_data[1:-3])
        dept = employee_data[-3]
        salary = employee_data[-2]
        join_date = employee_data[-1]
        employees.append((emp_id, name, dept, salary, join_date))

    queries = [input().strip() for i in range(Q)]

    process_test_case(N, Q, employees, queries)



