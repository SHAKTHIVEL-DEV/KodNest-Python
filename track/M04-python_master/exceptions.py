#without exception handling code 
from tuples import stu_info
print("starting")
a = 0 
b = 10 / a 
print(b) 
print("ending") \

#with exception handling code 

print("starting")
try:
    a = 0 
    b = 10/ a 
    print(b) 
except:
    print("cannotde  divide by zero") 
print("ending") 

#Type of Exception 
#1 Type Error
try; 
a = 10 
b = "hello"
print(a+b) 
except:
    print("type error")  

#2Key Error 
stu = {"name":"Anand" , "age" :25 , "city":"bengalure"} 
print(stu_info["salary"])  

#3Index Error 
lst = [2,3,5,8]
print(lst[6]) 

#4 Name Error 
print(age) 

#5 Value Error 
a = "hello"
num = int(a) 
print(num) 

 




