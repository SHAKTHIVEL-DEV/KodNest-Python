marks = [70,80,60]
stu_mark = marks 
print(marks)
print(stu_mark) 

first = [1,2,3]
second = first 
print(first is second)
print(first == second)  

first = [1,2,3,4,5]
second = [1,2,3,4,5,]  
print(first is second)
print(first == second)  


# modification / mutation 
num = [10,20]
values = num 
values.append(30) 
print(num)  
print(values)   

#Reasingment 
num = [10,20]
values = num 
values = [100,200]
print(num)  
print(values)   

# list comprehension 
num  = [10,20] 
values = num 
values = [100,200] 
print(num) 
print(values)  

