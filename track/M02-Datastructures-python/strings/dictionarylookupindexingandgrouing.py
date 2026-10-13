#creat a dictionary by looking at the following details 
list_product=[101,102,103,104,150,106,]
print(list_product)

product = {
    "101":["laptop", 12000],
    "102":["phone", 150520],
    "103":["tablet", 12000],
    "104":["headphone", 500],
    "150":["charger", 100],
    "106":["earphone", 200], 
}
 

print(product["102"])  
#printing Another ways using get 
res = product.get("105","product not found") 
print(res)

# Modifying the value 
product[1]=13000 
print(product[1])  

product["102"][0]="smart phone" 
print(product["102"])    

#

        
    