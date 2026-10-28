#create class and object 
class Student():
    name = "shakthi"
    age = 20  
    marks = 65 

    def study (self):
        print(f"{self.name} is studying {self.age} year") 
    def play (self):
        print(f"{self.name} is playing {self.age} year") 
#object 

stud1 = Student() 
print(stud1.name)
print(stud1.age)
print(stud1.marks) 

stud1.study()
stud1.play()  

#constructor: automatically called when creating an object 
# __init__() is a constructor 
class Student():
    def __init__(self,name,age,marks): 
        self.name = name
        self.age = age
        self.marks = marks 

    def study (self):
        print(f"{self.name} is studying {self.age} year") 
    def play (self):
        print(f"{self.name} is playing {self.age} year") 
#object 

stud1 = Student("shakthi",20 ,75) 
print(f"name:{stud1.name}\nage:{stud1.age}\nmarks:{stud1.marks}")  
stud2 = Student("vel",20 , 80) 
print(f"name:{stud2.name}\nage:{stud2.age}\nmarks:{stud2.marks}")

stud1.study()
stud1.play()  
    