# Identity operators 
x = ["apple","banna"]
y = ["apple","banaa"]
z=x 
print(x is z)
print(x is y)
print(x == y)

x = [1,2,3]
y = [1,2,3]
print(x == y)# checks for values 
print(x is y)# check for pointing same object  

#membership operators 
fruits = ["apple","banana","cherry"]
print("banna" in fruits)
print["apple","banana","cherry"] 
 
#ternary operators in python 
num = 10 
res = "Even" if num % 2 == 0 else "odd" 
print(res)  

# wap to  find larger of three numbers  
a = 10 
b = 15   
c = 25
greatest = a if a > b and a > c else b if b > c else c 
print(greatest) 
# wap to  find num 