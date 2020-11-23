class Resturant:
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name = resturant_name
        self.cusine_type = cusine_type
        self.NumberServed = 0
    def describe_resturant(self):

        if type(self.cusine_type) is list:

            for i in self.cusine_type:
                print(f"{self.resturant_name} has very good {i} ans has served {self.NumberServed} customers")
        else:
            print(f"{self.resturant_name} had very good {self.cusine_type} and has seved {self.NumberServed} customers")
    def open_resturant(self,num=""):
        print(f"{self.resturant_name} is open at {num}")
    def set_number_served(self, num):
        self.NumberServed = num
    def add_number_served(self, num):
        self.NumberServed += num
class flavors:
    def __init__(self,flavor1 = "choclate",flavor2 ="strawberry",flavor3="vanilla"):
        self.flavor1 = flavor1
        self.flavor2= flavor2
        self.flavor3 = flavor3
class ice_cream_shop(Resturant):
    def __init__(self,resturant_name,cusine_type):
        super().__init__(resturant_name,cusine_type)
        self.flavors = flavors()
    def ice_cream_stand(self):
       return f"We serve,{self.flavors.flavor1},{self.flavors.flavor2},{self.flavors.flavor3} "

Coldstone = ice_cream_shop("Coldstone","Icecream")

print(Coldstone.ice_cream_stand())