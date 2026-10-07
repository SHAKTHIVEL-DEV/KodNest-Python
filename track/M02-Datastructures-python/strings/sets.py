#creat sets {}
#sets are  unordered , unindexed, and have no duplicate elements {}
#example  
s ={1.2,3,5}
print(s)
print(type(s)) 
#print(s,s[1])  #indexing is not possible in set  
#s[2]=200#it will raise error  
# add the values in sets using add()
s.add(6)
print(s) 
# add multiple values in sets using update()
s.update({7,8,9,10})
print(s)
# removing method in sets using remove()
s.remove(10)
print(s) 
#removing  Anothers methods is discard()
s.discard(9)
print(s)

#removing methods pop()
print(s.pop())
print(s)
#clearing methods in sets  called clear()
s.clear()
print(s) 
#deleting methods in sets called del 
#el s
#rint(s)  

s1 = {1,2,3,4,5,"your",33,87.6,"Hello",True,1,2,3,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5}
print(s1) 

#constructor of set 
s2=set()
s3=set(1,2,3,4,5) 
print(s3) 
# loop 
for n in s3: 
    print(n) 
# frozenset
fs = {1,2,3,4,5} 
fs = frozenset(fs) 
print(fs,type(fs))  