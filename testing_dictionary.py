Alien_1 = {"x_position": 0, "y_position":25, "speed": "medium"}
print("Original x_position:" + str(Alien_1["x_position"]))
if Alien_1["speed"] == "slow":
    x_increment = 1
elif Alien_1["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
Alien_1["x_position"]  += x_increment    
print("new x_position:" + str(Alien_1["x_position"]))
print(Alien_1)
