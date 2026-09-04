my_men = ["john", "samuel", "joseph", "peter"]
my_men.append("daniel")
my_men.insert(0,"david")

print("so sorry that we have to remove joseph! becuase he said he can not make to the party".upper())
del my_men[3]
while len(my_men) > 3:
    removing_of_man = my_men.pop()
    print(f"you will not be going with us: {removing_of_man}")
print("the are only three men in the house".upper())
for remaining_men in my_men:
    print(f"{remaining_men}: you are the chossen one") 
del my_men[0]
del my_men[-1] 
print(my_men)  
del my_men[0]
print(my_men)
