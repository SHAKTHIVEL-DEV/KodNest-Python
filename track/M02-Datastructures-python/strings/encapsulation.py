#Create Encepsulation 
class student: 
    def __init__(self):
        self.__name = "SHAKTI"
        self.__age = 21 
        
    #getter Method 
    @property 
    def get__name(self):
        return self.__name 

    @property 
    def get_age(self):
        return self.__age 

    #setter methode 
    @get__name.setter 
    def set_name(self , name):
        self.__name = name 

    @get_age.setter 
    def set_age(self,age):
        self.__age = age 

s = student() 

print(s.get__name) #it will print SHAKTI
print(s.set_age)# it will print 21  

s.set_name = "shakti"
s.set_age = 20 

print(s.get__name)# it will print shakti 
print(s.set_age)# it will print 20  


# Access Modifiers 
# public - (name) --> accessible everywhere 
class Student:
    def __init(self):
        self.name = "vel"

s = Student()
print(s.name)

#protected - (_name)--> accessible in same class and child class 
class Student:
    def __init(self):
        self._name = "vel"  

class BioStudent(Student):
    def display(self):
        print(self._name)  

s = Student()
bs = BioStudent()
print(s._name) 
bs.display() 

#private - (__name) --> accessible only in same class  
class Student:
    def __init__(self):
        self.__name = "my career started in backend developer " 

s = Student()
print(s.__name)  




         


 


 

             
    







