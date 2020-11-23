fruit = ["lemon","orange","pear"]

for i in fruit:
    if i == "lemon":
        print("lemons are sour!")
    if i == "orange":
        print("oranges are orange!")
    if i == "pear":
        print("pears are pairs!")

veggies = ["potatoes","corn","celery","tomatoes"]

if "potatoes" in veggies:
    print("Potatoes are in french fries!")
if "corn" in veggies:
    syrup = "                                         corn is in corn syrup :(                     "
    print(syrup.strip())
if "celery" in veggies:
    msg = " CELERY GOES IN PEANUT BUTTER                "
    msg2 = msg.strip()
    print(msg2.lower())
if "tomoatoes" in veggies:
    print("tomoatoes are disgusting")