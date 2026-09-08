special = ["joseph", "john","mary","mike", "Admin", "faith", "john"]
del special[:]
for name in special:
    if name  == "Admin":
        print(f"{name} I greet you special.".upper())
    else:   
        print(f"{name} you are all welcome")  
print(special)
print("we need to fine more users to the list")   

current_user = ["maria", "jennifer", "moses", "samuel", "cicelia"]
new_users = ["joseph", "john","moses","mary","mike","maria", "Admin",
             "faith"]
for new_user in new_users:
    if new_user in current_user:
        print(f"{new_user} please you will have to enter another new user!.")
    else :
        print(f"{new_user} username is available")   


numbers = [1,2,3,4,5,6,7,8,9,]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    else:
        print(f"{number}th")        




