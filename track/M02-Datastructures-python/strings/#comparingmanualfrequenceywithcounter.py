#create a manual frequencey with counter 
language =["python","jave","python","jave","sql","python"] 
frequency = {} 
for l in language:
    if l in frequency:
        frequency [l] +=1
    else:
        frequency [l] = 1
print(frequency) 

#create frequence with Counter 
from collections import Counter 
language =["python","jave","python","jave","sql","python"] 
frequency = Counter(language)
print(frequency) 
print(frequency["python"])
print(frequency["java"])

# most common  
skill=["python",
       "sql",
       "python", 
       "jave",
       "python", 
] 
skill_count = Counter(skill) 
print(skill_count)
frequent_skill = skill_count.most_common()
print(frequent_skill)
frequent_skill = skill_count.most_common(1)
print(frequent_skill)  

most_required = skill_count . most_common(1)
skill = most_required[0][0]
count = most_required[0][1]

print(skill) 
print(count)