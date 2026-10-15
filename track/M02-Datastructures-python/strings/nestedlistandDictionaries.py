#creat a list of dictionaries 
asha_marks=[78,85,91]
ravi_marks=[72,88,80]
student_marks =[
    [78,85,91],
    [72,88,80],
]   
print(student_marks) 

#Nested lisr 
departments =[
    ["Asha","ravi"],
    ["meera","kiran"],
    ["john","sara"],
]
print(departments) 

#Dictonaries containing lists.
student ={
    "name":"shakthi",
    "subject":["python","sql","machine learning"],
   
}
print(student) 

#Dictionarye containing dictionaries 
students = {
    "name":"shakthi",
    "marks":{
        "python":80,
        "sql":88,
        "machine learning":90,
    } 
}    
print(students) 

#list containing dictioanries 
students=[
    {"name":"Asha",
    "branch":"pyhton",
    },
    {
        "name":"ravi",
        "branch":"EcE" ,
    }
] 
print(students)
