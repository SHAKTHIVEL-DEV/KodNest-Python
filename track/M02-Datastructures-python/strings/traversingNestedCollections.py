#create a traversing nested collections
from nestedlistandDictionaries import departments
student_marks=[
    [78,85,91],
    [72,88,80],
    [90,84,89]
]

for marks in student_marks:
    for mark in marks:
        print(mark)  

#Traversing dictionary containing lists
departments ={
    "Development":["Asha","Ravi"],
    "Testing":["Meera","Kiran"]
}

for department,employees in departments.items():
    print(department)
    for employee in employees: 
        print(employee)
#

    