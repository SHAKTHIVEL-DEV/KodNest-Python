#create a function 
def add(): 
    a = 50
    b = 50
    print( a + b)  
add()   

#local variable
def student():
    name ="shakthi" # local variable 
    age = 20 # local variable 
    print(name)
    print(age)    
student()  

#How to convert to local varible to globle variable 

def student():
    global a # Globle variable   
    a = 100
    print(a)  

student() 

#How to reasening  globle values or variables out side the fuction 
x = 25 # Globle variable 
def employee():
    name = "vel" # local variable 
    print(name)
    print(x) # local variable 
employee()  
x = 21 # reasening valuese  
print(x)     