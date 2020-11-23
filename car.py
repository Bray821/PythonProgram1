class Car:
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self,milage):
        if milage>= self.odometer_reading:
            self.odometer_reading =milage
        else:
            print("You cannot roll back on odometer")
    
    def increment_odometer(self,miles):
            self.odometer_reading += miles

altima = Car("Altima","A2013","2013")

print(altima.get_descriptive_name())

altima.update_odometer(14)

altima.update_odometer(5)

print(altima.get_descriptive_name())

class ElecticCar(Car):
    def __init__(self,make,model,year)
        super().__init__(make,model,year)

my_tesla = ElecticCar("Tesla","Model S","2019")

print(my_tesla.get_descriptive_name())


#	def getCurrentPage(self):