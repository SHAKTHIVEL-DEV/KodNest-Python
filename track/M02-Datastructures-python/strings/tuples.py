name = ("hammad","saim", "awais", "hammad") 
print(type(name))
print(name.count("awais"))  
print(name.index("saim"))
print(name[2])
print(name[-3])
yn  = name[0:3]
print(yn)
print(type(yn))
print(name)

#Loop in tuple 
numbers=(1,2,3,4,5,6,7,8,9,0)
for n in numbers:
    print(n) 
print(type(numbers))

fruits=('apple','banana','cherry')
print(fruits)
print(fruits*2)
print(type(fruits))

#constructor in tuple
stu_info = tuple(["Alice",17,520205,True])
print(type(stu_info))  
print(stu_info)
    
n = 10 
print(type(n))
numbers = (1,2,3,4,5,6,7,8,9,0)
print(type(numbers)) 
print(numbers)   


a = 20 
a = 25 
print(a) 

a = [10,20]
a [1] = 25  
print(a)

#Tuple packing and unpacking   
# unpaking tuple  
name = ("shakthi","vel","shakthi" )
n1,n2,n3 = name  
print(n1)
print(n3)
print(n2)  
print(n1)
print(n1,*n2,type(n2)) 
print(n2,type(n2))
print(name) 
#packinng in tuple 
a=10
b=20
c=30 
numbers=(a,b,c)
print(numbers,type(numbers))  

a = (1,2,3,4)
b=(10,20,30,40)
c=a+b
print(c,type(c))  
