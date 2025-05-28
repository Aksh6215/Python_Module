from abc import ABC, abstractmethod

class Ola(ABC):
    @abstractmethod
    def GoogleMap(self):
        pass

    def map(self):
        print("This is in Ola map")

class Payment(ABC):
    @abstractmethod
    def Paytm(self):
        pass

    def pay(self):
        print("This is in Payment")

class Calling(ABC):
    @abstractmethod
    def Jio(self):
        pass

    def call(self):
        print("This is in Calling")

class OlaCab(Ola, Payment, Calling):
    def GoogleMap(self):
        dest = input("Enter your destination: ")
        pickup = input("Enter your pickup location: ")
        return f"Cab Booked from {pickup} to {dest}"
    
    def Paytm(self):
        amount = int(input("Enter the amount to be paid: "))
        return f"Your ride is of {amount} rupees"
    
    def Jio(self):
        choice = input("Your name: ")
        return f"Hello!, {choice}"
    
obj = OlaCab()
obj1 = Ola()
obj2 = Payment()
obj3 = Calling()

# print(obj1.map())
# print(obj2.pay())
# print(obj3.call())
print(obj.Jio())
print(obj.GoogleMap())
print(obj.Paytm())
print(obj.pay())
