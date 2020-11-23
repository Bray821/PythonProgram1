current_users =["admin","greg","juan","wang","bob"]
new_users = ["amy","lara","GREG","blake","jerry"]


for i in new_users:
    if i in current_users or i.lower() in current_users or i.upper() in current_users:
        print("sorry this username has been taken!")
    else:
        print(f"Thanks for signing up {i}")



ordinal = list(range(1,10))

for i in ordinal:
    if i == 1:
        print("1st \n")
    elif i == 2:
        print("2nd \n")
    elif i == 3:
        print("3rd \n")
    else:
        print(f"{i}th \n")