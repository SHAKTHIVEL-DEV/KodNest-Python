# creat dictinariy are mutable  
# {key :values },mutable key cannot duplcate and value cad be anything  
student ={
    "name":"shakthi",
    "age": 20 , 
    "course":"python", 
    "skills":["python","web development","data science"]   
} 
student.setdefault("name", "shakthi") # if key is present then return the value  else return the value  
student.fromkeys(("name","age","course","skills"), "pass") #  returns the value of the key if the key is present else return the value  
my_deict.copy()#
student["course"]+="SQL"
student.update({"location":"Bengalure"}) 
print (type(student)) 
print(len(student))  
print(student.keys())
print(student.values())
print(student.items())  
print(student.get("age")) 
print(student["name"])  
print(student.pop("age")) 
print(student.popitem()) # pop the last key  values 
print(student.clear())# clearing all elements in the dict 
del student # deleting  the dict in memory  

print (student)

#nested dictiory  
student1 = {
    "name":"shakthi",
    "college name" : "Rilence technology",
    "Department" : "Robotics and Automation",
    
} 

employee = {
    "name": "shakthi",
    "company name":"Rilence technology",
    "Role" : "software engineer" ,
    "spesialization" : "Backend developer",
    "Experience" : "fresher",
    "Skills": ["python","SQL","HTLM", "CSS"] 

        
    } 

print(student1)
print(employee) 
print(employee.update({"salary":15210320})) 
print(student1) 
print(employee)
#nested dictiory loops methods 

for i in student1.items(): 
    print(i)
    print("")
    for j in i.values():   # innerloop for values  
        print(j)    

# loop in sets for student 
for i in student.values(): 
    print(f"{i} =>{student[i]}")
for i in student.keys():
    print(i)
for i in student.items():
    print(i) 
# lopps in sets for students1
for i in student.values(): 
    print(f"{i} =>{student[i]}")
for i in student.keys():
    print(i)
for i in student.items():
    print(i)  

# lopps in sets for employee
for i in employee.values(): 
    print(f"{i} =>{employee[i]}")
for i in employee.keys():
    print(i)
for i in employee.items():
    print(i)                  
