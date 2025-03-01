company_employees = {
"Engineering": {
"Alice": {"age": 30, "role": "Software Engineer"},
"Bob": {"age": 28, "role": "DevOps Engineer"}
},
"HR": {
"Charlie": {"age": 35, "role": "HR Manager"}
}
}

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}

total_employees = sum(len(employees) for employees in company_employees.values())

print(company_employees)
print("The total number of employees is: " + str(total_employees))