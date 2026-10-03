# creat a list 
numbers=[1,2,3,4,5,6,3] 
print(numbers)

#len in list
print(len(numbers))

#type of list
print(type(numbers))

# using list()constructor  of string list 
stu = list(["your","become","software","developer"]) 
print(stu) 
print(type(stu))

#indexing in list
print(numbers[5]) 

#Adding elements to the list 
numbers.append(7) 
numbers.insert(0,5)
numbers.extend([12,13])
print(numbers)   
#Removing the elaments from list  
numbers =[1,2,3,4,5,6,7,8]
numbers.pop() 
numbers.pop(2) 
numbers.remove(6) 
numbers.clear() 
print(numbers) 
del numbers 

#Changing elemtents the list  
numbers=[1,2,3,4,5,6,7,8,9,9]
numbers[9]=10
numbers[1:4]=[10,20,30,40,50]

print(numbers)







 
