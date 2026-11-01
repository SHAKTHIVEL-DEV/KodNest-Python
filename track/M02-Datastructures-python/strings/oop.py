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
 #instance attributes - seld or obj ref         
        self.name = name
        self.age = age
        self.marks = marks 
#instance method - using self reference obj ref 
#         

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

class student: 
    #class attr 
    company = "jio platfrom limited in relince" 
    #constructor 
    def __init__(self,name,age):
        # #instance attributes - self or obj ref 
        self.name = name 
        self.age = age
    #instance method - using self reference obj ref 
    def study(self): 
        a = 10 # local attribute 
        print(a)
        print(f"{self.name} is studying")
    def getDetails(self):
        print("Name :" ,self.name)
        print("Age :", self.age)
        print("Company :", self.company)  
#stati methods - classname , odj ref 
    @staticmethod
    def trip(name):
        print(f"{name} goes for a trip") 
#class methods - class name , odj ref
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company   

    def trip(self): 
        print(f"{self.name} goes for a trip") 


student.change_company("cognizant")
s1=student("shakthi",20) 
print(student.company)
print(s1.company)
print(s1.name) 
s1.study()
s1.getDetails() 
s1.trip() 

print("\n")
s2 = student("vel",20) 
print(s2.name)
s2.study()
s2.getDetails() 
s2.trip() 




    


    