#Create an abstract class 

from abc import abstractmethod,ABC 

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass 

    @abstractmethod
    def stop(self):
        pass 

#Abstract class 

class Car(Vehicle):
    def start(self):
        print("Car started")

    @abstractmethod 
    def stop(self):
        print("Car stopped") 
 
#concrete class         

class SportsCar(Car):
    def stop(self):
        print("SportsCar stops") 

v = SportsCar()
v.start()
v.stop()  


    
