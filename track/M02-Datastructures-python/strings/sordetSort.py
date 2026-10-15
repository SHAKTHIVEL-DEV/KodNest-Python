#create sorted()function 

#Asending oredr
marks =[60,73,48,50] 
new_marks = sorted(marks)
print(new_marks)
print(marks)  

#decending order 

marks =[60,73,48,50] 
new_marks = sorted(marks,reverse=True)
print(new_marks)
print(marks)  

#create sort() 
age =[2,30,1,18]
age.sort() 
print(age)   



names=["apple","mango","banana","Orange"]
names.sort()
print(names) 

name={"appele","mango","banana","orange"}
print(sorted(name)) 

#cannot bee use 
name ={"apple","mango","banana","orange"} 
names.sort()
print(names) # Attribute Error because set do not support sort()method 