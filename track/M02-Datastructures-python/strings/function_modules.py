# module - python file resuseable 
def add (x, y):
    return x + y 
def sun (x, y ):
    return x - y 
def mul (x , y ):
    return x * y 
def div (x , y ):
    return x / y   

#Package - folder containner modules 

#use - defined module 

import calculatormodule as cm                        
print(cm.add(10, 20))  
print(cm.sub(10, 20))
print(cm.mul(10, 20))
print(cm.div(10, 20)) 

#built in/standred library module - math , random  
from math import sqrt 
from math import * 
import math  
print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.factorial(5)) 