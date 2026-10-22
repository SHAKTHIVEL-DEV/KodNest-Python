#create a accessing and updating values of nested 
student_marks = [
    [78,85,91]
    [72,88,80]
]
print(student_marks[0]) 
print(student_marks)

#updating a values in nested list 
student_marks[0][1] = 92  
print(student_marks)  

#Accessing a list inside a dictionary 
student ={
    "name":"shakthi",
    "Skills":["python","django", "sql"]
    } 
print(student["Skills"])

#updating a list inside a dictinary  
student["Skills"] [1] ="sql" 
print(student["Skills"]) 
#add a new skills

student["skills"].append("git")
print(student)   

#Accdessing Values in a Nested Dictionary 
student ={
    "name":"shakthi",
    "marks":{
        "python":90,
        "sql":85,
        "machine learning":78,
    }
} 
print(student) 





