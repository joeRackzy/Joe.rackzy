age_of_user = 20
if age_of_user < 2:
    print("you are stil a baby.")

elif (age_of_user == 2) or (age_of_user < 4):
    print("you are a toddler.") 

elif (age_of_user == 4) or (age_of_user < 13):
    print("you are a kid.")
elif (age_of_user == 13) or (age_of_user < 20):
    print("you are a teenager.")

elif(age_of_user == 20) or (age_of_user < 65):
    print("you are adult.")

else:
    print("you are elder.")