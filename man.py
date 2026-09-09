special = ["joseph", "john","mary","mike", "Admin", "faith", "john"]
del special[:]
for name in special:
    if name  == "Admin":
        print(f"{name} I greet you special.".upper())
    else:   
        print(f"{name} you are all welcome")  
print(special)
print("we need to fine more users to the list\n")   

current_user = ["maria", "jennifer", "moses", "samuel", "cicelia"]

new_users = ["joseph", "john","moses","mary","mike","maria", "Admin",
             "faith"]
new_users[4] = "pat"
new_users.insert(4,"joe rackzy")
for new_user in new_users:
    if new_user in current_user:
        print(f"{new_user} please you will have to enter another new user!.")
    else :
        print(f"{new_user} username is available") 

numbers = [1,2,3,4,5,6,7,8,9,]
for number in numbers:
    if number == 1:
        print("1st")
    if number == 2:
        print("2nd")
    else:
        print(f"{number}th")        

alian_1 = {"name": "joseph", "age": 28}

alian_1["x_position"] = 0
alian_1["y_opsition"] = 24
print(alian_1["name"])
print(alian_1["age"])
new_piont = alian_1["age"]
print(f"you are now {new_piont} year old today!")
print(alian_1)


