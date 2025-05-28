# Store and Retrieve Employee Data 

data = []
dict = {}
e_no = int(input("Enter the number of employees : "))
for i in range (1, e_no+1):
    e_id = input("Enter the employee id : ")
    e_name = input("Enter the name of employee : ")
    e_salary = input("Enter the salary of the employee : ")

    dict[i] = {"Employee ID":e_id, "Employee Name":e_name, "Employee Salary":e_salary}

data.append(dict)
data1 = tuple(data)
print(dict)

retrieve = int(input("Enter the employee number to retrieve the data : "))
print(dict[retrieve])
