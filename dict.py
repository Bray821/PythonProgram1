alien = {"color":"green","points":5}

print(alien["color"])
print(alien["points"])


player = {"health":40,"speed":120,"attack":50,"defense":30}



player["x_position"] = 3
player["y_position"] = 5

player["moral"] = "terrible"
health = 0

boss = {"health":125,"power":50,"speed":30}

boss["strength"] = "bad"

boost = 0


if boss["strength"] == "powerful":
    boost = boost + 150
elif boss["strength"] == "good":
    boost = boost+50
elif boss["strength"] == "ok":
    boost = boost+10
elif boss["strength"] == "bad":
    boost = boost+0
elif boss["strength"] == "terrible":
    boost = boost-100

boss["health"] = boss["health"] + boost 

print(boss["health"])

print(boss)
del boss["power"]
print(boss[1])