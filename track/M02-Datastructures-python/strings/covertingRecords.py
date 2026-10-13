#creat a convertinng records into an indexed dictionary 
employees = [
    {"name":"shakthi","age":22,"city":"chennai"},
    {"name":"vijay","age":23,"city":"bangalore"},
    {"name":"vikram","age":24,"city":"mysore"},
    {"name":"kavin","age":25,"city":"mumbai"},
    {"name":"gowtham","age":26,"city":"hyderabad"}   
] 
print(employees)

employees_by_id ={}
for employee in employees:
    employee_id = employee ["employee_id"]
    employees_by_id[employee_id] = employee  
    
print(employees_by_id)
