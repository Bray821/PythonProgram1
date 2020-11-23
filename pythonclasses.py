class Employee:
    def __init__(self,name,title,salary,preformance):
        self.name = name
        self.title = title
        self.salary = salary
        self.preformance = preformance
    
    def update_salary(self,num):
        self.salary = num
        if self.salary >= 100_000:
            self.salary = 99_999
            return f"Salary is to high your salary is {self.salary} "
    def show_stats(self):
        stat_text = ""
        info = {
            "Name: ":self.name,
            "Title: ":self.title,
            "Salary: ":self.salary,
            "Preformance: ":self.preformance
        }
        for i,v in info.items():
            stat_text += i
            stat_text += f"{v} \n"
        
        return stat_text

john = Employee("John","Front End Engineer",75000,9)

print(john.update_salary(102_000))
print(john.show_stats())