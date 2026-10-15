# list compehenshion
#square  
from List import numbers
square = []
for i in range(1,6):
    square.append(i * i)
print(square)   

square=[ i * i for i in range(1,6)]
print(square)

numbers =[i for i in range(1,11) if i % 2 == 0]
print(numbers)

numbers = [10,3,12,5,43,7]
new_list=[i for i in numbers if i >= 10] 
print(new_list)
