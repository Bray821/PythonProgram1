class player:
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power
        self.players = 0
    def get_stats(self):
        return f"{self.name} {self.health} {self.power}, there is currently {self.players} in the game"
    def update_players(self,numbers):
        self.players = numbers
    def show_players(self):
        return self.players

greg = player("Greg",25,15)
greg = player("Jerry",110,0)
greg.update_players(13)

print(greg.get_stats())

class Employee:
    def __init__(self,name,titile,salary,preformance):
        self.name = name
        self.title = title 
        self.salary = salary
        self.preformance = preformance
        self.bonus = 0
    def update_preformance(self,num):
        self.preformance = num
    def increase_preformance(self,num):
        self.preformance += 1
    def update_salary(self,num):
        self.salary = num
    def increase_salary(self,num):
        self.salary += num
    def show_stats(self,num):
        print("Name:")

joe = Employee("Joe","Front End Developer",75000,8)