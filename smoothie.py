#s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
#s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
#s2.get_cost() ➞ "$3.50"
#s2.get_price() ➞ "$8.75"
#s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"



prices = {
	"Strawberries" : 1.50, 
	"Banana" :0.50,
	"Mango" : 2.50,
	"Blueberries" : 1.00,
	"Raspberries" : 1.00,
	"Apple" : 1.75,
	"Pineapple" : 3.50,
}

class Smoothie:
    def __init__(self,ingredients):
        self.ingredients = ingredients  
    def get_cost(self):
        num = 0
        for i in self.ingredients:
            if i in prices:
                num+= prices[i]
        rounded_number = round(num,2)
        final_num = str(rounded_number)
        if len(final_num) < len("1.00"):
            final_num+="0"
        return "$"+final_num

    def get_price(self):
        markup_num = 0
        for i in self.ingredients:            
            if i in prices:
                markup_num+= prices[i] + prices[i]*1.5
            rounded_markup_num = round(markup_num,2)
            final_markup_num = str(rounded_markup_num)
        if len(final_markup_num) < len("1.00"):
            final_markup_num+="0"
        return "$"+final_markup_num
    
    def get_name(self):
        alphabatized_ingredients = sorted(self.ingredients)
        names = ""
        for i in alphabatized_ingredients:
            if i in prices:
                if i == "Strawberries":
                    names+= "Strawberry "
                elif i=="Blueberries":
                    names+= "Blueberry "
                elif i == "Rasberries":
                    names += "Raspberry "
                else:
                    names += i+" "        
        if len(alphabatized_ingredients) >len("a"):
            names += "Fusion "
        else:
            names += "Smoothie "

        return names.rstrip()

a_smoothie = Smoothie(["Banana","Strawberries"])


print(a_smoothie.get_price())
print(a_smoothie.get_name())
print(a_smoothie.get_cost())