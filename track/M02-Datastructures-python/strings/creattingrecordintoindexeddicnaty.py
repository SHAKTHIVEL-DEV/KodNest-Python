# creating indexed list 
employees =[
    {"employee_id":"E101","name":"shakthi","department":"developer","salary":50000},
    {"employee_id":"E102","name":"vijay","department":"developer","salary":60000},
    {"employee_id":"E103","name":"vikram","department":"developer","salary":70000},
    {"employee_id":"E104","name":"kavin","department":"developer","salary":80000},
    {"employee_id":"E105","name":"gowtham","department":"developer","salary":90000}   
]  

print(employees)

employee_by_id = {} 

for employee in employees:
    employee_id = employee["employee_id"]
    employee_by_id[employee_id] = employee   
print(employees)  
print(employee_by_id)
# -----------------------------------





#---------------------------------------------------
