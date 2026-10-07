#creat a shallow cpoies 
#1.Normal assingment(not a copy )
original = [[10,20,30,],[40,50]]
copy = original
copy[0][0]=1500
print(original)
print(copy)

#2) Shallow copy 
original= [[10,20,30],[40,50]]
copy=original . copy()
copy[0][0]=1020350
print(copy)
print(original)

#3)Deepcopy / deepcopy
import copy 
original=[[10,20,30],[40,50]]
copy_list=copy.deepcopy(original)
copy_list[0][0]=741327
print(copy_list)
print(original)


