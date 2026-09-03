men_in_my_house = ["john", "samuel", "joseph", "peter"]
men_in_my_house.append("daniel")
men_in_my_house.insert(0,"david")

print("so sorry that we have to remove joseph! becuase he said he can not make to the party".upper())
del men_in_my_house[3]
while len(men_in_my_house) > 3:
    removing_of_man = men_in_my_house.pop()
    print(f"you will not be going with us: {removing_of_man}")
print("the are only three men in the house".upper())
for remaining_men in men_in_my_house:
    print(f"{remaining_men}: you are the chossen one") 
del men_in_my_house[0]
del men_in_my_house[-1] 
print(men_in_my_house)  
del men_in_my_house[0]
print(men_in_my_house)
