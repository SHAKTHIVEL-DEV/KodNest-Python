# square using normal fuction 
from List import numbers
numbers=[1,2,3,4,5,6,7,8,9,10] 
def sqaure(n):
     sqaure(n*n)
result=[] 
for num in numbers:
    result.append(num)

print(result) 

#even using normal fuction  

def is_even(n): 
    if n %2 == 0:
        return True 
    else:
        return False 
    even = [] 
    for num in numbers:
        if is_even(num):
            even.append(num)
    print(even)     

# sum using normal function 
def add(x, y): 
    return x + y  
sum_of_num  = 0 
for num in numbers:
    sum_of_num = add(sum_of_num, num)    
print(sum_of_num)     
    