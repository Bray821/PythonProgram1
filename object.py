class object:
    def __init__(self,Name,Health,Speed,Power):
        self.Name = Name
        self.Health = Health
        self.Speed = Speed
        self.Power = Power
        self.Luck = 0

    def update_luck(self,num):
        self.Luck = num
    def add_luck(self,num):
        self.Luck += num
    def show_stats(self):
        new_words = ""
        dictonary = {
            "Name":self.Name,
            "Health":self.Health,
            "Speed":self.Speed,
            "Power":self.Power,
            "Luck":self.Luck
        }
        for i,v in dictonary.items():
            new_words+= f"\n {i}: {v}"
        return new_words
class player(object):
    def __init__(self,Name,Health,Speed,Power):
        
        super().__init__(Name,Health,Speed,Power)

class enemy(object):
    def __init__(self,enemy_name = "Enemy",enemy_heath =20,Speed = 10, enemy_power = 15):
        self.enemy_name = enemy_name
        self.enemy_heath = enemy_heath
        self.enemy_power = enemy_power
        super().__init__(enemy_name,enemy_heath,Speed,enemy_power)
    def change_enemy_stats(self,Name,Heatlh,Power,Speed):
        self.enemy_name = Name
        self.enemy_heath = Heatlh
        self.enemy_power = Power
        self.Speed = Speed
    def show_enemy_luck(self):
        if self.Luck >=10 and self.Luck<100:
            return "This enemy has some luck"
        elif self.Luck>=100 and self.Luck<10_000:
            return "This enemy has luck"
        elif self.Luck>=10_000:
            return "This enemy is the luckiest"
        else:
            return "Return this enemy does not have much luck"
    def show_stats(self):
        enemy_text = ""
        enemy_dic = {
                    "Name":self.enemy_name,
                    "Health":self.enemy_heath,
                    "Power":self.enemy_power,
                    "Speed":self.Speed,
                    "Luck":self.Luck,
        }             
        for i,v in enemy_dic.items():
            enemy_text += f"\n {i}: {v}"
        return enemy_text
class boss(object):
    def __init__(self,Name,Health,Speed,Power,Destruction):
        self.Destruction = Destruction
        super().__init__(Name,Health,Speed,Power)
        self.enemy = enemy()
    def show_stats(self):
        boss_word =""
        boss_dictonary = {
            "Name":self.Name,
            "Health":self.Health,
            "Speed":self.Speed,
            "Luck":self.Luck,
            "Destruction":self.Destruction,
            "Power":self.Power
        }   
        for i,v in boss_dictonary.items():
            boss_word += f"\n {i}: {v}"
        return boss_word
greg = player("Greg",15,12,21)
greg.update_luck(10)
greg.add_luck(24)

superboss = boss("Plant Eater",25,12,12,"BIG")
superboss.update_luck(15)
superboss.add_luck(12)

superboss.enemy.change_enemy_stats("Small Plant Eater",10,25,12)
print(superboss.show_stats())


print(superboss.enemy.show_stats())

bad_guy = enemy("Bad Guy",23,20)
bad_guy.add_luck(14)
print(bad_guy.show_stats())
superboss.enemy.update_luck(3)
print(superboss.enemy.show_enemy_luck())