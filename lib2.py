class player:
    def __init__(self,name,health,power,personaility):
        self.name = name
        self.health = health
        self.power = power
        self.personaility = personaility
    def item(self):
        self.health += 5
        print(self.health)
    def description(self):
        print(self.personaility)

greg = player("Greg",102,32,"Good Looking")

greg.item()
lori = player("Lori",18,390,"HOT")

