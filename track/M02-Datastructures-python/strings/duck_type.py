#Create Duck type methode 

from ast import Return
class cat:
    def sound(self):
        print("cat meows")

class cow:
    def sound(self):
        print("cow mows")

def make_sound(animal):
    animal.sound()  

ct = cat()
cw = cow()

make_sound(ct) 
make_sound(cw)  

class GooglePay: 
    def pay(self):
        print("payment through google pay")

class phonepay:
    def pay(self):
        print("payment through phone pay") 

class creadicard:
    def pay(self):
        print("payment through creadicard pay") 

def process_payment(payment):
    payment.pay()

g = GooglePay() 
p = phonepay()
c = creadicard() 

process_payment(g)
process_payment(p)
process_payment(c) 
 

# operator overloading -- + -- dunnder methode __ 

print(3+3)

print("I am backend" + "Developer") 


class student:
    def __init__(self,mark):
        self.mark = mark 
    def __add__(self,other):
        return self .mark + other.mark
    def __mul__(self,other):
       return self.mark * other.mark 

s1 = student(20)
s2 = student(60) 

print(s1 + s2)
print(s1 * s2)  


class preson: 
    def __init__(self, name,age):
        self.name = name 
        self.age = age 
    def __gt__(self,other):
        return self.age > other.age 

p1 = preson("shakthi",20) 
p2 = preson("VEL",21) 
if p1 > p2:
    print(f"{p1.name}give treat")
else:
    print(f"{p2.name} give treat")   


    










                 





