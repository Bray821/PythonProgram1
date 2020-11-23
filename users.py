class Users:
    def __init__(self,FirstName,LastName,Username,Email,Description,Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Username = Username
        self.Email = Email
        self.Description = Description
        self.Password = Password
        self.login_attempts = 0
    def describe_user(self):
        return f"{self.FirstName}\n{self.LastName}\n{self.Username}\n{self.Email}\n{self.Description}\n{self.Password}\n{self.login_attempts}"
    def greet_user(self):
        return f"Welcome Back, {self.FirstName} {self.LastName}"
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attemps(self):
        self.login_attempts = 0


class admin(Users):
    def __init__(self,FirstName,LastName,Username,Email,Description,Password,Privilages):
        self.Privilages = Privilages
        super().__init__(FirstName,LastName,Username,Email,Description,Password)
    def describe_user(self):
        return f"{self.FirstName}\n{self.LastName}\n{self.Username}\b{self.Email}\n{self.Description}\n{self.Password}\n{self.login_attempts}\n{self.Privilages}"