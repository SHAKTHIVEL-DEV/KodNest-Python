#Create polymorphism with overloading method 

class Calculatior:
    def add(self,a,b):
        print(a+b) 

    def add (self,a,b,c):
        print(a+b+c)

obj = Calculatior() 
obj.add(10,20,30) 


#Defaualt ARGS 

class Calculatior:
    def add(self,a,b,c=0):
        print(a+b+c) 

obj = Calculatior()
obj.add(10,20)
obj.add(10,10,10)
#obj.add(10) class Add: 

#ARGS MTHODE 
class add:

def sum(self, *args):
    total = 0
    for i in args:
        total += i
    print(total)

obj = Add()
obj.sum(10, 20)
obj.sum(10, 20, 30)
obj.sum(10, 20, 30, 40)  



#Polymorphism  using methode clled overwriting 

#EXAMPLE 


class Payment:
    def pay(self):
        print("Pay for money")

class Gpay(Payment):
    def pay(self):
        print("pay money using Gpay")

class phonepay(Payment):
    def pay(slef):
        print("pay for money uing phonepay") 

g=Gpay() 
g.pay()
g.phonepay()












 

