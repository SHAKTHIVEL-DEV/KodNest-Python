numbers = [1,2,3,4,5,6,7,8,9,10] 
#square numbers using HOF - MAP
def square(n):
    return n * n 
result = map(square,numbers)
print(list(result)) 

#even normla methode   
def is_even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd") 

#Even filter medhode 
even_num = filter(is_even,numbers) 
print(list(even_num)) 

# Sum of numbers using HOF - Reduce
from functools import reduce 
def add(x,y):
    return x + y 

sum_of_num = reduce(add,numbers)
print(sum_of_num)


#Using lambda function in HOF
numbers = [1,2,3,4,5]
result = map(lambda x: x * x, numbers) 
print(list(result)) 

even_num = filter(lambda x: x % 2 == 0, numbers) 
print(list(even_num)) 

sum_of_num = reduce(lambda x,y: x + y, numbers) 
print(sum_of_num)  
