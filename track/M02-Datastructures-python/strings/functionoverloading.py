#create a function overloading 
#NOt posiible to python 
# But can achieve this using default arguments  
# example for default arguments 
def add (a, b=0, c=0, d=0):
    print(a+b+c+d)    
    print(add(10)) # 10 , 0 , 0, 0
    print(add(10,20,30,0)) # 10 , 20, 30 ,0
    print(add(10,50)) # 10 , 50 , 0,0 
    print(add()) # 0,0,0,0
    print(add(10,10,10,20)) # 10,10,10,20 
    print(a)   # error  

# Another one was variable arguments (* args) 

def add(* arg):
    return arg  
print(add(10,20,30,40,50,60)) 
print(add(10,20)) 
#Without using add()
def add(*arg): 
    total = 0 
    for n in arg:
        total = total + n  
    return total 
print(add(10,20)) 
print(add()) 






 
