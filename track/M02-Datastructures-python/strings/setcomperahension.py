# creat set comperahension 

from listcomprehesion import square
from enum import unique
from List import numbers
cities = ["bengaluru","pune","Bengaluru","Pune","chennai"] 
u_cities ={city.lower() for city in cities}
print( type(u_cities)) 
print(u_cities)  
 #normal method 
numbers =[2,3,2,4,3]
unique_squares= []
for number in numbers:
    unique_squares.append(number*number)  
print(unique_squares)

# set comprehnsion method

unique_squares ={number * number for number in numbers}
print(unique_squares)
print(type(unique_squares))

numbers=[2,3,2,4,3] 
square_list=[number * number for number in numbers]
square_set={number * number for number in numbers}
print(square_list)
print(square_set)  

#dictionery comperahension  
# normal methode  

numbers =[2,3,2,4,3]
cube_by_numbers = {}
for numbers in numbers:
    cube_by_numbers[number] = numbers ** 3 
print(cube_by_numbers)     

# comprehnsion method

cube_by_numbers = {number : numbers ** 3 for number in numbers}
print(cube_by_numbers)
print(type(cube_by_numbers))    
     
    
