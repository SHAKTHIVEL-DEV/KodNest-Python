set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9,10} 

#union 
print(set1.union(set2))#1,2,3,4,5,6,7,8,9,10
#intersection
print(set1.intersection(set2))#4,5,6
#difference
print(set1.difference(set2))#1,2,3 
#symmetric_difference
print(set1.symmetric_difference(set2))#1,2,3,7,8,9,10
#update
print(set1.update(set2)) 
print(set1) #1,2,3,4,5,6,7,8,9,10
#remove
print(set1.remove(10))
print(set1)#1,2,3,4,5,6,7,8,9
#discard
print(set1.discard(10))
print(set1)#1,2,3,4,5,6,7,8,9
#pop
print(set1.pop())
print(set1)# Removig elemenths randomly
#clear
print(set1.clear())
print(set1)# clearing all the elements from the set
#issubset
print(set1.issubset(set2))# return True if set1 is a subset of set2  
#issuperset
print(set1.issuperset(set2))#return True if set1 is a superset of set2   
#isdisjoint
print(set1.isdisjoint(set2))# Return True if set1 and set2 have no common elements 